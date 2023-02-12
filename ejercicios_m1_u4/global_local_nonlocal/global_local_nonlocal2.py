a = 5
b = 6


def nopisa():
    a = 10
    print(a, b)


# ahora le pido que imprima la función, se ve que toma a valor 10
# luego le pido que imprima a, como está fuera de la función => vale 5

nopisa()
print(a)
