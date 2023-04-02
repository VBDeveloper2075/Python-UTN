import re
# #############################################
# Forma 1
# #############################################
patron = re.compile(r'(?i:pera) y manzana')
string1 = "pera y manzana"
string2 = "PERA y manzana"
string3 = "Pera y manzana"
string4 = "PERA Y manzana"
print(patron.match(string1))
print(patron.match(string2))
print(patron.match(string3))
print(patron.match(string4))

# #############################################
# Forma 2
# #############################################
m = re.search('(?i:abc)def', 'Abcdef')
print(m.group(0))

print('---'*23)
# #############################################
# Forma 3
# #############################################
patron2 = '(?i:pera) y manzana'
string5 = "pera y manzana"
string6 = "PERA y manzana"
string7 = "Pera y manzana"
string8 = "PERA Y manzana"
print(re.match(patron2, string5))
print(re.match(patron2, string6))
print(re.match(patron2, string7))
print(re.match(patron2, string8))
