.PHONY: check-uv setup precommit-install precommit-run encrypt decrypt

check-uv:
	@command -v uv >/dev/null 2>&1 || { \
		echo "Error: uv is not installed."; \
		echo "Install uv: https://docs.astral.sh/uv/getting-started/installation/"; \
		exit 1; \
	}

setup: check-uv
	cd scripts && uv sync
	uv tool install pre-commit
	uv tool run pre-commit install

precommit-install: check-uv
	uv tool install pre-commit
	uv tool run pre-commit install

precommit-run: check-uv
	uv tool run pre-commit run --all-files

encrypt: check-uv
	cd scripts && uv run secure_vault.py encrypt

decrypt: check-uv
	cd scripts && uv run secure_vault.py decrypt
