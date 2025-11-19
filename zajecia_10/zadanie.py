"""
# Zadanie: Prosty system logowania (moduły + pliki + `with open`)

W tym zadaniu stworzymy prosty system logów: plik, do którego dopiszemy informacje o działaniu programu, oraz funkcję, która pozwoli je odczytać.

Struktura plików:
- `main.py`
- `logs_helper.py`
- `logs.txt` (powstanie automatycznie)

## Krok 1: Plik `logs_helper.py`

W tym pliku napisz dwie funkcje:

### 1) add_log
Funkcja ma:
- dopisać jedną linijkę w formacie:
  `LEVEL MESSAGE`

Przykład użycia:

add_log("INFO", "Program się uruchomił")
add_log("ERROR", "Błąd połączenia")


### 2) read_logs
Funkcja ma:

- jeśli `level` jest `None`, zwrócić wszystkie linie,
- jeśli `level` ma wartość (np. `"ERROR"`), zwrócić tylko te linie, które zaczynają się od `"ERROR "`.

Przykład użycia:

read_logs() # wszystkie logi
read_logs(level="ERROR") # tylko błędy
read_logs(level="INFO") # tylko informacje


Funkcja ma zwracać listę stringów.

## Krok 2: Plik `main.py`

1. Zaimportuj funkcje:
2. Dodaj kilka logów:
3. Wyświetl wszystkie logi:
4. Wyświetl tylko błędy:


Po wykonaniu zadania powinieneś mieć:
- moduł `logs_helper.py`,
- plik `logs.txt`,
- program `main.py`, który wyświetla i filtruje logi.
"""