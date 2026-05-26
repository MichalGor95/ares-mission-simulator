import random

def dust_storm(rover, world_size=50):

    dx = random.choice([-2, -1, 0, 1, 2])
    dy = random.choice([-2, -1, 0, 1, 2])
    rover.x = max(-world_size, min(world_size, rover.x))
    rover.y = max(-world_size, min(world_size, rover.y))
    rover.energy -= 10
    rover.energy = max(0, rover.energy)
    msg = f"Burza pyłowa! Łazik przesunięty o ({dx:+},{dy:+}), utrata 10 energii."
    rover.log(msg)
    return msg

def rockslide(rover):

    dmg = random.randint(10, 25)
    rover.take_damage(dmg)
    msg = f"Osunięcie skał! Utrata {dmg} osłony."
    rover.log(msg)
    return msg

def signal_boost(rover):

    bonus = random.randint(10, 20)
    rover.recharge(bonus)
    msg = f"Odebrano sygnał pomocniczy! +{bonus} energii."
    rover.log(msg)
    return msg


def meteor_impact(rover):
    dmg_energy = random.randint(5, 15)
    dmg_shield = random.randint(5, 15)
    rover.energy -= dmg_energy
    rover.energy = max(0, rover.energy)
    rover.take_damage(dmg_shield)
    msg = f"Uderzenie meteorytu! Utrata {dmg_energy} energii i {dmg_shield} osłony."
    rover.log(msg)
    return msg

def magnetic_anomaly(rover):
    # losowo obraca łazika
    rover.angle = random.randint(0, 359)
    rover.energy -= 5
    rover.energy = max(0, rover.energy)
    msg = f"Anomalia magnetyczna! Kompas oszalał, nowy kąt: {rover.angle}°, utrata 5 energii."
    rover.log(msg)
    return msg

def nothing(rover):
    return None

EVENTS = (
    [nothing] * 10 +
    [dust_storm] * 3 +
    [rockslide] * 3 +
    [signal_boost] * 1 +
    [meteor_impact] * 2 +
    [magnetic_anomaly] * 2
)

def random_event(rover, world_size=50):
    func = random.choice(EVENTS)
    if func == dust_storm:
        return func(rover, world_size)
    return func(rover)