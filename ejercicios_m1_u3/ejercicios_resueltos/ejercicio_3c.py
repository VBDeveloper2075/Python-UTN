"""
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.  
"""


def repetidos(elemento, lista):
    veces = 0

    for i in lista:
        if elemento == i:
            veces += 1

    return veces

oracion = input("Ingrese una oracion: ")

vocales = ["a" , "e", "i", "o", "u", "A", "E", "I", "O", "U", "á","é","í","ó", "ú", "Á", "É", "Í", "Ó", "Ú"]

for vocal in vocales:
    print(vocal+ " ==> " + str(repetidos( vocal, oracion)))
