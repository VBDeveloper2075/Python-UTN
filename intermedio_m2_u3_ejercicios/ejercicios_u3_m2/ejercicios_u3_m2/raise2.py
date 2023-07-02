import sys

try:
    frutas=["Pera", "Manzana"]
    print(frutas[7])
except IndexError as e:
    print("---: ", e)
    print(sys.exc_info())
    mi_except = IndexError("Hay un error en el indice")
    raise mi_except

