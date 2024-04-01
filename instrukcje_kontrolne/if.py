# Przykładowe zmienne
x = 5
y = 10
z = 15

# Instrukcja if prosta
if x < y:
    print("x jest mniejsze od y")

# Instrukcja if else
if y < z:
    print("y jest mniejsze od z")
else:
    print("y nie jest mniejsze od z")

# Instrukcja if sprawdzająca kilka zmiennych
if x < y and x < z:
    print("x jest najmniejsze")
elif y < x and y < z:
    print("y jest najmniejsze")
elif z < x and z < y:
    print("z jest najmniejsze")
else:
    print("Co najmniej dwie zmienne mają taką samą wartość")
