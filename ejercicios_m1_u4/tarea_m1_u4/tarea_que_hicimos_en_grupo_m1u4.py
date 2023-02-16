# EJERCICIO 1

"""
Cree una función lambda que compruebe si un número es par o impar. 
"""

print("EJERCICIO 1")


# EJERCICIO 2


"""
Cree una función lamba que compruebe si un número es par o impar. 

def multiplicar_por_tres(valor): 
res=3*valor
return res

"""
print("EJERCICIO 2")


# EJERCICIO 3

"""
Crear una función lambda que sea equivalente a la siguiente función: 

def sumar(valor1, valor2): 
res=valor1 + valor2
return res
"""
print("EJERCICIO 3")


# EJERCICIO 4

"""
def sumar(valor1, valor2): 

"""

print("EJERCICIO 4")


# EJERCICIO 5

""" 
EJERCICIO 5

 Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo.  

1, 2, 3, 4, 5 

Y  

5, 4, 3, 2, 1 
"""
print("EJERCICIO 5")


def crecer(edad):
    i = 1
    edadnumero = int(edad)
    k = edad
    for i in range(i, edadnumero + 1):
        if i == edadnumero:
            print(str(i))
        else:
            print(str(i), end=", ")


def decrecer(edad):
    i = 1
    edadnumero = int(edad)
    k = edad

    for i in range(i, edadnumero + 1):
        if i == edadnumero:
            print(str(k))
        else:
            print(str(k), end=", ")
            k -= 1


crecer(25)
print("Y")
decrecer(25)

"""
EJERCICIO 6

 Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes: 

[3, 44, 21, 78, 5, 56, 9] 

"""
print("EJERCICIO 6")


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
print("EJERCICIO 6 - RESUELTO POR NORA")


def ordenar_lista(mi_lista):
    mi_lista.sort()
    print(mi_lista)


ordenar_lista([3, 44, 21, 78, 5, 56, 9])

"""
EJERCICIO 7

 isinstance(x, list) permite consultar si el elementos x es del tipo lista. 

A partir de la siguiente función recursiva que permite recorrer los niveles de una lista: 


"""
print("EJERCICIO 7")
