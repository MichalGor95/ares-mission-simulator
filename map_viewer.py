import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def clear():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\033[2J\033[H", end="")

def load_and_print(filename="world.json"):
    path = os.path.join(BASE_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Nie znaleziono pliku world.json — najpierw uruchom main.py")
        return

    size = data["size"]
    elements = {
        tuple(map(int, k.split(","))): v
        for k, v in data["elements"].items()
    }

    symbols = {
        "KRATER":   "#",
        "STACJA":   "$",
        "RADIACJA": "~",
        "ANOMALIA": "X",
    }

    clear()
    print("  Legenda: X=cel  #=krater  $=stacja  ~=radiacja  .=puste")
    print("  " + "-" * (size * 2 + 3))
    for y in range(size, -size - 1, -1):
        row = "| "
        for x in range(-size, size + 1):
            if (x, y) in elements:
                row += symbols[elements[(x, y)]]
            else:
                row += "."
        row += " |"
        print(row)
    print("  " + "-" * (size * 2 + 3))

load_and_print()
input("Press enter to continue...")