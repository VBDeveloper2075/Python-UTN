def generador():
    n=1
    print("Primera vez")
    yield n

    n+=1
    print("Segunda vez")
    yield n

g=generador()
print(g)
print(next(g))
print(next(g))