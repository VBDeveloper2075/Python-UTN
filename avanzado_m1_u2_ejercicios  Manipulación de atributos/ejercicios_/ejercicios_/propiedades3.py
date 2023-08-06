class Empresa:
    def __init__(self, usuario):
        self._usuario=usuario

    @property
    def usuario(self,):
        """Datos adicionales"""
        print('Recuperar el usuario...')
        return self._usuario

    @usuario.setter
    def usuario(self, valor):
        print('Modificar usuario...')
        self._usuario=valor

    @usuario.deleter
    def usuario(self,):
        print('Remover el usuario....')
        del self._usuario



class Cliente(Empresa): pass

cliente1=Cliente("Anna")
print(cliente1.usuario)
cliente1.usuario='Ana'
print(cliente1.usuario)
#del cliente1.usuario
#print(cliente1.usuario)
print(Cliente.usuario.__doc__)