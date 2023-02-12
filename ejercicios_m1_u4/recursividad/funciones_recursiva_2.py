def mi_suma(param):
    if not param:
        return 0
    return secundaria(param)


def secundaria(param):
    return param[0] + mi_suma(param[1:])


print(mi_suma([1.1, 2.2, 3.3, 4.4]))

"""
 
"""
