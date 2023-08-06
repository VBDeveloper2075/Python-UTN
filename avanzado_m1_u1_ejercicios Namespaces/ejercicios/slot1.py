class Limites:
    __slots__=['edad', 'sexo', 'trabajo', 'salario']
    pass

x=Limites()
x.edad=4
print(x.edad)

#x.peso=4
#print(x.peso)
setattr(x, 'sexo', 'masculino')
print(getattr(x, 'edad'))
print(getattr(x, 'sexo'))
