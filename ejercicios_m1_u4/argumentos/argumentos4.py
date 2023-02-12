def f(a, *args):
    for arg in args:
        print(arg)


f(0, 1, 2, "Manzana")


def f2(**kwargs):
    # el doble asterisco indica que es un diccionario
    # puedo mezclar dentro de una función tuplas, diccionarios, etc

    if kwargs is not None:
        for clave, valor in kwargs.items():
            print(clave, " ==> ", valor)


f2(nombre="Anna", edad=49)
