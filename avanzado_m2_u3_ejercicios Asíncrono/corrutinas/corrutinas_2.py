def ver_nombre(prefix):
    print("Inicia con: {}".format(prefix))
    while True:
        nombre=(yield)
        if prefix in nombre:
            print(nombre)

c=ver_nombre("Ju")
c.__next__()
c.send("Anna")
c.send("Juana")
c.send("Pedro")
c.send("Juan")