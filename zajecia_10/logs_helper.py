"""
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
"""

def add_log(level, message):
    with open("logs.txt", mode="a") as file:
        file.write(f"{level} {message} \n")

def read_logs(level=None):
    with open("logs.txt") as file:
        if not level:
            return file.readlines()
        logs = []
        for line in file:
            if line.startswith(level):
                logs.append(line)
        return logs
