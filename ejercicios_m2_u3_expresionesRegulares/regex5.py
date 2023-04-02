import re

patron = re.compile(r"color (?=rojo)")
string1 = "El auto de color rojo."
print(patron.search(string1))
