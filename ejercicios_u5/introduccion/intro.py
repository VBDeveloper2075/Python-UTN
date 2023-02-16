from tkinter import *

root = Tk()  # con esto abro la ventana.tk es una ventana emergente
e = Entry(
    root
)  # entry es el campo de entrada de texto llamado e, y tiene un valor que le puse con el set
e.pack()

# *********************************
a = 4
b = 5
c = a + b
d = "Mi resultado es: " + str(c)
# *********************************

var = StringVar()
# StringVar es un tipo de dato string de tkinter
e.config(textvariable=var)
# esto permite que la variable pueda sacar(.get) o poner (.set) info en el campo de entrada
var.set(d)  # le pongo un valor
root.mainloop()  # para cerrar la ventana
