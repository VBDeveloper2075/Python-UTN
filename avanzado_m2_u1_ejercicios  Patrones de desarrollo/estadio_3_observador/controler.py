from tkinter import Tk
import vista
import observador

# from modelo import *


class Controller:
    """
    Está es la clase principal
    """

    def __init__(self, root):
        self.root_controler = root
        self.objeto_vista = vista.Ventanita(self.root_controler)
        self.el_observador = observador.ConcreteObserverA(self.objeto_vista.objeto_base)


if __name__ == "__main__":
    root_tk = Tk()
    application = Controller(root_tk)

    application.objeto_vista.actualizar()
    root_tk.mainloop()
