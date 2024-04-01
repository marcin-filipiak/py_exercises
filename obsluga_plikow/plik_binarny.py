# Otwarcie pliku binarnego do odczytu
with open("plik.bin", "rb") as plik_binarny:
    # Odczytanie danych z pliku binarnego
    dane = plik_binarny.read()
    print(dane)

