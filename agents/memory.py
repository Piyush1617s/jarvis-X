import json
from pathlib import Path

FILE = Path("data/memory.json")


def load_memory():

    if not FILE.exists():

        return []

    with open(FILE, "r") as f:

        return json.load(f)


def save_memory(items):

    with open(FILE, "w") as f:

        json.dump(items, f, indent=4)


def remember(text):

    items = load_memory()

    items.append(text)

    save_memory(items)

    return "Saved."


def show():

    items = load_memory()

    if not items:

        return "Memory is empty."

    output = ""

    for i, item in enumerate(items, 1):

        output += f"{i}. {item}\n"

    return output