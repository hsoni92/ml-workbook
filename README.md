# ml-workbook

## Pre-commit

To run checks on every commit:

1. Install `uv`:

   ```bash
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. In this repository root, run:

   ```bash
   make setup
   ```

This installs project dependencies with `uv sync`, installs `pre-commit`, and configures the Git hook.

Useful commands:

- `make precommit-install` to (re)install the Git hook
- `make precommit-run` to run all hooks for all files

Every `make` target prechecks that `uv` is installed before running.

### Secure vault (`secure.yaml`)

Paths listed in [secure.yaml](secure.yaml) are encrypted with Fernet when you run `encrypt` locally. Each **regular file** under a configured path becomes **`filename.enc`** next to where the plaintext was (the original basename, including any extension, stays visible before `.enc`). Symlinks are skipped. Anything **Git ignores** (same rules as `git check-ignore`, including nested `.gitignore` files) is not encrypted.

**Safety / data-loss:** ciphertext is written with a same-directory temp file and `os.replace`, so you should not get a truncated `.enc` from a crash mid-write. Decrypt strips one `.enc` layer per run. Overwriting an existing `.enc` emits a warning. Very large single files must fit in one Fernet payload (no sharding).

Provide a Fernet key via `SECURE_VAULT_KEY` in the environment, or in repo-root `.env` as `SECURE_VAULT_KEY=...`, or on the first line of `.secure_key` (both gitignored). Generate a key:

```bash
python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'
```

Encrypt or strip one encryption layer locally. With [uv](https://docs.astral.sh/uv/), run the script directly so dependencies are installed automatically (do not use `uvx python`, which does not add `pyyaml` / `cryptography`):

```bash
make encrypt
make decrypt
```

If those packages are already on your `python`, plain `python scripts/secure_vault.py …` is fine.

**Pre-commit and Git index:** the hook checks that the working tree under secured paths has no remaining plaintext (same rules as `encrypt`), then verifies the index. Under secured paths you may only stage **`.enc`** files (except paths in `allow_staged_non_enc`). Run `encrypt` and `git add` the `.enc` paths (and drop plaintext from the index) before committing.

**Legacy `.vault`:** older versions stored whole directories as a single `dirname.vault` blob. That format is no longer supported. Decrypt any existing `.vault` with the script version that created it (for example from git history) before relying on the current flow.
