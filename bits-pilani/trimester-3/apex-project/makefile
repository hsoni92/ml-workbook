NOTEBOOK := Apex2_Week2_Notebook_2025EM1100506_Himanshu_Soni.ipynb
OUTPUT := Apex2_Week2_Notebook_2025EM1100506_Himanshu_Soni_executed.ipynb
DATA_DIR := data
DATA_FILE := $(DATA_DIR)/bank-full.csv
UCI_ZIP_URL := https://archive.ics.uci.edu/static/public/222/bank+marketing.zip

.PHONY: execute run sync data clean

# Default: execute notebook headlessly (no browser)
execute run: sync data
	@echo "Executing $(NOTEBOOK) (no browser)..."
	uv run jupyter nbconvert \
		--to notebook \
		--execute \
		--ExecutePreprocessor.timeout=600 \
		--output "$(OUTPUT)" \
		"$(NOTEBOOK)"
	@echo "Wrote $(OUTPUT)"

# Download UCI Bank Marketing (bank-full.csv) if missing
data: $(DATA_FILE)

$(DATA_FILE):
	@mkdir -p $(DATA_DIR)
	@echo "Downloading bank marketing dataset from UCI..."
	@curl -fsSL "$(UCI_ZIP_URL)" -o /tmp/apex-bank-outer.zip
	@unzip -p /tmp/apex-bank-outer.zip bank.zip > /tmp/apex-bank-inner.zip
	@unzip -p /tmp/apex-bank-inner.zip bank-full.csv > "$(DATA_FILE)"
	@rm -f /tmp/apex-bank-outer.zip /tmp/apex-bank-inner.zip
	@echo "Saved $(DATA_FILE)"

sync:
	uv sync

clean:
	rm -rf $(DATA_DIR) "$(OUTPUT)"
