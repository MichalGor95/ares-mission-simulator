import math

class Rover:
    def __init__(self, name, x, y, angle, energy, shield):
        self.name = name
        self.x = x
        self.y = y
        self.angle = angle
        self.energy = energy
        self.shield = shield
        self.steps = 0
        self.history = []

        self.start_x = x
        self.start_y = y
        self.start_energy = energy
        self.start_shield = shield

    def move(self, direction):
        if self.energy <= 0:
            return False
        moves = {
            "N":  (0,  1),
            "S":  (0, -1),
            "E":  (1,  0),
            "W":  (-1, 0),
            "NE": (1,  1),
            "NW": (-1, 1),
            "SE": (1, -1),
            "SW": (-1,-1),
        }
        dx, dy = moves[direction]
        self.x += dx
        self.y += dy
        self.energy -= 3
        self.energy = max(0, self.energy)
        self.steps += 1
        angles = {"N":90,"S":270,"E":0,"W":180,"NE":45,"NW":135,"SE":315,"SW":225}
        self.angle = angles[direction]

    def take_damage(self, amount):
        self.shield -= amount
        self.shield = max(0, self.shield)

    def recharge(self, amount):
        self.energy += amount
        self.energy = min(100, self.energy)  # max 100

    def is_alive(self):
        return self.energy > 0 and self.shield > 0

    def log(self, event_text):

        self.history.append(f"Krok {self.steps}: {event_text}")

    # przyda się do liczenia dystansu do anomalii (0,0)
    def distance_to_goal(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)