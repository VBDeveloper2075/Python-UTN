from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import ttk

import os
import sys
# ===========================================================
from pathlib import Path
import sqlite3
import subprocess
import threading
import time
import datetime
import socket
import secrets
import pprint
import binascii


theproc=""

class Ventanita:
    def __init__(self, window):
        self.root = window
        self.root.title("Tarea POO")

        #PASO 1 - AGREGO RUTA A SERVIDOR
        self.raiz = Path(__file__).resolve().parent
        self.ruta_server = os.path.join(self.raiz, 'src', 'servidor', 'udp_server_t.py')
    
        self.titulo = Label(self.root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w")



        self.boton_alta=Button(self.root, text="Prender", command=lambda:self.try_connection())
        self.boton_alta.grid(row=6, column=1)

        self.boton_borrar=Button(self.root, text="Apagar", command=lambda:self.stop_server())
        self.boton_borrar.grid(row=6, column=3)

    def prender(self,):
        print("prender")

    def try_connection(self, ): 

        if theproc != "":
            theproc.kill()
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        else:
            threading.Thread(target=self.lanzar_servidor, args=(True,), daemon=True).start()
        
    def lanzar_servidor(self, var):

        the_path =  self.ruta_server
        if var==True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()
        else:
            print("")

    # =================== INNIT AND STOP SERVER ====================== 
    def stop_server(self, ):

        global theproc
        if theproc !="":
            theproc.kill() 

 