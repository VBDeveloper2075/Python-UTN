def fuente(sentencia, corrutina): 
    palabras=sentencia.split(" ")
    for palabra in palabras:
        corrutina.send(palabra)
    corrutina.close()

def mi_filtro(patron="do", proxima_corrutina=None):
    print("Estoy buscando el patrón: {}".format(patron))
    try:
        while True:
            palabra = yield
            if patron in palabra:
                proxima_corrutina.send(palabra)
    except GeneratorExit:
        print("Se realizo el filtrado")

def destino():
    print("Estoy en destino")
    try:
        while True:
            palabra=yield
            print(palabra)
    except GeneratorExit:
        print("Se realizo con el presentado de datos encontrados")


pt = destino()
pt.__next__()

pf=mi_filtro(proxima_corrutina=pt)
pf.__next__()

oracion="Estoy corriendo y saltando así como jugando"
fuente(oracion, pf)