archivo = open("archivo1.txt", "r", encoding="utf-8")
print(archivo.readlines())
archivo.seek(0)
for x in archivo:
    print(x, end="")
archivo.close()