import csv

# Otwarcie pliku CSV do odczytu
with open("dane.csv", "r") as plik_csv:
    czytnik = csv.reader(plik_csv)
    for wiersz in czytnik:
        print(wiersz)

