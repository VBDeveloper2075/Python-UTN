from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter as tk
import sqlite3
import os

# from PIL import ImageTk, Image
import re

# --------------------------CREAR BASE DE DATOS--------------------------#


def conexion():
    con = sqlite3.connect("baseDeDatos.db")
    return con


# --------------------------CREAR TABLA----------------------------------#


def crear_tabla(con):
    cursor = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS pacientes (id integer PRIMARY KEY AUTOINCREMENT, paciente text, especialidad text, dia text, hora text, obra_social text)"
    cursor.execute(sql)
    print("asdsadsdd")
    con.commit()
