class Usuarios():
    class __Usuarios:
        def __init__(self,):
            self.usuario=None

        def __str__(self):
            return repr(self)+ " --- "+self.usuario

        def imprimir(self,):
            print("hola")

    instancia=None

    def __new__(cls):
        if not Usuarios.instancia:
            Usuarios.instancia=Usuarios.__Usuarios() 
        return Usuarios.instancia

anna = Usuarios()
anna.usuario="anita"
print(anna)
print(anna.imprimir())
print("---"*23)
pedro = Usuarios()
pedro.usuario="pedrito"
print(pedro)
print(pedro.imprimir())