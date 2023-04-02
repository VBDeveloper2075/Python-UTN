import re

patron = re.compile("pera" "|manzana")
string = "manzana"

print(patron.match(string))
