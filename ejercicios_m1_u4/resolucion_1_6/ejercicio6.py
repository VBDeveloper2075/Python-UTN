def orden(lista):
    global lista_ordenada
    if not lista:
        return
    else:
        menor = min(lista)
        lista.remove(menor)
        lista_ordenada.append(menor)
        orden(lista)


mi_lista = [3, 44, 21, 78, 5, 56, 9, 3]
lista_ordenada = []
print(f"Su lista original es: \n{mi_lista}")
orden(mi_lista)
print(f"Su lista ordenada es: \n{lista_ordenada}")
