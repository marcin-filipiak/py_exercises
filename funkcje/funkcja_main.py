```
W języku Python nie ma specjalnej funkcji o nazwie "main" tak jak w niektórych 
innych językach programowania, np. w języku C/C++. 
Jednakże, w Pythonie często stosuje się konwencję, 
że główna część programu znajduje się w bloku kodu pod warunkiem, 
że plik ten jest uruchamiany bezpośrednio (a nie importowany jako moduł do innego pliku). 
Ten blok kodu często zawiera wywołanie innych funkcji lub instrukcje sterujące przepływem programu.
```

def main():
    # Tutaj znajduje się główna część programu
    print("To jest główna część programu")

# Wywołanie funkcji main tylko wtedy, gdy plik jest uruchamiany bezpośrednio
if __name__ == "__main__":
    main()

