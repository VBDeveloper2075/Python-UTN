from clases.cls_personas import Personas

class Gerentes(Personas):
    def dar_aumento(self, porcentaje, premio=0.1):
        self.salario*=1+porcentaje+premio