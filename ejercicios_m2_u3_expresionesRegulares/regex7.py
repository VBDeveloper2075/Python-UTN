import re

patron = re.compile(r"(?<=color )azul")
string1 = "El auto de color azul."

print(patron.search(string1))

m = re.search(r"(?<=color )azul", "El auto de color azul.")
print(m.group(0))
