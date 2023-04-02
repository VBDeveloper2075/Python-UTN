from tkinter import *
from tkinter.messagebox import *
import random
import re
import sqlite3
#https://docs.python.org/3/library/sqlite3.html
#https://www.sqlitetutorial.net/sqlite-python/

#interfaz
root = Tk()
root.title("Tarea POO")
ventana = Frame(root, bg="#FF7F50", height=122,borderwidth=2, relief=RAISED)
ventana.grid(row=10, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

        
titulo = Label(root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

producto = Label(root, text="Producto")
producto.grid(row=1, column=0, sticky=W)
descripcion = Label(root, text="Descripción")
descripcion.grid(row=2, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val = StringVar(), StringVar()
w_ancho = 20

# Creo una función para generar las entradas
def entradas(txt_var, width_e, row, col):
    entrada = Entry(root, textvariable = txt_var, width = width_e) 
    entrada.grid(row = row, column = col)
    return entrada
# Ejecuto la función tres veces, con diferentes parámetros de forma
# de generar los tres campos de entrada en la pantalla y poder recuperar
# los valores ingresados.
entradas(a_val, w_ancho, 1, 1)
entradas(b_val, w_ancho, 2, 1)

#modificar boton color 
def cambiarcolor():
    colores = ['snow', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'tomato2', 'OrangeRed2']
    color = random.choice(colores) 
    root.configure(background=color)

Button(root, text="Sorpresa", command=cambiarcolor).grid(row=6, column=2, sticky=W+E)


# ###########################################
def conexion():
    con = sqlite3.connect('mibase.db')
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = '''CREATE TABLE productos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  producto varchar(20) NOT NULL,
                  descripcion varchar(20) NOT NULL)'''
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
except:
    print("hay un eror en la creación")


def alta(producto, descripcion):
    con = conexion()
    print("Nueva alta de datos")
    cadena=producto#obtenemos la cadena del campo de texto
    patron="^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"
    if(re.match(patron,cadena)):
        print("validado")
        cursor = con.cursor()
        data = (producto, descripcion)
        sql = "INSERT INTO productos(producto, descripcion) VALUES(?, ?)"
        cursor.execute(sql, data)
        con.commit()
    else:
        print("NO validado") 
 
Button(root, text="Alta", command=lambda:alta(a_val.get(), b_val.get())).grid(row=6, column=1)

root.mainloop()

