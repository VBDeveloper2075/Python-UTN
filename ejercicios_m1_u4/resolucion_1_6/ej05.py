"""
Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo.
1, 2, 3, 4, 5
Y
5, 4, 3, 2, 1
"""

enum = lambda num: "".join(str(i) + "," for i in range(1, num + 1) if i < num) + str(num)
reversed_enum = lambda num: "".join(str(i) + "," for i in range(num, 1, -1) if i > 0) + str(1)

def pedir_edad():
    edad = int(input("Ingrese su edad: "))
    print(enum(edad))
    print(reversed_enum(edad))

pedir_edad()
