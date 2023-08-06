class Indice:
    lista=['M','a','n','z','a','n','a']
    def __getitem__(self, mi_indice):
        return mi_indice**0.5

    def __setitem__(self, mi_indice, valor):
        self.lista[mi_indice]=valor

x=Indice()
x[6]='o'
print(x.lista)