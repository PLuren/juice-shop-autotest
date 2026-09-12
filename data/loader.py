import json
from pathlib import Path

def load_json(filename):
    path = Path(__file__).with_name(filename)
    with path.open(encoding="utf-8") as file:
        return json.load(file)