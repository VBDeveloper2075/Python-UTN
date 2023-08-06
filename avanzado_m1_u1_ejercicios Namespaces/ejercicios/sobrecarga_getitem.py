class Indice:
    def __getitem__(self, mi_indice):
        return mi_indice**0.5

x=Indice()
print(x[64])