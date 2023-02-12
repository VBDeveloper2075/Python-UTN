a = 5


def funcion():
    print(a)  # esta es global
    a = 10  # esta es local


funcion()

# da un error porque el programa quiere trabajar con una variable global y a continuación le cambio el valor, entonces no puede ejecutar la función ya que no sabe què valor usar
