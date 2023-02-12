def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n - 1):  # <-- bucle padre
        for j in range(n - 1 - i):  # <-- bucle hijo
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


elementos = [3, 44, 21, 78, 5, 56, 9]
ord_burbuja(elementos)

print(elementos)