def normal(a, b):
    c = a + b
    return c


print(normal(2, 4))

b = lambda a, b: a + b
print(b(2, 4))


numero = lambda num: num % 2 != 0
print(numero(4))
print(numero(5))
