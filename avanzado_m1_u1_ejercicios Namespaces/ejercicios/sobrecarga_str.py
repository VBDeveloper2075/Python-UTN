class Usuarios:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def __str__(self, ):
        return "El nombre de usuario es: " + self.nombre


x=Usuarios("Anna")
print(x)