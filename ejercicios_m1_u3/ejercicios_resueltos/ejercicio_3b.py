frase = input("ingrese una frase: ")
vocales = ["a", "á", "e", "i", "o", "u", "é", "í", "ó", "ú"]
for vocal in vocales:
    contador = 0
    for caracter in frase:
        if caracter == vocal:
            contador += 1
    print("la vocal " + vocal + " se repite " + str(contador) + " vez/veces")
