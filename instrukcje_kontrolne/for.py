

#od 1 do 5
for i in range(1, 6):
    print(i)


#iteracja przez listę napisów
napisy = ["jabłko", "banan", "gruszka", "śliwka", "pomarańcza"]
for napis in napisy:
    print(napis)


#iteracja przez listę liczb i zrobienie ich sumy
liczby = [1, 2, 3, 4, 5]
suma = 0
for liczba in liczby:
    suma += liczba
print("Suma liczb w liście to:", suma)


#iteracja przez słownik
samochody = {"Marka": "Toyota", "Model": "Corolla", "Rok produkcji": 2022, "Kolor": "Czarny"}
for klucz, wartosc in samochody.items():
    print(klucz + ":", wartosc)


