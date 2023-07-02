if __name__=="__main__":
    import shelve
    from clases.cls_personas import Personas
    from clases.cls_gerentes import Gerentes

    juan=Personas("Juan Marcelo Barreto", 7, 500)
    susana=Personas("Susana Anna Perez", 6, 300)
    susana.dar_aumento(0.1)
    tom=Gerentes("Tomás Perez", 10, 1000, "software")
    tom.dar_aumento(0.3)

    base_personas=[juan, susana, tom]
    for persona in base_personas:
        print(persona.nombre, persona.salario, persona.apellido())

    db=shelve.open("personas")
    db["juan"]=juan
    db["susana"]=susana
    db["tom"]=tom
    db.close()