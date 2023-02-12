"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""
#eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
el_id=0
compra=[]
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
    el_id += 1
    total = total + float(cantidad)*float(precio)
    compra.append([el_id, producto, cantidad, precio])
    print("Estoy en alta")

def borrar(id_borrar): 
    global total
    global compra
    for x in compra:
        if x[0]==int(id_borrar):
            compra.remove(x)
            total = total -float(x[2])*float(x[3])
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
    print(id_modificar, precio)
    for x in compra:
        if x[0]==int(id_modificar):
            a_modificar=float(x[3])
            x[3]=float(precio)
            total = total + float(x[2])*float(precio)-float(x[2])*a_modificar


while valor == True:
    print("eleccion: ", eleccion)

    if eleccion=='a':
        producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
        alta(producto, cantidad, precio)
    elif eleccion=='e':
        id_borrar = input("Ingrese el id del elemento a borrar: ")
        borrar(id_borrar)
    elif eleccion=='l':
        listar()
    elif eleccion=='m':
        id_modificar, precio = input("Ingrese el id y el nuevo precio: ").split()
        modificar(id_modificar, precio)
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