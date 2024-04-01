```
Krotki są niezmienialnymi strukturami danych w Pythonie, 
co oznacza, że ich zawartość nie może być zmieniana po ich utworzeniu.
```

# Tworzenie krotki (tuple)
krotka = (1, 2, 3, 4, 5)

# Dostęp do elementu w krotce
print(krotka[2])  # Wypisze 3

# Krotki są niezmienne, próba zmiany elementu spowoduje błąd
# krotka[2] = 6  # TypeError: 'tuple' object does not support item assignment

# Iterowanie po krotce
for element in krotka:
    print(element)

