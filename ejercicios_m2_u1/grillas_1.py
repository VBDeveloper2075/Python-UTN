from tkinter import *

master = Tk()

el_id = Label(master, text="id")
el_id.grid(row=0, column=0, sticky=W)
nombre = Label(master, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)

entry_id = Entry(master)
entry_id.grid(row=0, column=1)
entry_nombre = Entry(master)
entry_nombre.grid(row=1, column=1)


master.mainloop()
