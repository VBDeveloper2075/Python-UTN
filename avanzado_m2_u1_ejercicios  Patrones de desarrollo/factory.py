def factory(Clase, *args, **kwargs):
    return Clase(*args, **kwargs)

class Auto:
    def frenar(self, arg):
        print(arg)

class Moto:
    def __init__(self, color, marca="Fiat"):
        self.color=color
        self.marca=marca

obj1=factory(Auto)
obj1.frenar("El valor es dddd")
obj2=factory(Moto, "azul", "Chevrolet")
print(obj2.color)
