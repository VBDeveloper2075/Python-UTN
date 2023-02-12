"""
Ejercicio 6
A partir del ejercicio 5 cree un programa que vaya agregando 
en una lista las compras realizadas.
"""
eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
compra=[]
total = 0
if eleccion == "i":
    valor=True
else:
    valor=False


while valor == True:
    producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
    total = total + float(cantidad)*float(precio)
    compra.append([producto, cantidad, precio])
    eleccion = input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter: ")
    if eleccion == "i":
        valor=True
    else:
        valor=False
print("El costo total de lo comprado es: ", total)
print(compra)
for x in compra:
    print("Producto: ", x[0], "cantidad: ", x[1], "precio: ", x[2])