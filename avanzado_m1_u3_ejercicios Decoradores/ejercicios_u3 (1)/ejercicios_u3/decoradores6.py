def contar_llamadas(funcion):
    def envoltura(*args, **kwargs):
        envoltura.numero_de_llamada+=1
        print("Llamada número %s a la función %s" %(envoltura.numero_de_llamada, funcion.__name__))
        return funcion(*args, **kwargs)
    envoltura.numero_de_llamada=0
    return envoltura

@contar_llamadas
def sumar(a, b):
    c=a+b
    return c

sumar(2, 3)
sumar(3, 4)