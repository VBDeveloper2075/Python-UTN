import re

patron = re.compile('(?i)pera|manzana')
string = "MANZANA"

print(patron.match(string))

input()