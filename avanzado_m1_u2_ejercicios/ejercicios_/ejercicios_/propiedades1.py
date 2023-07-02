class Cliente():  

    def __init__(self, usuario):
        self._usuario=usuario

    def get_usuario(self,):
        print('Recuperar el usuario...')
        return self._usuario

    def set_usuario(self, valor):
        print('Modificar usuario...')
        self._usuario=valor

    def del_usuario(self,):
        print('Remover el usuario....')
        del self._usuario

    usuario=property(get_usuario, set_usuario, del_usuario, "Datos adicionales")

cliente1=Cliente("Anna")
print(cliente1.usuario)
cliente1.usuario='Ana'
print(cliente1.usuario)
#del cliente1.usuario
#print(cliente1.usuario)
print(Cliente.usuario.__doc__)