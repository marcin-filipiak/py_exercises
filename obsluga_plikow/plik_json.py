import json

# Otwarcie pliku JSON do odczytu
with open("dane.json", "r") as plik_json:
    dane = json.load(plik_json)
    print(dane)

