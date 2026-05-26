import random
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATION   = "STACJA"
CRATER    = "KRATER"
RADIATION = "RADIACJA"
GOAL      = "ANOMALIA"

class World:
    def __init__(self, size, difficulty):
        self.size = size
        self.goal = (0, 0)
        self.elements = {}
        self._generate(difficulty)

    def _generate(self, difficulty):
        counts = {
            1: {"craters": 5, "stations": 6, "radiation": 4},
            2: {"craters": 10, "stations": 4, "radiation": 7},
            3: {"craters": 15, "stations": 2, "radiation": 12},
        }
        cfg = counts.get(difficulty, counts[2])


        scale = max(1.0, self.size / 20)
        cfg = {k: int(v * scale) for k, v in cfg.items()}

        def rand_pos():
            x = random.randint(-self.size, self.size)
            y = random.randint(-self.size, self.size)
            return (x, y)

        for _ in range(cfg["craters"]):
            pos = rand_pos()
            if pos != (0, 0):
                self.elements[pos] = CRATER

        for _ in range(cfg["stations"]):
            pos = rand_pos()
            if pos not in self.elements and pos != (0, 0):
                self.elements[pos] = STATION

        for _ in range(cfg["radiation"]):
            pos = rand_pos()
            if pos not in self.elements and pos != (0, 0):
                self.elements[pos] = RADIATION

        self.elements[(0, 0)] = GOAL

    def get_element(self, x, y):
        return self.elements.get((x, y), None)

    def is_blocked(self, x, y):
        return self.elements.get((x, y)) == CRATER

    def in_bounds(self, x, y):
        return -self.size <= x <= self.size and -self.size <= y <= self.size

    def save_to_json(self, filename="world.json"):
        path = os.path.join(BASE_DIR, filename)
        data = {
            "size": self.size,
            "goal": list(self.goal),
            "elements": {f"{k[0]},{k[1]}": v for k, v in self.elements.items()}
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)