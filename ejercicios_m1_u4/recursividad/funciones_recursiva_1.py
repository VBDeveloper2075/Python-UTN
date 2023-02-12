def mi_suma(param):
    print(param)
    if not param:
        return 0
    else:
        return param[0] + mi_suma(param[1:])


print(mi_suma([1, 2, 3, 4, 5]))

"""
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
[]
1 + 2 + 3 + 4 + 5 + 0


"""
