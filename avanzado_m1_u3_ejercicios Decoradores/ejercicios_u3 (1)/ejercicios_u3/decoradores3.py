def decorador(cls):
    class Envoltura:
        def __init__(self, *args):
            self.instancia_de_clase=cls(*args)

        def __getattr__(self, nombre):
            print(self.__class__)
            print(self.instancia_de_clase.__class__)
            print("Nombre de atributos de la clase Auto: ", nombre)
            return getattr(self.instancia_de_clase, nombre)
            
    return Envoltura

@decorador
class Auto:
    def __init__(self, color, marca):
        self.color=color
        self.marca=marca

x=Auto("Rojo", "Renault")
print(x.color)
print(x.marca)