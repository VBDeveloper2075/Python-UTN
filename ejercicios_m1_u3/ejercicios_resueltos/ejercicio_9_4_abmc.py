"""
Ejercicio9
A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
Pregunta: Considera que es más fácil guardar la información en listas o en diccionarios


"""
#eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
el_id=0
compra={}
total = 0
"""if eleccion == "i":
    valor=True
else:
    valor=False"""

def menu():
    print("\n Elija una opción: ")
    print("    (a) Agregar producto")
    print("    (e) Eliminar producto")
    print("    (l) Listar producto")
    print("    (m) Modificar producto")
    print("    ó cualquier otra tecla para salir")
    global valor
    global eleccion
    eleccion = input()
    if eleccion=="a" or eleccion=="e" or eleccion=="l" or eleccion=="m":
        valor=True
        print("ingresada")
    else:
        valor=False
        print("Chau")

menu()

def alta(producto, cantidad, precio): 
    global total
    global el_id

    total = total + float(cantidad)*float(precio)
    compra[el_id]= {'producto':producto, 'cantidad':cantidad, 'precio':precio}
    el_id += 1
    print("Estoy en alta")

def borrar(id_borrar): 
    global total
    global compra
    print(compra[id_borrar])

    total = total - (float(compra[id_borrar]['cantidad'])*float(compra[id_borrar]['precio']))
    del compra[id_borrar]
    print("Estoy en borrar")

def listar(): 
    global compra
    global total
    print(compra)
    print(total)
    print("Estoy en listar")

def modificar(id_modificar, precio): 
    global compra
    global total
    antes = float(compra[id_modificar]['cantidad'])*float(compra[id_modificar]['precio'])
    compra[id_modificar]['precio']=precio 
    despues = float(compra[id_modificar]['cantidad'])*float(compra[id_modificar]['precio']) 
    total = total + despues - antes


while valor == True:
    print("eleccion: ", eleccion)

    if eleccion=='a':
        producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
        alta(producto, cantidad, precio)
    elif eleccion=='e':
        id_borrar = input("Ingrese el id del elemento a borrar: ")
        borrar(int(id_borrar))
    elif eleccion=='l':
        listar()
    elif eleccion=='m':
        id_modificar, precio = input("Ingrese el id y el nuevo precio: ").split()
        modificar(int(id_modificar), float(precio))
    else:
        break

    menu()
    """producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
    total = total + float(cantidad)*float(precio)
    compra.append([producto, cantidad, precio])
    eleccion = input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter: ")
    if eleccion == "i":
        valor=True
    else:
        valor=False"""
#print("El costo total de lo comprado es: ", total)
#print(compra)
for x in compra:
    print("Producto: ", x[0], "cantidad: ", x[1], "precio: ", x[2])