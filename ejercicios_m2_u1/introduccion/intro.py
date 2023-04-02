from tkinter import *

root = Tk()
e = Entry(root)
e.pack()

# *********************************
a = 4
b = 5
c = a + b
d = "Mi resultado es: " + str(c)
# *********************************

var = StringVar()
e.config(textvariable=var)
var.set(d)
root.mainloop()
