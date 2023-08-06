class Motor():
    voltaje_minimo=1.5
    voltaje_maximo=3

    @classmethod
    def salida(cls, voltaje_entrada):
        if voltaje_entrada>cls.voltaje_maximo:
            print("Con voltaje de entrada de : %s V se quema!"%(voltaje_entrada))
        elif voltaje_entrada<cls.voltaje_minimo:
            print("Con voltaje de entrada de : %s V no prende!"%(voltaje_entrada))
        else:
            print("Con voltaje de entrada de : %s V funciona!"%(voltaje_entrada))

    def prender(self, voltaje_entrada):
        self.salida(voltaje_entrada)

class Fuente():
    voltaje_salida=None

class FuenteAr(Fuente):
    voltaje_salida=220

class Fuente9V(Fuente):
    voltaje_salida=9

class FuenteArAdapter():
    voltaje_entrada=FuenteAr.voltaje_salida
    voltaje_salida=(Motor.voltaje_maximo+Motor.voltaje_minimo)/2

if __name__=="__main__":
    motor=Motor()
    print(motor.prender(FuenteAr.voltaje_salida))
    print(motor.prender(FuenteArAdapter.voltaje_salida))