"""Ejercicio 1
Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y
agréguele un bucle al código de forma de simplificarlo. 

"""
import sys

valor1 = sys.argv[1]
valor2 = sys.argv[2]
valor3 = sys.argv[3]

lista = sys.argv[1:]

for x in lista:
    if int(x) % 2 == 0:
        print(valor1, "es par")
    else:
        print(valor1, "es impar")

 
