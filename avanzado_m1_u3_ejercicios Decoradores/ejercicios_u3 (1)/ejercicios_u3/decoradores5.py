def modo_de_trabajo(valor=False):
    def _modo_de_trabajo(funcion):
        def interna(*args, **kwargs):
            if valor:
                print("Estoy en producción")
            else:
                print("Estoy en desarrollo")
            for id, argumento in enumerate(args):
                print("argumento %d:%s " %(id, argumento))
            funcion(*args, **kwargs)
        return interna
    return _modo_de_trabajo


@modo_de_trabajo(False)
def registro_usuario(nombre, apellido):
    print("Registro de : %s " %nombre)

registro_usuario("Anna", "Rodriguez")