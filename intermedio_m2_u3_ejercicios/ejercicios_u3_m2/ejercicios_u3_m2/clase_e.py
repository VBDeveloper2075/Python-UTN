class B(Exception):
    color="rojo"

class C(B):
    color="verde"

class D(C):
    color="azul"

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
        print(D.color)
    except C:
        print("C")
        print(C.color)
    except B:
        print("B")
        print(B.color)