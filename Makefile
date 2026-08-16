.PHONY: check-uv check-node setup precommit-install precommit-run encrypt decrypt notes-pdf-setup notes-pdf notes-pdf-t3 mermaid-setup mermaid-validate

check-uv:
	@command -v uv >/dev/null 2>&1 || { \
		echo "Error: uv is not installed."; \
		echo "Install uv: https://docs.astral.sh/uv/getting-started/installation/"; \
		exit 1; \
	}

check-node:
	@command -v node >/dev/null 2>&1 || { \
		echo "Error: node (>=20) is not installed."; \
		echo "Install Node: https://nodejs.org/en/download"; \
		exit 1; \
	}
	@node -e "process.exit(Number(process.versions.node.split('.')[0]) >= 20 ? 0 : 1)" || { \
		echo "Error: node >=20 required (found $$(node --version))."; \
		exit 1; \
	}

setup: check-uv check-node
	cd scripts && uv sync
	uv tool install pre-commit
	uv tool run pre-commit install
	$(MAKE) mermaid-setup

precommit-install: check-uv check-node
	uv tool install pre-commit
	uv tool run pre-commit install

precommit-run: check-uv
	uv tool run pre-commit run --all-files

encrypt: check-uv
	cd scripts && uv run secure_vault.py encrypt

decrypt: check-uv
	cd scripts && uv run secure_vault.py decrypt

verify-encryption:
	python3 scripts/secure_vault.py pre-commit

notes-pdf-setup: check-uv
	cd scripts && uv sync && uv run playwright install chromium

notes-pdf: check-uv
	cd scripts && uv run notes-pdf-gen.py $(ARGS)

notes-pdf-t3: check-uv
	cd scripts && uv run python ../notes-pdf-compact.py $(ARGS)

mermaid-setup: check-node
	npm install

mermaid-validate: check-node
	node scripts/validate-mermaid.js

# Auto-fix safe issues (maid's level-1 fixes: e.g. unquoting parens in labels).
# Use with care — review the diff before committing.
mermaid-validate-fix: check-node
	npx -y @probelabs/maid --fix bits-pilani/
