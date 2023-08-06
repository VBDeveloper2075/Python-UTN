#PASO 1
from concurrent.futures import Future

#PASO 3
def retornar(parametro_futuro): 
    #PASO 5
    valor1 = parametro_futuro.result()
    print(valor1)

#PASO 2
obj = Future()
#PASO 4
obj.add_done_callback(retornar)
obj.set_result(['Hola', 'Clase'])