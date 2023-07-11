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
Ejercicio 3
Operadores lógicos "and" y "or"

Hacer un programa que evalúe si un estudiante que ingresa en el instituto puede ser beneficiario de una beca, o no. El programa debe evaluar la distancia del alumno al lugar de estudio, si tiene hermanos, y cuál es el ingreso total familiar.

"""
