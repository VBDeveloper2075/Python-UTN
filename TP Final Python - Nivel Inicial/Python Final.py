from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter as tk
import sqlite3
import os

# from PIL import ImageTk, Image
import re

# --------------------------iMPORTO IMAGEN--------------------------#

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "logo1.png")

master = Tk()
master.title("Appointment System")
master["background"] = "#F7F3F3"

# --------------------------CREAR BASE DE DATOS--------------------------#


def conexion():
    con = sqlite3.connect("baseDeDatos.db")
    return con


# --------------------------CREAR TABLA----------------------------------#


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS pacientes (id integer PRIMARY KEY AUTOINCREMENT, paciente text, especialidad text, dia text, hora text, obra_social text)"
    cursor.execute(sql)
    con.commit()


con = conexion()
crear_tabla(con)


# --------------------------ETIQUETAS Y CAMPOS DE ENTRADA Tkinter--------------------------#

titulo = Label(
    master, text="INGRESE SUS DATOS", bg="#D83737", fg="thistle1", height=1, width=60
)
titulo.grid(row=0, column=0, columnspan=6, padx=2, pady=2, sticky=W + E)

# Defino variables para tomar valores de campos de entrada
entry_paciente, entry_especialidad, entry_dia, entry_hora, entry_obra_social = (
    StringVar(),
    StringVar(),
    IntVar(),
    StringVar(),
    StringVar(),
)
w_ancho = 20

paciente = Label(master, text="Paciente:")
paciente.grid(
    row=1,
    column=0,
    sticky=W,
)
entry_paciente = Entry(master, textvariable=entry_paciente, width=70)
entry_paciente.grid(row=1, column=1)

especialidad = Label(master, text="Especialidad:")
especialidad.grid(row=2, column=0, sticky=W)
entry_especialidad = Entry(master, textvariable=entry_especialidad, width=70)
entry_especialidad.grid(row=2, column=1)

dia = Label(master, text="Día:")
dia.grid(row=3, column=0, sticky=W)
entry_dia = Entry(master, textvariable=entry_dia, width=50)
entry_dia.grid(row=3, column=1)

hora = Label(master, text="Hora:")
hora.grid(row=4, column=0, sticky=W)
entry_hora = Entry(master, textvariable=entry_hora, width=50)
entry_hora.grid(row=4, column=1)

obra_social = Label(master, text="Obra Social:")
obra_social.grid(row=5, column=0, sticky=W)
entry_obra_social = Entry(master, textvariable=entry_obra_social, width=70)
entry_obra_social.grid(row=5, column=1)

# ------------------------------------VISTA FOTO------------------------------------#

# image2 = Image.open(ruta)
# image1 = ImageTk.PhotoImage(image2)
# background_label = tk.Label(master, image=image1)
# background_label.place(x=600, y=30)

# ------------------------------------TREEVIEW------------------------------------#

tree = ttk.Treeview(master)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=50, minwidth=50)
tree.column("col2", width=50, minwidth=50)
tree.column("col3", width=200, minwidth=80)
tree.column("col4", width=200, minwidth=80)
tree.column("col5", width=200, minwidth=80)

tree.heading("#0", text="ID")
tree.heading("col1", text="Paciente    ")
tree.heading("col2", text="Especialidad")
tree.heading("col3", text="Fecha       ")
tree.heading("col4", text="Hora        ")
tree.heading("col5", text="O.Social    ")

tree.grid(row=12, column=0, columnspan=4)

# ------------------------------------BOTONES------------------------------------#

s = ttk.Style()
s.configure("Peligro.TButton", foreground="#ff0000")
s.map("Peligro.TButton", foreground=[("active", "#7DCEA0")])

botonagregar = ttk.Button(
    master,
    text="Agregar",
    style="Peligro.TButton",
    command=lambda: funcion_a(
        entry_paciente.get(),
        entry_especialidad.get(),
        entry_dia.get(),
        entry_hora.get(),
        entry_obra_social.get(),
        tree,
    ),
)
botonagregar.grid(row=20, column=1, sticky=E + W)

botonEditar = ttk.Button(
    master,
    text="Editar",
    style="Peligro.TButton",
    command=lambda: funcion_b(
        entry_paciente.get(),
        entry_especialidad.get(),
        entry_dia.get(),
        entry_hora.get(),
        entry_obra_social.get(),
        tree,
    ),
)
botonEditar.grid(row=20, column=0, sticky=E)

botonborrar = ttk.Button(
    master, text="Borrar", style="Peligro.TButton", command=lambda: funcion_c(tree)
)
botonborrar.grid(row=20, column=2, sticky=W)

titulo2 = Label(master, bg="#D83737", fg="thistle1", height=1, width=60)
titulo2.grid(row=30, column=0, columnspan=6, padx=2, pady=2, sticky=W + E)
titulo3 = Label(master, bg="#D83737", fg="thistle1", height=1, width=60)
titulo3.grid(row=18, column=0, columnspan=6, padx=2, pady=2, sticky=W + E)

# ------------------------------------MOSTRAR------------------------------------#

# Bucle de ejecución
mostrar(con)
master.mainloop()
