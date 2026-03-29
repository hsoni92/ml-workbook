"""Train a causal LM on instruction/response JSONL with a YAML config."""
import argparse
from pathlib import Path

import torch
from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForLanguageModeling

from dataset import build_dataset
from model import load_model_and_tokenizer
from utils import load_config, get_logger, ensure_dir

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config", help="Path to YAML config (e.g. configs/smollm2.yaml)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    config = load_config(root / args.config)
    model_name = config["model_name"]
    train_cfg = config["training"]
    dataset_path = train_cfg.get("dataset", config.get("dataset", "data/support.jsonl"))
    if not Path(dataset_path).is_absolute():
        dataset_path = root / dataset_path

    logger.info("Loading model and tokenizer: %s", model_name)
    model, tokenizer = load_model_and_tokenizer(model_name)

    logger.info("Loading dataset: %s", dataset_path)
    ds = build_dataset(str(dataset_path))
    max_length = train_cfg.get("max_length", 512)

    encoded = []
    for i in range(len(ds)):
        out = tokenizer(
            ds[i]["text"],
            truncation=True,
            max_length=max_length,
            padding="max_length",
            return_tensors=None,
        )
        out["labels"] = out["input_ids"][:]
        encoded.append(out)

    class SimpleDataset(torch.utils.data.Dataset):
        def __init__(self, data):
            self.data = data
        def __len__(self):
            return len(self.data)
        def __getitem__(self, i):
            return {k: torch.tensor(v) for k, v in self.data[i].items()}

    train_dataset = SimpleDataset(encoded)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    output_dir = root / train_cfg["output_dir"]
    ensure_dir(output_dir)

    training_args = TrainingArguments(
        output_dir=str(output_dir),
        num_train_epochs=train_cfg.get("num_epochs", 3),
        per_device_train_batch_size=train_cfg.get("batch_size", 4),
        gradient_accumulation_steps=train_cfg.get("gradient_accumulation_steps", 4),
        learning_rate=train_cfg.get("learning_rate", 2e-5),
        warmup_ratio=train_cfg.get("warmup_ratio", 0.1),
        logging_steps=5,
        save_strategy="epoch",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=data_collator,
    )
    logger.info("Starting training")
    trainer.train()
    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))
    logger.info("Saved to %s", output_dir)


if __name__ == "__main__":
    main()
