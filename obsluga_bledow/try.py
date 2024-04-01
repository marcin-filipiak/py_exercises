```
W języku Python obsługa błędów odbywa się za pomocą instrukcji try, except 
oraz opcjonalnie finally. Pozwala to na kontrolowanie sytuacji, 
w których mogą wystąpić wyjątki (błędy) i zapewnienie, 
że program może kontynuować działanie nawet w przypadku nieprzewidzianych problemów. 
```


#ogólna obsługa błędów
try:
    # Operacje, które mogą spowodować błędy
    x = 10 / 0
except Exception as e:
    # Ogólna obsługa błędów
    print("Wystąpił błąd:", e)



#konkretna obsługa błędów
try:
    # Tutaj umieszczamy kod, który może spowodować błąd
    x = 10 / 0
except ZeroDivisionError:
    # Obsługa konkretnego rodzaju błędu (ZeroDivisionError)
    print("Dzielenie przez zero jest niedozwolone.")
except:
    # Obsługa ogólnego błędu (jeśli nie pasuje do żadnego innego except)
    print("Wystąpił nieoczekiwany błąd.")
else:
    # Opcjonalny blok else, który jest wykonywany, jeśli żaden wyjątek nie został zgłoszony w bloku try
    print("Działanie wykonane poprawnie.")
finally:
    # Opcjonalny blok finally, który jest zawsze wykonywany niezależnie od tego, czy wystąpił wyjątek
    print("Zawsze wykonaj to, bez względu na to, czy wystąpił wyjątek czy nie.")

