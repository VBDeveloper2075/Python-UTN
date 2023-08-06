import re

 
patron = re.compile("^[0-9]*$")
lista = ["44565", "3v22fg"]

print(patron.match(lista[0]))
print(patron.match(lista[1]))