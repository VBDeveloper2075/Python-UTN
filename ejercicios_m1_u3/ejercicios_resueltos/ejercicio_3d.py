"""
Escriba un programa que consulte al usuario por una oración
y comente al usuario cuantas veces aparecen todas las vocales
considerando minúsculas, mayúsculas y acentos.
"""

oracion = input("Ingrese una oración: ")
print(oracion)
print("---" * 10)

letras = ("a", "á", "A", "e", "é", "E", "i", "í", "I", "o", "ó", "O", "u", "ú", "U")

for x in letras:
    print("La letra ", x, " aparece ", oracion.count(x), " veces")
# print("La letra 'a' aparece ", oracion.count("a"), " veces")
