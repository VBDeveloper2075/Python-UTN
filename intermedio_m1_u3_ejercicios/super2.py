class AbueloPaterno(object):

    def __init__(self, *args, **kwars):
        print("AbueloPaterno")
        super(AbueloPaterno, self).__init__(*args, **kwars)


class AbueloMaterno(object):

    def __init__(self, *args, **kwars):
        print("AbueloMaterno")
        super(AbueloMaterno, self).__init__(*args, **kwars)


class Padre(AbueloPaterno):

    def __init__(self, arg, *args, **kwars):
        print("Padre", "arg = ", arg)
        super(Padre, self).__init__(arg, *args, **kwars)


class Madre(AbueloMaterno):

    def __init__(self, arg, *args, **kwars):
        print("Madre", "arg = ", arg)
        super(Madre, self).__init__(*args, **kwars)


class Hijo(Padre, Madre):

    def __init__(self, arg, *args, **kwars):
        print("Hijo", "arg = ", arg)
        super(Hijo, self).__init__(arg, *args, **kwars)


objeto = Hijo("celeste")

