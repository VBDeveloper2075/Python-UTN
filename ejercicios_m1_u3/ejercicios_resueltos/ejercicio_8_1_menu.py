"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""
#eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
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


while valor == True:
    print("eleccion: ", eleccion)

    if eleccion=='a':
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    elif eleccion=='e':
        print("eeeeeeeeeeeeeeeeeeeee")
    elif eleccion=='l':
        print("llllllllllllllllllll")
    elif eleccion=='m':
        print("mmmmmmmmmmmmmmmmmmmmm")
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
#for x in compra:
#    print("Producto: ", x[0], "cantidad: ", x[1], "precio: ", x[2])