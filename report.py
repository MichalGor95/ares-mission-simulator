RED    = "\033[31m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"
PINK   = "\033[95m"
RESET  = "\033[0m"

CFM  = f"{ORANGE}[CFM]{RESET} "
CONF = f"{GREEN}[CNF]{RESET} "
WARN = f"{YELLOW}[WRN]{RESET} "


def show_report(rover, world, reason):
    wynik = "SUKCES" if reason == "CEL OSIĄGNIĘTY" else "PORAŻKA"
    kolor_wyniku = GREEN if wynik == "SUKCES" else RED

    print()
    print(f"{RED}╔══════════════════════════════════════════════════════╗{RESET}")
    print(f"{RED}║{RESET}         {ORANGE}RAPORT KOŃCOWY MISJI ARES{RESET}                {RED}║{RESET}")
    print(f"{RED}╠══════════════════════════════════════════════════════╣{RESET}")
    print(f"{RED}║{RESET}  {CFM}Łazik:             {BLUE}{rover.name}{RESET}")
    print(f"{RED}╠══════════════════════════════════════════════════════╣{RESET}")
    print(f"{RED}║{RESET}  {ORANGE}PARAMETRY STARTOWE:{RESET}")
    print(f"{RED}║{RESET}  {CFM}Pozycja startowa:  {BLUE}({rover.start_x}, {rover.start_y}){RESET}")
    print(f"{RED}║{RESET}  {CFM}Energia startowa:  {BLUE}{rover.start_energy}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Osłona startowa:   {BLUE}{rover.start_shield}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Rozmiar świata:    {BLUE}{world.size}{RESET}")
    print(f"{RED}╠══════════════════════════════════════════════════════╣{RESET}")
    print(f"{RED}║{RESET}  {ORANGE}WYNIKI MISJI:{RESET}")
    print(f"{RED}║{RESET}  {CFM}Pozycja końcowa:   {BLUE}({rover.x}, {rover.y}){RESET}")
    print(f"{RED}║{RESET}  {CFM}Energia końcowa:   {BLUE}{rover.energy}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Osłona końcowa:    {BLUE}{rover.shield}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Liczba kroków:     {BLUE}{rover.steps}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Dystans od celu:   {BLUE}{rover.distance_to_goal():.2f}{RESET}")
    print(f"{RED}║{RESET}  {CFM}Przyczyna końca:   {YELLOW}{reason}{RESET}")
    print(f"{RED}╠══════════════════════════════════════════════════════╣{RESET}")
    print(f"{RED}║{RESET}  {ORANGE}HISTORIA ZDARZEŃ:{RESET}")

    if rover.history:
        for wpis in rover.history:
            print(f"{RED}║{RESET}   {YELLOW}• {wpis}{RESET}")
    else:
        print(f"{RED}║{RESET}   {BLUE}Brak zdarzeń.{RESET}")

    print(f"{RED}╠══════════════════════════════════════════════════════╣{RESET}")
    print(f"{RED}║{RESET}  {CFM}WYNIK MISJI:  {kolor_wyniku}{wynik}{RESET}")
    print(f"{RED}╚══════════════════════════════════════════════════════╝{RESET}")
    print()