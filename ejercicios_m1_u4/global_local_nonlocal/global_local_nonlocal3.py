a = 5
b = 6


def nopisa():
    global a
    a = 10
    print(a, b)


nopisa()
print(a)
