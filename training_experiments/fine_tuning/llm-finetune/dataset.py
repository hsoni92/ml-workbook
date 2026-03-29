"""Load and prepare JSONL datasets for fine-tuning."""
import json
from pathlib import Path

from torch.utils.data import Dataset


def load_jsonl(path: str) -> list[dict]:
    """Load a JSONL file into a list of dicts."""
    path = Path(path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parent / path
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


class InstructionDataset(Dataset):
    """Dataset that formats instruction/response pairs as a single text for causal LM."""

    def __init__(self, rows: list[dict], template: str = "### Instruction:\n{instruction}\n\n### Response:\n{response}"):
        self.rows = rows
        self.template = template

    def __len__(self) -> int:
        return len(self.rows)

    def __getitem__(self, i: int) -> dict:
        row = self.rows[i]
        text = self.template.format(
            instruction=row.get("instruction", row.get("input", "")),
            response=row.get("response", row.get("output", "")),
        )
        return {"text": text}


def build_dataset(path: str, **kwargs) -> InstructionDataset:
    """Load JSONL and return an InstructionDataset."""
    rows = load_jsonl(path)
    return InstructionDataset(rows, **kwargs)
