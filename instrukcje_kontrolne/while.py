# Inicjalizacja zmiennej
licznik = 0

# Pętla while do chwili aż licznik mniejszy od 5
while licznik < 5:
    print("Wartość licznika:", licznik)
    odpowiedz = input("Czy chcesz kontynuować? (Tak/Nie): ")
    
    # Inkrementacja licznika
    licznik += 1
    
    # Sprawdzenie odpowiedzi
    if odpowiedz.lower() != 'tak':
        break

