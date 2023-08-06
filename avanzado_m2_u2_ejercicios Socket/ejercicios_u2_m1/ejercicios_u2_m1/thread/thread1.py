from ast import arg
import threading
import time

def en_espera(arg, tiempo):
    print("Esté argumento se pasa en el hilo: {}, {} segundos despues \n".format(arg, tiempo))
    time.sleep(tiempo)
    print("El hilo; {} finaliza su ejecución \n".format(arg))

t=threading.Thread(target=en_espera, name="thread", args=("thread", 7))
t.start()
t.join()
print("hola")