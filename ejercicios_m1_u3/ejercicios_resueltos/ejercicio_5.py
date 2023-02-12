"""
Ejercicio 5
Suponga que tiene una verdulería y carga la cantidad y el precio
de lo comprado por un cliente. Realice un programa que tome
de a uno la cantidad y el precio comprado por el cliente y
al finalizar la compra retorne el monto total gastado. 
 
"""
eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
total = 0
if eleccion == "i":
    valor=True
else:
    valor=False


while valor == True:
    producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
    total = total + float(cantidad)*float(precio)
    eleccion = input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter: ")
    if eleccion == "i":
        valor=True
    else:
        valor=False
print("El costo total de lo comprado es: ", total)
