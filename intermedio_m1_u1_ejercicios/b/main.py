import modulo2#Importamos y ejecutamos el código del archivo
print(modulo2.color)# La asignación crea un atributo
modulo2.color = "verde"# Modificamos el atributo en el módulo importado
import modulo2# Solo obtenemos el módulo ya cargado
print(modulo2.color)# El código no se recarga el atributo no ha retornado a su valor original

import modulo2 # Solo obtenemos el módulo ya cargado
print(modulo2.color) 
