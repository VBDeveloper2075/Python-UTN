"""
Ejercicio 7
A partir del ejercicio 5 cree un programa que vaya 
agregando en un diccionario las compras realizadas.

"""
eleccion = input("Para iniciar ingrese 'i', para finalizar ingrese 'f': ")
compra={}
total = 0
el_id = 0
if eleccion == "i":
    valor=True
else:
    valor=False


while valor == True:
    producto, cantidad, precio = input("Ingrese el nombre la cantidad de producto en kg y el precio separado por espacio: ").split()
    total = total + float(cantidad)*float(precio)
    compra[el_id]= {'producto':producto, 'cantidad':cantidad, 'precio':precio}
    el_id+=1
    eleccion = input("Para agregar otro producto ingrese 'i', para finalizar ingrese cualquier otro caracter: ")
    if eleccion == "i":
        valor=True
    else:
        valor=False
print("El costo total de lo comprado es: ", total)
print(compra)
