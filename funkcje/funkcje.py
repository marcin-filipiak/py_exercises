```
Funkcje w języku Python są blokami kodu, które mogą być wielokrotnie 
wywoływane w różnych miejscach programu. 
Funkcje służą do grupowania określonych zadań w jednostki, 
co pomaga w organizacji kodu, zwiększa czytelność i ułatwia ponowne użycie kodu. 
```

def nazwa_funkcji(parametr1, parametr2):
    # blok kodu funkcji
    # możemy wykonywać różne operacje na parametrach
    wynik = parametr1 + parametr2
    return wynik


#funkcja rekurencyjna - wywołująca samą siebie
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)



wynik_funkcji = nazwa_funkcji(2, 3)
print(wynik_funkcji)  # Wypisze 5

