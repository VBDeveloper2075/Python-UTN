def dividir(x, y):
    try:
        resultado=x/y
    except ZeroDivisionError:
        print("dividir por 0")
    else:
        print("El resultado es: ", resultado)
    finally:
        print("Esto se da al final")

dividir(2, 1)
print("---"*23)
dividir(2, 0)