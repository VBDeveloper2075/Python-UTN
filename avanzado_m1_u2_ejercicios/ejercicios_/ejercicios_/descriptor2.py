class AccederInstanciaMail():
    def __get__(self, instance, owner):
        print('Recuperar el usuario...')
        return instance._mail+'.ar'

    def __set__(self, instance, valor):   
        print('Modificar usuario...')
        instance._mail=valor

class Cliente:
    def __init__(self, usuario, _mail):
        self._usuario=usuario
        self._mail=_mail

    class DescriptorUsuario:

        "Documentación para el descriptor"
        def __get__(self, instance, owner):
            print('Recuperar el usuario...')
            print(self, instance, owner)
            return instance._usuario.upper()

        def __set__(self, instance, valor):
            print('Modificar usuario...')
            instance._usuario=valor

        def __delete__(self, instance):
            print('Remover el usuario....')
            del instance._usuario
    usuario=DescriptorUsuario()
    mail=AccederInstanciaMail()

cliente1=Cliente("Anna", 'anna@gmail.com')
print(cliente1.usuario, cliente1._mail, cliente1.mail)
#cliente1.usuario='Ana'
#print(cliente1.usuario)
#del cliente1.usuario
#print(cliente1.usuario)
#print(Cliente.usuario.__doc__)