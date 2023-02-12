def modificar(a, b):
    a = 2
    b[0] = "Manzana"


variable_inmutable = 1
variable_mutable = [1, 2]
modificar(variable_inmutable, variable_mutable)
print(variable_inmutable, variable_mutable)

# los números son inmutables
# las listas son mutables
