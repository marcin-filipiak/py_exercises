#######################################################
#zmodyfikuj program, by dodawał nowe słowa do słownika#
#######################################################

# Definicja pustego słownika
slownik = {}

# Funkcja do wczytywania słów z pliku
def wczytaj_slowa_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            polskie, angielskie = linia.strip().split(',')
            slownik[polskie] = angielskie

# Funkcja do tłumaczenia słowa polskiego na angielskie
def tlumacz_slowo(polskie):
    return slownik.get(polskie, "Nie znaleziono tłumaczenia")

# Wczytanie słów z pliku
wczytaj_slowa_z_pliku("slowa.txt")

# Pytanie użytkownika o słowo polskie
polskie_slowo = input("Podaj słowo polskie: ")

# Wyszukanie i wyświetlenie angielskiego odpowiednika
angielskie_slowo = tlumacz_slowo(polskie_slowo)
print(f"Angielski odpowiednik słowa '{polskie_slowo}' to: {angielskie_slowo}")
