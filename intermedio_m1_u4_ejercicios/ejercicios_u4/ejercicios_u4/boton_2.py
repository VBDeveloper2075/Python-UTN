from tkinter import *
from boton_base import BotonB

class MiBoton(BotonB):
     
    def callback(self,):
        print("Estoy en mi boton")
         

if __name__=="__main__":
    root=Tk()
    mi_app = MiBoton(root, text="Hola botón")
    root.mainloop()