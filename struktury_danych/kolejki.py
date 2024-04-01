```
Kolejki są strukturami danych, w których elementy są dodawane na jednym końcu 
(zwany "tyłem") i usuwane z drugiego końca (zwany "przodem"). 
W Pythonie, moduł queue dostarcza implementacje kolejki.
```

from queue import Queue

# Tworzenie kolejki
kolejka = Queue()

# Dodawanie elementów do kolejki
kolejka.put(1)
kolejka.put(2)
kolejka.put(3)

# Usuwanie elementów z kolejki
while not kolejka.empty():
    print(kolejka.get())

