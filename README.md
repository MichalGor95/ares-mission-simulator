# ARES Mission Simulator

Symulator misji łazika marsjańskiego po dwuwymiarowym świecie. Projekt na Gigathon 2026 – Python (16–18 lat), III etap.

## Uruchomienie

```
python main.py
```

Wymagany Python 3.11. Żadnych dodatkowych bibliotek — tylko moduły ze standardowej biblioteki (`math`, `random`, `json`, `os`, `time`, `sys`, `turtle`).

## Pliki

| Plik | Opis |
|---|---|
| `main.py` | Punkt startowy. Pętla gry, intro, pobieranie danych, `game_loop` |
| `rover.py` | Klasa `Rover` — pozycja, energia, osłona, historia |
| `world.py` | Klasa `World` — generowanie mapy, elementy świata |
| `events.py` | Losowe zdarzenia (burza, meteoryty, itp.) |
| `report.py` | Raport końcowy misji |
| `visualizer.py` | Wizualizacja trasy w oknie turtle |
| `map_viewer.py` | Podgląd mapy ASCII (uruchamiany osobno) |
| `world.json` | Zapisana mapa z ostatniej sesji |

## Sterowanie

Po każdym kroku program pyta o kierunek ruchu:

```
1.N   2.S   3.E   4.W
5.NE  6.NW  7.SE  8.SW
```

Można wpisać numer (1–8) lub skrót kierunku (N, NE, SW itp.).

## Elementy świata

| Symbol | Nazwa | Efekt |
|---|---|---|
| STACJA | Stacja bazowa | +25 energii |
| KRATER | Krater | blokuje ruch |
| RADIACJA | Strefa radiacji | -15 osłony |
| ANOMALIA | Cel misji (0,0) | wygrana |

## Warunki zakończenia

- **CEL OSIĄGNIĘTY** – łazik dotarł do anomalii na (0,0)
- **BRAK ENERGII** – energia spadła do 0
- **ŁAZIK ZNISZCZONY** – osłona spadła do 0
- **LIMIT KROKÓW** – wykonano 200 kroków

## Podgląd mapy

```
python map_viewer.py
```

Wyświetla mapę ASCII wygenerowanego świata (wymaga wcześniejszego uruchomienia `main.py`).