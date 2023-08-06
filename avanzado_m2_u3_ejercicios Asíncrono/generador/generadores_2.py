def contador_yield(max):
    n=0
    while n < max:
        yield n
        n+=1

#g=contador_yield(3)
#print(next(g))

for x in contador_yield(5):
    print(x)