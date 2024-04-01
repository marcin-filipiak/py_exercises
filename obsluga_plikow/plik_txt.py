

# Otwarcie pliku do zapisu
with open("wyniki.txt", "w") as plik:
    # Zapisywanie danych do pliku
    plik.write("To jest przykładowa linia tekstu.\n")
    plik.write("Kolejna linia tekstu.\n")


# Otwarcie pliku do odczytu
with open("plik.txt", "r") as plik:
    # Odczytanie zawartości pliku wiersz po wierszu
    for linia in plik:
        print(linia.strip())  # .strip() usuwa białe znaki z końca i początku linii



