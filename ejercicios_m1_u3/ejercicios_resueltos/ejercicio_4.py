"""
Ejercicio 4
Escriba un programa que solicite la edad de la persona e imprima
todos los años que la persona ha cumplido. 

"""
edad = int(input("Ingrese su edad :"))

if edad < 0:
    print("El valor ingresado no corresponde")
elif edad == 0:
    print(0)
else:
    for x in range(1, edad+1):
        print(x)
