def decorador_multiplicar_por10(funcion):
    def envoltura(*args):
        print(funcion(*args)*10)
    return envoltura

class Operaciones:
    @decorador_multiplicar_por10
    def sumar(self, a, b):
        c=a+b
        return c

@decorador_multiplicar_por10
def sumar(a, b):
    c=a+b
    return c

sumar(2, 3)
obj=Operaciones()
obj.sumar(2, 3)