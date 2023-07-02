class DecoradorMultiplicarPor10:
    def __init__(self, func) -> None:
        self.func=func

    def __call__(self, *args):
        print(self.func(*args)*10)


"""class Operaciones:
    @DecoradorMultiplicarPor10
    def sumar(self, a, b):
        c=a+b
        return c"""

@DecoradorMultiplicarPor10
def sumar(a, b):
    c=a+b
    return c

sumar(2, 3)
#obj=Operaciones()
#obj.sumar(2, 3)