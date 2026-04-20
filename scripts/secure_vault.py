#!/usr/bin/env python3
# /// script
# dependencies = [
#   "cryptography",
#   "pyyaml",
# ]
# ///
"""Encrypt/decrypt files under paths listed in secure.yaml (repo root)."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

import yaml
from cryptography.fernet import Fernet, InvalidToken

ENV_KEY = "SECURE_VAULT_KEY"
CONFIG_NAME = "secure.yaml"
_CHECK_IGNORE_BATCH = 8192
_MAX_REPORTED_PATHS = 4


def git_toplevel() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        print("secure_vault: not inside a git repository", file=sys.stderr)
        sys.exit(1)
    return Path(out.stdout.strip()).resolve()


def load_config(root: Path) -> tuple[list[str], set[str]]:
    cfg_path = root / CONFIG_NAME
    if not cfg_path.is_file():
        print(f"secure_vault: missing {cfg_path}", file=sys.stderr)
        sys.exit(1)
    data = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    paths = data.get("paths") or []
    if not isinstance(paths, list):
        print("secure_vault: secure.yaml 'paths' must be a list", file=sys.stderr)
        sys.exit(1)
    allow = data.get("allow_staged_non_enc") or []
    if not isinstance(allow, list):
        print("secure_vault: allow_staged_non_enc must be a list", file=sys.stderr)
        sys.exit(1)
    norm_paths = [normalize_rel(p) for p in paths if p]
    allow_set = {normalize_rel(p) for p in allow if p}
    allow_set.add(normalize_rel(CONFIG_NAME))
    return norm_paths, allow_set


def normalize_rel(p: str) -> str:
    return str(Path(p).as_posix()).strip().strip("/")


def rel_posix_under_root(root: Path, path: Path, root_resolved: Path | None = None) -> str | None:
    rr = root_resolved or root.resolve()
    try:
        return path.resolve().relative_to(rr).as_posix()
    except ValueError:
        return None


def git_ignored_relpaths(root: Path, relpaths: list[str]) -> set[str]:
    """Paths Git would ignore (root + nested .gitignore), via git check-ignore."""
    ignored: set[str] = set()
    if not relpaths:
        return ignored
    rr = str(root.resolve())
    for i in range(0, len(relpaths), _CHECK_IGNORE_BATCH):
        batch = relpaths[i : i + _CHECK_IGNORE_BATCH]
        payload = "\0".join(batch) + "\0"
        r = subprocess.run(
            ["git", "-C", rr, "check-ignore", "-z", "--stdin"],
            input=payload,
            capture_output=True,
            text=True,
        )
        if r.returncode not in (0, 1):
            msg = (r.stderr or "").strip() or f"exit {r.returncode}"
            print(f"secure_vault: git check-ignore failed: {msg}", file=sys.stderr)
            sys.exit(1)
        if r.stdout:
            ignored.update(p for p in r.stdout.split("\0") if p)
    return ignored


def _walk_encrypt_candidates(root: Path, target: Path) -> list[Path]:
    """Regular files under target; no symlinks, no .git/, no existing .enc names."""
    rr = root.resolve()
    out: list[Path] = []
    try:
        target.resolve().relative_to(rr)
    except ValueError:
        return out

    if target.is_file():
        if target.is_symlink():
            return out
        if target.name.endswith(".enc"):
            return out
        return [target]

    if not target.is_dir() or target.is_symlink():
        return out

    for dirpath, dirnames, filenames in os.walk(target, followlinks=False):
        dp = Path(dirpath)
        if ".git" in dirnames:
            dirnames.remove(".git")
        dirnames[:] = [d for d in dirnames if not (dp / d).is_symlink()]
        for name in filenames:
            p = dp / name
            if p.is_symlink() or not p.is_file():
                continue
            if p.name.endswith(".enc"):
                continue
            if rel_posix_under_root(root, p) is None:
                continue
            out.append(p)
    return out


def _encrypt_candidates_with_rel(
    root: Path, target: Path, rel: str, root_resolved: Path | None = None
) -> list[tuple[Path, str]]:
    candidates = _walk_encrypt_candidates(root, target)
    if not candidates:
        return []
    rr = root_resolved or root.resolve()
    out: list[tuple[Path, str]] = []
    for p in candidates:
        rp = rel_posix_under_root(root, p, root_resolved=rr)
        if rp is None:
            print(f"secure_vault: path escapes repo root: {rel}", file=sys.stderr)
            return []
        out.append((p, rp))
    return out


def files_to_encrypt(root: Path, target: Path, rel: str) -> list[Path]:
    pairs = _encrypt_candidates_with_rel(root, target, rel)
    if not pairs:
        return []
    rels = [rp for _, rp in pairs]
    ignored = git_ignored_relpaths(root, rels)
    return [p for p, rp in pairs if rp not in ignored]


def _atomic_replace_bytes(dest: Path, data: bytes) -> None:
    """Write data to dest via a same-directory temp file and os.replace (crash-safe replace)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.parent / f".{dest.name}.tmp.{os.getpid()}"
    try:
        tmp.write_bytes(data)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
    try:
        os.replace(tmp, dest)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


