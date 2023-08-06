def contador_yield(max):
    n=0
    while n < max:
        n=yield 
        n+=1
        print(n)

g=contador_yield(13)
g.__next__()
g.send(7)
g.close()
g.send(9)