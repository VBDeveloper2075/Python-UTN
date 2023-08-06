from tkinter import *


class temas:
    def tema1(self, root):
        self.root = root
        self.tema_1 = "yellow"
        self.root.configure(background=self.tema_1)
        return self.root

    def tema2(self, root):
        self.root = root
        self.tema_2 = "white"
        self.root.configure(background=self.tema_2)
        return self.root

    def tema3(self, root):
        self.root = root
        self.tema_3 = "red"
        self.root.configure(background=self.tema_3)
        return self.root
