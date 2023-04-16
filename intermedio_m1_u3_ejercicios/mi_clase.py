class OperacionesM():

    def sumar(self, a, b):    #this
        c = a + b
        print("1: ", self)
        print(id(self))
        return c

#print(sumar(2, 3))

obj=OperacionesM()
print(obj.sumar(2,3))

print("1: ", obj)
print(id(obj))