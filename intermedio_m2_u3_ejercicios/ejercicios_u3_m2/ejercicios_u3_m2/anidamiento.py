def evento2():
    print(1+"pera")

def evento1():
    try:
        evento2()
    except TypeError:
        print("Try interno")

try:
    evento1()
except TypeError:
    print("Try externo")