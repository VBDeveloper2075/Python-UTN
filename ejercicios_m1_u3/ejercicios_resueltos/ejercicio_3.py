"""
Ejercicio 3
Escriba un programa que consulte al usuario por una oración
y comente al usuario cuantas veces aparecen todas las vocales
considerando minúsculas, mayúsculas y acentos.  

"""

frase = input("Introduce una frase: ")

# Para minusculas y mayusculas
vocales = ['a', 'e', 'i', 'o', 'u' ]
for vocal in vocales: 
    contador = 0
    for caracter in frase: 
        if caracter == vocal or caracter == vocal.upper():
            contador += 1
    print("La vocal: " + vocal + " se repite " + str(contador) + " veces")

print("---------------------------------------------")
# Para minusculas, mayusculas y acentos
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú' ]
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
for vocal in vocales: 
    
    for caracter in frase:
        if vocal == 'a' or vocal == 'á':
            if caracter == vocal or caracter == vocal.upper():
                contador_a += 1
        if vocal == 'e' or vocal == 'é':
            if caracter == vocal or caracter == vocal.upper():
                contador_e += 1
        if vocal == 'i' or vocal == 'í':
            if caracter == vocal or caracter == vocal.upper():
                contador_i += 1
        if vocal == 'o' or vocal == 'ó':
            if caracter == vocal or caracter == vocal.upper():
                contador_o += 1
        if vocal == 'u' or vocal == 'ú':
            if caracter == vocal or caracter == vocal.upper():
                contador_u += 1
                
print("La vocal: a se repite " + str(contador_a) + " veces")
print("La vocal: e se repite " + str(contador_e) + " veces")
print("La vocal: i se repite " + str(contador_i) + " veces")
print("La vocal: o se repite " + str(contador_o) + " veces")
print("La vocal: u se repite " + str(contador_u) + " veces")
