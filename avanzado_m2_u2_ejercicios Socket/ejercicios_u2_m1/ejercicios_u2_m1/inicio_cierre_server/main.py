#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

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
import multiprocessing
import binascii
# IMPORTO VISTAS
from src.vistas.ui_interface import *

#VARIABLES GLOBALES
theproc = ""

class Abmc():
    def __init__(self,):
        pass
        self.raiz = Path(__file__).resolve().parent
        self.ruta_bd = os.path.join(self.raiz, 'src', 'bases', 'nivel_avanzado.db')
        self.ruta_server = os.path.join(self.raiz, 'src', 'servidor', 'udp_server_t.py')
 
    def conectar(self,):
        con = sqlite3.connect(self.ruta_bd)
        return con

    def lanzar_servidor(self, var):

        the_path =  self.ruta_server
        if var==True:
            global theproc
            theproc = subprocess.Popen([sys.executable, the_path])
            theproc.communicate()
        else:
            print("")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self,)

 
        # ==================== BASE DE DATOS =================================== 
        self.abmc_object = Abmc()

  
        # =============== TRY CONNECTION  si hago click en botón ===========================
        self.ui.btn_try.clicked.connect(self.try_connection)
        # =============== DETENER SERVIDOR  si hago click en botón ===========================
        self.ui.detener_servidor.clicked.connect(self.stop_server)
        
  
   
    # =================== OPEN SERVER ================================
    def try_connection(self, ): 
        
        self.ui.progressserv.setMinimum(0)
        self.ui.progressserv.setMaximum(500)
        for i in range(214):
            time.sleep(0.01)
            self.ui.progressserv.setValue(i+1)

        if theproc != "":
            theproc.kill()
            threading.Thread(target=self.abmc_object.lanzar_servidor, args=(True,), daemon=True).start()
        else:
            threading.Thread(target=self.abmc_object.lanzar_servidor, args=(True,), daemon=True).start()
        
        for i in range(214, 500):
            time.sleep(0.01)
            self.ui.progressserv.setValue(i+1)
        self.ui.progressserv.setValue(0)    

    # =================== INNIT AND STOP SERVER ====================== 
    def stop_server(self, ):

        self.ui.progress_cerrar.setMinimum(0)
        self.ui.progress_cerrar.setMaximum(500)
        for i in range(214):
            time.sleep(0.01)
            self.ui.progress_cerrar.setValue(i+1)

        global theproc
        if theproc !="":
            theproc.kill() 

        for i in range(214, 500):
            time.sleep(0.01)
            self.ui.progress_cerrar.setValue(i+1)
        self.ui.progress_cerrar.setValue(0) 

 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
        print(len(window.variable_los_thread))
        for i in range(len(window.variable_los_thread)):
            window.variable_los_thread[i] = False
        if theproc!="":
            theproc.kill() 
