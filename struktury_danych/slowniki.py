```
Słowniki w Pythonie są strukturami danych, które przechowują pary klucz-wartość. 
Klucze muszą być unikalne i niezmienne, wartości mogą być dowolnego typu.
```
# Tworzenie słownika
slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2', 'klucz3': 'wartosc3'}

# Dodawanie nowej pary klucz-wartość
slownik['klucz4'] = 'wartosc4'

# Dostęp do wartości poprzez klucz
print(slownik['klucz2'])  # Wypisze 'wartosc2'

# Iterowanie po kluczach w słowniku
for klucz in slownik:
    print(klucz, ':', slownik[klucz])

