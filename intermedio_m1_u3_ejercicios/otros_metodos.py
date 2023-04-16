class OperacionesM():

    variable = ""

    def sumar(a, b):     
        c = a + b
        return c


obj=OperacionesM()
print(obj.sumar(2, 3))
print(OperacionesM.sumar(2, 3))