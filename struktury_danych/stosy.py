```
Stosy są strukturami danych, w której ostatni dodany 
element jest pierwszym usuwanym (zasada LIFO - Last In, First Out).
```

# Tworzenie stosu
stos = []

# Dodawanie elementów do stosu
stos.append(1)
stos.append(2)
stos.append(3)

# Usuwanie elementów ze stosu
while len(stos) > 0:
    print(stos.pop())

