print("Ejercicio 1", end="\n--------------\n")

numero = lambda num: num % 2 != 0
print(numero((int(input("ingrese un numero: ")))))
print(end="\n---------------\n")

print("Ejercicio 2", end="\n---------------\n")

multi = lambda x: x * 3
print(multi(int(input("Ingrese un numero a multiplicar por 3: "))))

print(end="\n---------------\n")
print("Ejercicio 3", end="\n---------------\n")

revertir = lambda cadena: cadena[::-1]
print(revertir(input("ingrese una frase: ")))

print(end="\n---------------\n")
print("Ejercicio 4", end="\n---------------\n")

suma = lambda x, y: x + y
print(suma(int(input("numero 1: ")), int(input("numero 2: "))))
