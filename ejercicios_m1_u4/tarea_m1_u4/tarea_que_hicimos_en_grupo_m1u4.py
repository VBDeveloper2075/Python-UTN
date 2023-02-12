# EJERCICIO 1

# EJERCICIO 2

# EJERCICIO 3

# EJERCICIO 4

# EJERCICIO 5

# EJERCICIO 6


def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n - 1):  # <-- bucle padre
        for j in range(n - 1 - i):  # <-- bucle hijo
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


elementos = [3, 44, 21, 78, 5, 56, 9]
ord_burbuja(elementos)

print(elementos)

# -- otro ejemplo de ordenamiento usando "sort" --


def ordenar_lista(mi_lista):
    mi_lista.sort()
    print(mi_lista)


ordenar_lista([3, 44, 21, 78, 5, 56, 9])

# EJERCICIO 6