def try_load_key_from_repo(root: Path) -> None:
    """If SECURE_VAULT_KEY is unset, read from repo-root .env or .secure_key."""
    if os.environ.get(ENV_KEY):
        return
    env_path = root / ".env"
    if env_path.is_file():
        try:
            text = env_path.read_text(encoding="utf-8")
        except OSError:
            text = ""
        prefix = f"{ENV_KEY}="
        for line in text.splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.startswith(prefix):
                val = s[len(prefix) :].strip()
                if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                    val = val[1:-1]
                val = val.split("#", 1)[0].strip()
                if val:
                    os.environ[ENV_KEY] = val
                    return
    key_path = root / ".secure_key"
    if key_path.is_file():
        try:
            for line in key_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    os.environ[ENV_KEY] = line.split("#", 1)[0].strip()
                    return
        except OSError:
            pass


def get_fernet() -> Fernet:
    raw = os.environ.get(ENV_KEY)
    if not raw:
        print(
            f"secure_vault: set {ENV_KEY} (export, or add {ENV_KEY}=... to repo-root .env, "
            f"or put the key on the first line of .secure_key). Generate one with: "
            f'python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"',
            file=sys.stderr,
        )
        sys.exit(1)
    key = raw.encode() if isinstance(raw, str) else raw
    try:
        return Fernet(key)
    except ValueError as e:
        print(f"secure_vault: invalid Fernet key: {e}", file=sys.stderr)
        sys.exit(1)


def encrypt_path(fernet: Fernet, path: Path) -> None:
    data = path.read_bytes()
    token = fernet.encrypt(data)
    out = path.with_name(path.name + ".enc")
    if out.exists():
        print(f"secure_vault: warning: overwriting existing {out}", file=sys.stderr)
    _atomic_replace_bytes(out, token)
    path.unlink()


def decrypt_file(fernet: Fernet, path: Path) -> None:
    if not path.name.endswith(".enc"):
        return
    raw = path.read_bytes()
    try:
        plain = fernet.decrypt(raw)
    except InvalidToken:
        print(
            f"secure_vault: decrypt failed for {path}\n"
            "  Fernet rejected the ciphertext (wrong SECURE_VAULT_KEY vs key used at encrypt time, "
            "or truncated/corrupt file). If every .enc fails, fix the key first.",
            file=sys.stderr,
        )
        sys.exit(1)
    out = path.with_name(path.name[: -len(".enc")])
    if out.exists():
        print(f"secure_vault: warning: overwriting existing {out}", file=sys.stderr)
    _atomic_replace_bytes(out, plain)
    path.unlink()


def cmd_encrypt(root: Path, fernet: Fernet, rel_paths: list[str]) -> None:
    rr = root.resolve()
    for rel in rel_paths:
        target = (root / rel).resolve()
        try:
            target.relative_to(rr)
        except ValueError:
            print(f"secure_vault: path escapes repo root: {rel}", file=sys.stderr)
            continue
        if not target.exists():
            print(f"secure_vault: skip missing path: {rel}", file=sys.stderr)
            continue
        if target.is_symlink():
            continue
        for path in files_to_encrypt(root, target, rel):
            encrypt_path(fernet, path)


def collect_enc_files(root: Path, rel: str) -> list[Path]:
    target = (root / rel).resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        print(f"secure_vault: path escapes repo root: {rel}", file=sys.stderr)
        return []
    if not target.exists():
        enc_only = (root / rel).with_name(Path(rel).name + ".enc")
        if enc_only.is_file() and not enc_only.is_symlink():
            try:
                enc_only.resolve().relative_to(root.resolve())
            except ValueError:
                return []
            return [enc_only.resolve()]
        print(f"secure_vault: skip missing path: {rel}", file=sys.stderr)
        return []
    if target.is_file():
        if target.is_symlink():
            return []
        if target.name.endswith(".enc"):
            return [target]
        enc = target.with_name(target.name + ".enc")
        if enc.is_file() and not enc.is_symlink():
            return [enc]
        return []
    found: list[Path] = []
    if target.is_dir():
        for dirpath, dirnames, filenames in os.walk(target, followlinks=False):
            dirnames[:] = [d for d in dirnames if not (Path(dirpath) / d).is_symlink()]
            for name in filenames:
                p = Path(dirpath) / name
                if p.is_symlink() or not p.name.endswith(".enc"):
                    continue
                if p.is_file():
                    found.append(p)
    return found


