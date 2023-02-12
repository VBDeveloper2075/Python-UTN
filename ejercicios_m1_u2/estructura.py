import random

resultado = 5 * random.randint(0, 5)
print(resultado)

if resultado < 11:
    print("Es menor a 11")
else:
    print("Es mayor a 11")
