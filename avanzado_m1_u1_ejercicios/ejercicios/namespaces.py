class ClasePadre():
    atributo="verde"
    def metodo1(self,):pass

class ClaseHija(ClasePadre):
    atributo="verde"
    def metodo1(self,):pass   

class ClaseHija2(ClasePadre):

    def __init__(self, color):
        self.color=color
    atributo="verde"
    def metodo1(self,):pass   

x=ClaseHija()
y=ClaseHija2("verde")
print(x.__dict__)
print(y.__dict__)
print(x.__class__)
print(ClaseHija.__bases__)
print(ClaseHija2.__dict__.keys())