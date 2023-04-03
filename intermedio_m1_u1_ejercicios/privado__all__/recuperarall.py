from privadoall import *
#from privado__all__ import variablePrivada1
print(variableACompartir1)
print(funcionACompartir1())

# variablePrivada1 no es exportado por el módulo ya que no esta definido
#dentro de __all__
# no es accesible mediante : from privadoall import *

print(variablePrivada1)


