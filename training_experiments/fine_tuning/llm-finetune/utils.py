"""Shared utilities."""
import os
import yaml
import logging


def load_config(path: str) -> dict:
    """Load a YAML config file."""
    with open(path) as f:
        return yaml.safe_load(f)


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Return a logger with a stream handler."""
    log = logging.getLogger(name)
    log.setLevel(level)
    if not log.handlers:
        h = logging.StreamHandler()
        h.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        log.addHandler(h)
    return log


def ensure_dir(path: str) -> None:
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
