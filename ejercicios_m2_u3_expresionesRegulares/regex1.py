import re

patron = re.compile("[p+]")
lista = ["pera", "vfg"]

print(patron.match(lista[0]))
print(patron.match(lista[1]))
