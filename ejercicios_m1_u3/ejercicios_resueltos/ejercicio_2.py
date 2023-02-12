"""
Ejercicio 2
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. 
"""
frase = input("Introduce una frase: ")
vocales = ['a',  ]
for vocal in vocales: 
    contador = 0
    for caracter in frase: 
        if caracter == vocal:
            contador += 1
    print("La vocal: " + vocal + " se repite " + str(contador) + " veces")
