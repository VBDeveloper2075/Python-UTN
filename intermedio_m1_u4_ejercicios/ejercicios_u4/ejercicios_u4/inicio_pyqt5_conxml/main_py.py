import sys
from PyQt5 import QtWidgets
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

# IMPORTO VISTAS
from ui_mainwind import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(
        self,
    ):
        # ========== DESDE .PY ======================= pyuic5 nombre.ui -o nombre.py
        QtWidgets.QMainWindow.__init__(
            self,
        )
        Ui_MainWindow.__init__(
            self,
        )
        self.setupUi(
            self,
        )

        # ===============  ===========================
        self.btn_try.clicked.connect(self.try_connection)

    # =================== TRY CONNECTION =============================
    def try_connection(
        self,
    ):
        print("dddd")


if __name__ == "__main__":
    dirname = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dirname, "plugins", "platforms")
    QtWidgets.QApplication.addLibraryPath(plugin_path)

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle("PRUEBA")
    widget.setFixedWidth(1290)
    widget.setFixedHeight(650)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")
