# ejercicio 6

lista=[3,44,21,78,5,56,9]
lista_ordenada=[]

def ordenar(lista):

    for x in range(0,len(lista)):
        lista_ordenada.append(min(lista))
        indice=lista.index(min(lista))
        lista[indice]=max(lista)+1
            

ordenar(lista)
print(lista_ordenada)
