class Personas():

    def __init__(self, nombre, edad, salario, trabajo=None):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario
        self.trabajo=trabajo

    def apellido(self,):
        return self.nombre.split()[-1]

    def dar_aumento(self, porcentaje):
        self.salario*=1+porcentaje 


if __name__=="__main__":
    juan=Personas("Juan Marcelo Barreto", 7, 500)
    susana=Personas("Susana Anna Perez", 6, 300)
    susana.dar_aumento(0.1)

    base_personas=[juan, susana]
    for persona in base_personas:
        print(persona.nombre, persona.salario, persona.apellido())