import re

patron = re.compile(r"color (?!rojo)")
string1 = "El auto de color azul."
print(patron.search(string1))
