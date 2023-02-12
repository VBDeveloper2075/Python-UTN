persona1 = {
    "nombre": "Pepe Pedro",
    "apellido": "Perez",
    "edad": 4,
    "telefono": "12345678",
    "sueldo": "3000",
}

print(persona1["nombre"])
print(persona1.get("nombre"))
print(persona1.keys())
print(persona1.values())
print(persona1.items())
print(len(persona1))

print(persona1.items())
print(list(persona1.items()))
print(list(persona1.items())[0])
key0, value0 = list(persona1.items())[0]
print(list(persona1.items())[0])
print(key0, value0)
