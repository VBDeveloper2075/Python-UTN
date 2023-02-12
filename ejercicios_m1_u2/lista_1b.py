"""
enteros --> inmutables
strings --> inmutables
listas  --> mutables
diccionarios --> mutables
"""

persona1 = ["Pepe Pedro", "Perez", 4, "12345678", "30000"]
print(persona1)
persona2 = ["Anna", "Perez", 12, "12345622", "43000"]
print(persona2)
persona3 = ["Josefa", "Rodriguez", 4, "12345563", "50000"]
print(persona3)
personas = [persona1, persona2]
print(personas)
personas.append(persona3)
print(personas)
print("---" * 23)
print(personas[2] * 2)

empleados = []
empleados.extend([persona1, persona2])
print(empleados)
print(persona1[0].split()[-2])
