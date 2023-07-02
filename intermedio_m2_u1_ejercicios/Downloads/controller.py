from tkinter import Tk
import vista

class Controller:

    def __init__(self, root_w):
        #PASO 2 - Creo atributos de instancia para la ventana y 
        # la instancia de Panel
        self.root = root_w
        self.objeto_vista=vista.Panel(self.root)

if __name__=="__main__":
    root = Tk()
    #mi_app=vista.Panel(root)
    # PASO 1 - Intancio el controlador
    mi_app=Controller(root)
    root.mainloop()