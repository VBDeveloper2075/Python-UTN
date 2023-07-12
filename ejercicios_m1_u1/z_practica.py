""" 
Ejercicio 1

Programa que verifica la mayoría de edad de quienes ingresan a un club. Si son menores de 18 no pueden pasar . Si son mayores de 110 tiene que indicar que hay un error



print("\n\t Verificación de acceso")

edad_usuario=int(input("\n\n\t Ingresa tu edad: "))

if 0>edad_usuario or edad_usuario >110:
    print("\n\t Hay un error. Ejecuta nuevamente e ingresa tu edad.")
elif edad_usuario<18:
    print("\n\t Eres menor, no puedes pasar")
elif edad_usuario>=18:
    print("\n\t Bienvenido al club")
else:
    print("\n\t Hay un error. Ejecuta nuevamente e ingresa tu edad.")

print("\n\t El programa finalizó\n") 




nota:
con el alt (que está a la derecha de la barra espaciadora)
+ n .... sale un salto de línea
con el alt (que está a la derecha de la barra espaciadora)
+ t .... sale un sangría


"""

"""
Ejercicio 2

Programa que otorga calificación al alumno 
según su nota


print("Valoración del Aprendizaje logrado")

nota_lograda=int(input("Ingresa tu nota: "))

if nota_lograda<4:
  print("Insuficiente")
  
elif nota_lograda<6:
  print("Regular")
  
elif nota_lograda<8:
  print("Aprobado")
  
elif nota_lograda<9:
  print("Excelente")
  
else:
  print("Sobresaliente")

print("El programa finalizó") 

****Aunque en el ejercicio 2 si el usuario pone 5678 le va a tirar sobresaliente. Habría que hacer como en el 1:
elif nota_lograda=10:
  print("Bienvenido al club")
else:
  print("Hay un error. Ejecuta nuevamente e ingresa tu nota.")
  
También se puede hacer un bucle para que el programa se ejecute automáticamente si hay error

"""

"""
Ejercicio 3

Verificar que los sueldos de los empleados tengan relación con su responsabilidad en la empresa. 
Usamos concatenación de operaciones de comparación

salario_presidente=int(input("\n\t Introduce el salario del Presidente: "))
print("\n\t Salario Presidente: " + str(salario_presidente))

salario_director=int(input("\n\t Introduce el salario del Director: "))
print("\n\t Salario Director: " + str(salario_director))

salario_jefe_area=int(input("\n\t Introduce el salario del Jefe de Area: "))
print("\n\t Salario Jefe de Area: " + str(salario_jefe_area))

salario_administrativo=int(input("\n\t Introduce el salario del Administrativo: "))
print("\n\t Salario Administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
  print("Todo funciona correctamente")
else:
  print("Algo falla en esta empresa")

"""


"""
Ejercicio 4
Operadores lógicos "and" y "or"


Hacer un programa que evalúe si un estudiante que ingresa en el instituto puede ser beneficiario de una beca, o no. El programa debe evaluar la distancia del alumno al lugar de estudio, si tiene hermanos, y cuál es el ingreso total familiar.

"and" --- *y si además   ....y "or" --- *o si no   


distancia_hogar=int(input("\n\t Introduce la distancia domicilio-instituto (en kilómetros): "))
print("\n\t Distancia al Instituto: " + str(distancia_hogar))

hermanos_escolarizados=int(input("\n\t Cantidad de hermanos actualmente escolarizados: "))
print("\n\t Cantidad de hermanos escolarizados: " + str(hermanos_escolarizados))

salario_familiar=int(input("\n\t Introduce el salario mensual que recibe la familia: "))
print("\n\t Salario mensual de la familia: " + str(salario_familiar))

if distancia_hogar>40 and hermanos_escolarizados>3 and salario_familiar<80000:
    print("\n\t Tienes derecho a la Beca")
    
else: 
    print("\n\t No tienes derecho a la Beca")

# también podría poner que aunque no cumpla con la cantidad de hermanos o la distancia, si tiene un sueldo muy bajo obtenga igualmente la beca. entonces uso el operador "or"

distancia_hogar=int(input("\n\t Introduce la distancia domicilio-instituto (en kilómetros): "))
print("\n\t Distancia al Instituto: " + str(distancia_hogar))

hermanos_escolarizados=int(input("\n\t Cantidad de hermanos actualmente escolarizados: "))
print("\n\t Cantidad de hermanos escolarizados: " + str(hermanos_escolarizados))

salario_familiar=int(input("\n\t Introduce el salario mensual que recibe la familia: "))
print("\n\t Salario mensual de la familia: " + str(salario_familiar))

if distancia_hogar>40 and hermanos_escolarizados>3 or salario_familiar<80000:
    print("\n\t Tienes derecho a la Beca")
    
else: 
    print("\n\t No tienes derecho a la Beca")

"""

"""
Ejercicio 5

bucle for

for i in  [1,2,3]:
  print ("Hola")
  
  # así imprime ehola en cada iteración:
for i in  ["primavera","verano","otoño","invierno"]:
  print ("Hola")

# así imprime el valor de la variable i:
for i in  ["primavera","verano","otoño","invierno"]:
  print (i) 


"""

"""
Ejercicio 6

Identificar si el mail que ingresó el usuario es correcto, evaluando si ingresó el @ y el punto (de .com, .org...)

email = False

for i in "vero@gmail.com":
    if i == "@":
        email = True

if email:
    print("El mail es correcto")
else:
    print("El mail es correcto")
    
"""


# email = False
# miEmail = input("\n\t introduce tu correo electrónico:  ")

# for i in miEmail:
#     if i == "@":
#         email = True

# if email:
#     print("El mail es correcto")
# else:
#     print("El mail es correcto")

"""
Ejercicio 7

'in range' quiere decir que recorra cierto rango
acá se pone f"" string  para que imprima la variable en cada vuelta. Dicha variable: "i" se pone entre llaves.

for i in range(5):
    print(f"valor de la variable {i}")

- también se puede usar para indicar que queremos trabajar con los datos entre determinado rango. en el ejemplo se trabaja con los números del 5 al 49 y saltando de 3 en 3.

for i in range(5,50,3):
    print(f"valor de la variable {i}")

-----
Ahora queremos validar el mail que ingresa un usuario.

contiene_arroba = False

email = input("\n\t Introduce tu email: ")

for i in range(len(email)):
    if email[i] == "@":
        contiene_arroba = True

if contiene_arroba:
    print("Email correcto")

else:
    print("Email incorrecto")

Se puede mejorar así:

email=input("Introduce tu email, por favor: ")

for i in email:

    if i=="@":
        
        arroba:True
        
        break;

else:

    arroba=False

print(arroba)

"""

    
"""
Ejercicio 8
 Bucle while  ... mientras que:...
 
 i=1
 while i<=10
     print("Ejecución" + str(i))
     i=i+1  

print("Terminó la ejecución")
 
"""
"""
edad=int(input("Introduce tu edad por favor: "))

while edad<5 or edad>100:
    print("\n\t Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad=int(input("Introduce tu edad por favor: "))
  
  print("\n\t Gracias por colaborar. Puedes pasar.")
  print("\n\t Edad del aspirante " + str(edad))

"""