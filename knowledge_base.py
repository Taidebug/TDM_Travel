import json
from pathlib import Path

def load_guide():
    file_path = Path(__file__).with_name("knowledge_base.json")
    with open(file_path, "r", encoding="utf-8") as file:
        entries = json.load(file)
    return entries

if __name__ == "__main__":
    guide = load_guide()

    print("Num", len(guide))
     