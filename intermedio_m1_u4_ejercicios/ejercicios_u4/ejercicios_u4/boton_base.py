from tkinter import *
from parametros import bcolor, bfont, bsize

class BotonB:
    def __init__(self, parent=None, *args,**kwars) -> None:
        self.root=parent
        self.root.geometry("300x300")
        b1=Button(self.root, *args,**kwars)
        b1.pack(side=LEFT)
        b1.config(command=self.callback, bg=bcolor, font=(bfont, bsize))

    def callback(self,):
        print("Chau")
        self.root.quit()

if __name__=="__main__":
    root=Tk()
    mi_app = BotonB(root, text="Hola botón")
    root.mainloop()