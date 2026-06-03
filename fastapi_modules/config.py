
import yaml
from pathlib import Path


CONFIG_FILE = Path("config.yaml")

with CONFIG_FILE.open("r") as f:
    config = yaml.safe_load(f)