def cmd_decrypt(root: Path, fernet: Fernet, rel_paths: list[str]) -> None:
    batch: list[Path] = []
    rr = root.resolve()
    for rel in rel_paths:
        target = (root / rel).resolve()
        try:
            target.relative_to(rr)
        except ValueError:
            print(f"secure_vault: path escapes repo root: {rel}", file=sys.stderr)
            continue
        batch.extend(collect_enc_files(root, rel))
    batch.sort(key=lambda p: len(str(p)), reverse=True)
    for p in batch:
        decrypt_file(fernet, p)


def is_under_secure_path(staged: str, secure_paths: list[str]) -> bool:
    s = normalize_rel(staged)
    for p in secure_paths:
        if s == p:
            return True
        if s.startswith(p + "/"):
            return True
    return False


def staged_files(root: Path) -> list[str]:
    return staged_files_under(root, [])


def staged_files_under(root: Path, secure_paths: list[str]) -> list[str]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"]
    if secure_paths:
        cmd.extend(["--", *secure_paths])
    out = subprocess.run(
        cmd,
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    return [line.strip() for line in out.stdout.splitlines() if line.strip()]


def print_path_list(paths: list[str], max_items: int = _MAX_REPORTED_PATHS) -> None:
    shown = paths[:max_items]
    for p in shown:
        print(f"  {p}", file=sys.stderr)
    remaining = len(paths) - len(shown)
    if remaining > 0:
        print(f"  +{remaining} others", file=sys.stderr)


def check_staged(root: Path, secure_paths: list[str], allow: set[str]) -> None:
    bad: list[str] = []
    for name in staged_files_under(root, secure_paths):
        n = normalize_rel(name)
        if n in allow:
            continue
        if not is_under_secure_path(n, secure_paths):
            continue
        if n.endswith(".enc"):
            continue
        bad.append(name)
    if bad:
        print(
            "secure_vault: under secured paths you may only stage .enc ciphertext "
            "(or paths listed in allow_staged_non_enc). Offending:",
            file=sys.stderr,
        )
        print_path_list(bad)
        sys.exit(1)


def assert_vault_clean(root: Path, rel_paths: list[str]) -> None:
    """Exit with an error if any plaintext file under secured paths would be encrypted."""
    rr = root.resolve()
    valid_secure_paths: list[str] = []
    for rel in rel_paths:
        target = (root / rel).resolve()
        try:
            target.relative_to(rr)
        except ValueError:
            print(f"secure_vault: path escapes repo root: {rel}", file=sys.stderr)
            continue
        if not target.exists() or target.is_symlink():
            continue
        valid_secure_paths.append(rel)
    if not valid_secure_paths:
        return

    out = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", *valid_secure_paths],
        cwd=root,
        capture_output=True,
        check=True,
    )
    rels = [p for p in out.stdout.decode("utf-8", errors="surrogateescape").split("\0") if p]

    bad: list[str] = []
    for rp in rels:
        if rp.endswith(".enc"):
            continue
        p = (root / rp).resolve()
        try:
            p.relative_to(rr)
        except ValueError:
            continue
        if not p.exists() or p.is_symlink() or not p.is_file():
            continue
        bad.append(rp)
    bad = sorted(set(bad))
    if bad:
        print(
            "secure_vault: secured paths must contain only ciphertext (.enc) or gitignored files; "
            "plaintext files remain. Run: python scripts/secure_vault.py encrypt",
            file=sys.stderr,
        )
        print_path_list(bad)
        sys.exit(1)


def cmd_pre_commit(root: Path, rel_paths: list[str], allow: set[str]) -> None:
    assert_vault_clean(root, rel_paths)
    check_staged(root, rel_paths, allow)


def main() -> None:
    parser = argparse.ArgumentParser(description="Secure vault encrypt/decrypt (see secure.yaml).")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser(
        "encrypt",
        help="Each regular file -> basename.enc in place; skip gitignored paths.",
    )
    sub.add_parser(
        "decrypt",
        help="Strip one .enc layer from files under configured paths.",
    )
    sub.add_parser(
        "pre-commit",
        help="Verify working tree and index (only .enc under secured paths).",
    )
    args = parser.parse_args()

    root = git_toplevel()
    rel_paths, allow = load_config(root)

    if args.command == "encrypt":
        try_load_key_from_repo(root)
        cmd_encrypt(root, get_fernet(), rel_paths)
    elif args.command == "decrypt":
        try_load_key_from_repo(root)
        cmd_decrypt(root, get_fernet(), rel_paths)
    else:
        cmd_pre_commit(root, rel_paths, allow)


if __name__ == "__main__":
    main()
