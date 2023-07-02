a=[43, 23, 11, 78]
n = len(a)
#bucle for pra ordenar
for i in range(n-1):
    for j in range(n-1):
        if(a[j]>a[j+1]):
            aux=a[j]
            a[j]=a[j+1]
            a[j+1]=aux


print( "ORDENAR DE MAYOR A MENOR...")

print(a)
print(len(a))
print(a[0])
print(a[len(a)-1])