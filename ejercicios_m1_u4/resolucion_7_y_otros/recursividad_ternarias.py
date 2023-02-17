# ##############################################
# Recursión ####
# ##############################################


def mi_suma(L):
    return 0 if not L else L[0] + mi_suma(L[1:])  # Uso de expresión ternaria


def mi_suma1(L):
    return L[0] if len(L) == 1 else L[0] + mi_suma1(L[1:])


def mi_suma2(L):
    first, *rest = L
    return first if not rest else first + mi_suma2(rest)

print(mi_suma([1, 2, 3, 4, 5]))
print('',end='\n################\n' )
print(mi_suma1([1, 2, 3, 4, 5]))
print('',end='\n################\n' )
print(mi_suma2([1, 2, 3, 4, 5]))
 