__all__ = ['variableACompartir1', 'funcionACompartir1']

variablePrivada1 = "Hola variable privada 1"
variableACompartir1 = "Hola variable pública 1"
def funcionACompartir1():
    return 'Hola función pública 1'
print("i-----------------------")
print(variablePrivada1)
print(variableACompartir1)
print(funcionACompartir1())
print("f-----------------------")