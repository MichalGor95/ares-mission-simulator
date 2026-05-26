import os
import time
import sys
from rover import Rover
from world import World, STATION, RADIATION, GOAL
from events import random_event
import report
try:
    import visualizer
    TURTLE_OK = True
except ImportError:
    TURTLE_OK = False

# Stałe kolorów
RED    = "\033[31m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"
PINK   = "\033[95m"
RESET  = "\033[0m"

ASK  = f"{BLUE}[ASK]{RESET} "
CONF = f"{GREEN}[CNF]{RESET} "
WARN = f"{YELLOW}[WRN]{RESET} "
ERR  = f"{RED}[ERR]{RESET} "
CFM  = f"{ORANGE}[CFM]{RESET} "


def typewrite(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def blink_cursor(text, times=3):
    for _ in range(times):
        sys.stdout.write(f"\r{text} █\033[K")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{text}  \033[K")
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write(f"\r{text}\033[K\n")
    sys.stdout.flush()


def blink_then_input(prompt, times=3):
    blink_cursor(prompt, times)
    return input(f"{prompt} ")


def clear_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print("\033[2J\033[H", end="")


def splash_screen():
    clear_terminal()

    logo = f"""{RED}

 █████╗ ██████╗ ███████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝ ██╔════╝
███████║██████╔╝█████╗   ███████╗
██╔══██║██╔══██╗██╔══╝   ╚════██║
██║  ██║██║  ██║███████╗ ███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚══════╝

███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
████╗ ████║██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
██╔████╔██║██║███████╗███████╗██║██║   ██║██╔██╗ ██║
██║╚██╔╝██║██║╚════██║╚════██║██║██║   ██║██║╚██╗██║
██║ ╚═╝ ██║██║███████║███████║██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝

{ORANGE}        Autonomous Mars Rover Terminal
{BLUE}              Expedition Control v1.0

{RESET}
"""
    border  = f"{RED}╔═══════════════════════════════════════════════╗{RESET}"
    title1  = f"{RED}║{RESET}           {BLUE}ARES MISSION CONTROL v1.0{RESET}           {RED}║{RESET}"
    title2  = f"{RED}║{RESET}        {ORANGE}Symulator Ekspedycji Łazika{RESET}            {RED}║{RESET}"
    border2 = f"{RED}╚═══════════════════════════════════════════════╝{RESET}"

    print(border)
    print(title1)
    print(title2)
    print(border2)
    print()
    time.sleep(0.3)

    for line in logo.splitlines():
        print(line)
        time.sleep(0.05)

    print()

    loading_lines = [
        f"{GREEN}[ OK ]{RESET} Initializing onboard systems...",
        f"{GREEN}[ OK ]{RESET} Loading terrain database...",
        f"{GREEN}[ OK ]{RESET} Calibrating navigation module...",
        f"{GREEN}[ OK ]{RESET} Synchronizing satellite uplink...",
        f"{GREEN}[ OK ]{RESET} Establishing rover connection...",
        f"{GREEN}[ OK ]{RESET} Power systems nominal.",
        f"{YELLOW}[INFO]{RESET} Dust storm probability: LOW",
        f"{GREEN}[ OK ]{RESET} Mission control ready.",
    ]

    for line in loading_lines:
        typewrite(line, 0.02)
        time.sleep(0.35)

    print()
    typewrite(f"{ORANGE}> Press ANYTHING to start mission...{RESET}", 0.02)
    input()


def input_data():
    while True:
        name_rover = str(input(f"{ASK}Nazwa łazika:\t"))
        if not name_rover.strip():
            name_rover = "ARES-1"

        while True:
            try:
                world_size = int(input(f"{ASK}Rozmiar świata (10-500):\t"))
                if 10 <= world_size <= 500:
                    break
                print(f"{WARN}Rozmiar świata powinien wynosić 10-500")
            except ValueError:
                print(f"{ERR}Podaj liczbę całkowitą!")

        while True:
            try:
                x_position = int(input(f"{ASK}Podaj koordynat x ({-world_size} do {world_size}):\t"))
                if -world_size <= x_position <= world_size:
                    break
                print(f"{WARN}Koordynat x musi być między {-world_size} a {world_size}")
            except ValueError:
                print(f"{ERR}Podaj liczbę całkowitą!")

        while True:
            try:
                y_position = int(input(f"{ASK}Podaj koordynat y ({-world_size} do {world_size}):\t"))
                if -world_size <= y_position <= world_size:
                    break
                print(f"{WARN}Koordynat y musi być między {-world_size} a {world_size}")
            except ValueError:
                print(f"{ERR}Podaj liczbę całkowitą!")

        while True:
            try:
                starting_angle = int(input(f"{ASK}Podaj kąt startowy (0-359):\t"))
                if 0 <= starting_angle <= 359:
                    break
                print(f"{WARN}Kąt startowy musi być liczbą 0-359")
            except ValueError:
                print(f"{ERR}Podaj liczbę całkowitą!")

        while True:
            try:
                starting_enrgy = int(input(f"{ASK}Podaj poziom energii startowej (10-100):\t"))
                if 10 <= starting_enrgy <= 100:
                    break
                print(f"{WARN}Energia startowa musi być liczbą 10-100")
            except ValueError:
                print(f"{ERR}Podaj liczbę całkowitą!")

        while True:
            print(f"{GREEN}Poziomy trudności:\n 1. Łatwy\n 2. Normalny\n 3. Trudny{RESET}")
            try:
                difficulty_level_input = input(f"{ASK}Wybierz poziom trudności:\t")
                if difficulty_level_input.lower() in ["1", "2", "3", "łatwy", "latwy", "normalny", "trudny", "easy", "medium", "hard"]:
                    if difficulty_level_input.lower() in ["1", "latwy", "łatwy", "easy"]:
                        difficulty_level = 1
                    elif difficulty_level_input.lower() in ["2", "normalny", "medium"]:
                        difficulty_level = 2
                    else:
                        difficulty_level = 3
                    break
                print(f"{WARN}Należy wpisać liczbę 1-3 lub nazwę poziomu")
            except ValueError:
                print(f"{ERR}Coś poszło nie tak, spróbuj ponownie")

        difficulty_names = {1: "Łatwy", 2: "Normalny", 3: "Trudny"}
        clear_terminal()
        print(f"{RED}╔════════════════════════════════════════════════╗{RESET}")
        print(f"{RED}║{RESET}          {ORANGE}POTWIERDŹ INFORMACJE{RESET}                  {RED}║{RESET}")
        print(f"{RED}╠════════════════════════════════════════════════╣{RESET}")

        lines = [
            f"{RED}║{RESET} {CFM}Nazwa łazika:      {BLUE}{name_rover}{RESET}",
            f"{RED}║{RESET} {CFM}Rozmiar świata:    {BLUE}{world_size}{RESET}",
            f"{RED}║{RESET} {CFM}Koordynat x:       {BLUE}{x_position}{RESET}",
            f"{RED}║{RESET} {CFM}Koordynat y:       {BLUE}{y_position}{RESET}",
            f"{RED}║{RESET} {CFM}Kąt startowy:      {BLUE}{starting_angle}°{RESET}",
            f"{RED}║{RESET} {CFM}Energia startowa:  {BLUE}{starting_enrgy}{RESET}",
            f"{RED}║{RESET} {CFM}Poziom trudności:  {BLUE}{difficulty_names[difficulty_level]}{RESET}",
        ]

        for line in lines:
            typewrite(line)

        print(f"{RED}╚════════════════════════════════════════════════╝{RESET}")
        typewrite(f"{ASK}Czy informacje są poprawne i możemy zaczynać?")
        potwierdzenie = input(f"{ASK}Wpisz y lub n:\t").strip().lower()
        if potwierdzenie == "y":
            typewrite(f"{CONF}Zaczynamy!")
            break
        if potwierdzenie == "n":
            clear_terminal()

    return name_rover, world_size, x_position, y_position, starting_angle, starting_enrgy, difficulty_level


def get_direction():
    valid = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]
    print(f"""{WARN}Możliwe kierunki:
  1.N   2.S   3.E   4.W
  5.NE  6.NW  7.SE  8.SW{RESET}""")
    while True:
        direction = input(f"{ASK}Kierunek: ").upper().strip()
        if direction.isdigit():
            idx = int(direction)
            if 1 <= idx <= 8:
                return valid[idx - 1]
        elif direction in valid:
            return direction
        print(f"{ERR}Podane dane są niepoprawne!")


def handle_element(rover, element):
    if element == STATION:
        rover.recharge(25)
        return "STATION"
    elif element == RADIATION:
        rover.take_damage(15)
        return "RADIATION"
    elif element == GOAL:
        return "GOAL"
    else:
        return None


def show_step_log(krok, direction, x_przed, y_przed, x_po, y_po,
                  energy_przed, energy_po, shield_przed, shield_po,
                  element_msg, event_msg, dystans):
    print(f"{RED}╔══════════════════════════════════════════════════╗{RESET}")
    print(f"{RED}║{RESET}  {ORANGE}KROK: {krok:<5}{RESET}                                    {RED}║{RESET}")
    print(f"{RED}╠══════════════════════════════════════════════════╣{RESET}")
    print(f"{RED}║{RESET}  {CFM}Kierunek:        {BLUE}{direction:<6}{RESET}                       {RED}║{RESET}")
    print(f"{RED}║{RESET}  {CFM}Pozycja:         {BLUE}({x_przed},{y_przed}) → ({x_po},{y_po}){RESET}")
    print(f"{RED}║{RESET}  {CFM}Energia:         {BLUE}{energy_przed} → {energy_po}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Osłona:          {BLUE}{shield_przed} → {shield_po}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Dystans do celu: {BLUE}{dystans:.2f}{RESET}")
    if element_msg is not None:
        label = {
            "STATION":   f"{GREEN}[STACJA] Doładowano +25 energii{RESET}",
            "RADIATION": f"{YELLOW}[RADIACJA] Utrata 15 osłony{RESET}",
            "GOAL":      f"{PINK}[ANOMALIA] Cel osiągnięty!{RESET}",
        }.get(element_msg, f"{BLUE}{element_msg}{RESET}")
        print(f"{RED}║{RESET}  {CFM}Element:         {label}")
    if event_msg is not None:
        print(f"{RED}║{RESET}  {CFM}Zdarzenie:       {YELLOW}{event_msg}{RESET}")
    print(f"{RED}╚══════════════════════════════════════════════════╝{RESET}")


def game_loop(rover, world, positions):
    MAX_STEPS = 200
    reason = None

    while True:
        # zapamiętaj stan przed krokiem
        x_przed      = rover.x
        y_przed      = rover.y
        energy_przed = rover.energy
        shield_przed = rover.shield

        clear_terminal()

        # pokaż aktualny stan przed pobraniem kierunku
        print(f"{RED}╔══════════════════════════════════════════════════╗{RESET}")
        print(f"{RED}║{RESET}  {ORANGE}KROK: {rover.steps + 1:<5}{RESET}  {BLUE}Łazik: {rover.name}{RESET}")
        print(f"{RED}║{RESET}  {CFM}Pozycja: ({rover.x}, {rover.y})  "
              f"Energia: {rover.energy}  Osłona: {rover.shield}  "
              f"Dystans: {rover.distance_to_goal():.2f}{RESET}")
        print(f"{RED}╚══════════════════════════════════════════════════╝{RESET}")

        direction = get_direction()

        # oblicz następną pozycję
        deltas = {
            "N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0),
            "NE": (1, 1), "NW": (-1, 1), "SE": (1, -1), "SW": (-1, -1),
        }
        dx, dy = deltas[direction]
        next_x = rover.x + dx
        next_y = rover.y + dy

        # sprawdź granice
        if not world.in_bounds(next_x, next_y):
            print(f"{WARN}Wyjście poza granice świata! Wybierz inny kierunek.{RESET}")
            input("Naciśnij Enter aby kontynuować...")
            continue

        # sprawdź krater
        if world.is_blocked(next_x, next_y):
            print(f"{ERR}Na tej drodze jest krater! Wybierz inny kierunek.{RESET}")
            input("Naciśnij Enter aby kontynuować...")
            continue

        # ruch
        rover.move(direction)
        positions.append((rover.x, rover.y))

        # element świata
        element = world.get_element(rover.x, rover.y)
        element_msg = handle_element(rover, element)

        # zdarzenie losowe
        event_msg = random_event(rover, world.size)

        # pokaż log kroku
        clear_terminal()
        show_step_log(
            rover.steps, direction,
            x_przed, y_przed, rover.x, rover.y,
            energy_przed, rover.energy,
            shield_przed, rover.shield,
            element_msg, event_msg,
            rover.distance_to_goal()
        )

        # warunki końca
        if element_msg == "GOAL":
            reason = "CEL OSIĄGNIĘTY"
            break
        if rover.energy <= 0:
            reason = "BRAK ENERGII"
            break
        if rover.shield <= 0:
            reason = "ŁAZIK ZNISZCZONY"
            break
        if rover.steps >= MAX_STEPS:
            reason = "LIMIT KROKÓW"
            break

        input(f"\n{ASK}Naciśnij Enter aby przejść do następnego kroku...")

    if reason is None:
        reason = "NIEZNANA PRZYCZYNA"
    return reason


def main():
    splash_screen()
    while True:
        dane = input_data()
        name, size, x, y, angle, energy, difficulty = dane

        rover = Rover(name, x, y, angle, energy, 100)
        world = World(size, difficulty)
        world.save_to_json()

        positions = [(rover.x, rover.y)]

        reason = game_loop(rover, world, positions)

        report.show_report(rover, world, reason)
        if TURTLE_OK:
            visualizer.draw(positions, size)

        print()
        typewrite(f"{ASK}Czy chcesz zagrać ponownie?")
        again = input(f"{ASK}Wpisz y lub n:\t").strip().lower()
        if again != "y":
            typewrite(f"{CONF}Dziękujemy za udział w misji ARES. Do zobaczenia!")
            break
        clear_terminal()


main()