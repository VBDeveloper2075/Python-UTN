#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core

# ===========================================================

from ui_mainwind import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(
            self,
        )
        self.ui = Ui_MainWindow()
        self.ui.setupUi(
            self,
        )

        # ===============  ===========================
        self.ui.btn_try.clicked.connect(self.try_connection)

    # =================== TRY CONNECTION =============================
    def try_connection(
        self,
    ):
        print("dddd")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.setWindowTitle("PRUEBA")
    window.setFixedWidth(1290)
    window.setFixedHeight(650)
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")
