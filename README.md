# ml-workbook

## Pre-commit

To run checks on every commit:

1. Install the CLI (pick one):

   ```bash
   uv tool install pre-commit
   ```

   Or: `pip install pre-commit`

2. In this repository root, install the Git hook:

   ```bash
   pre-commit install
   ```

Optional: run all hooks on the whole repo once with `pre-commit run --all-files`. See [pre-commit](https://pre-commit.com/) for details.

### Secure vault (`secure.yaml`)

Paths listed in [secure.yaml](secure.yaml) are encrypted with Fernet before the staged-file check runs. Each **regular file** under a configured path becomes **`filename.enc`** next to where the plaintext was (the original basename, including any extension, stays visible before `.enc`). Symlinks are skipped. Anything **Git ignores** (same rules as `git check-ignore`, including nested `.gitignore` files) is not encrypted.

**Safety / data-loss:** ciphertext is written with a same-directory temp file and `os.replace`, so you should not get a truncated `.enc` from a crash mid-write. Decrypt strips one `.enc` layer per run. Overwriting an existing `.enc` emits a warning. Very large single files must fit in one Fernet payload (no sharding).

Provide a Fernet key via `SECURE_VAULT_KEY` in the environment, or in repo-root `.env` as `SECURE_VAULT_KEY=...`, or on the first line of `.secure_key` (both gitignored). Generate a key:

```bash
python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'
```

Encrypt or strip one encryption layer locally. With [uv](https://docs.astral.sh/uv/), run the script directly so dependencies are installed automatically (do not use `uvx python`, which does not add `pyyaml` / `cryptography`):

```bash
uv run scripts/secure_vault.py encrypt
uv run scripts/secure_vault.py decrypt
```

If those packages are already on your `python`, plain `python scripts/secure_vault.py …` is fine.

**Pre-commit and Git index:** the hook runs `encrypt` then verifies the index. Under secured paths you may only stage **`.enc`** files (except paths in `allow_staged_non_enc`). After the hook encrypts plaintext, `git add` the new or updated `.enc` paths (and remove plaintext from the index if needed), then commit. Whenever the hook changes what is on disk, refresh what is staged before committing.

**Legacy `.vault`:** older versions stored whole directories as a single `dirname.vault` blob. That format is no longer supported. Decrypt any existing `.vault` with the script version that created it (for example from git history) before relying on the current flow.
