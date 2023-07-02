# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwind.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1299, 671)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1291, 631))
        self.widget.setStyleSheet(u" QWidget#widget{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.0150273, y1:0.108, x2:0.955, y2:0.852591, stop:0 rgba(1, 17, 165, 255), stop:0.97037 rgba(1, 17, 250, 255));}")
        self.btn_try = QPushButton(self.widget)
        self.btn_try.setObjectName(u"btn_try")
        self.btn_try.setGeometry(QRect(210, 10, 151, 30))
        self.btn_try.setStyleSheet(u"font-size:16px;\n"
"background-color: #FACB1B;")
        self.prueba = QPushButton(self.widget)
        self.prueba.setObjectName(u"prueba")
        self.prueba.setGeometry(QRect(150, 310, 321, 51))
        self.prueba.setStyleSheet(u"font-size:20px;\n"
"background-color:#D90728;")
        self.add_signal = QPushButton(self.centralwidget)
        self.add_signal.setObjectName(u"add_signal")
        self.add_signal.setGeometry(QRect(490, 680, 75, 23))
        self.local_port = QLabel(self.centralwidget)
        self.local_port.setObjectName(u"local_port")
        self.local_port.setGeometry(QRect(610, 680, 100, 30))
        self.local_port.setStyleSheet(u"font-size: 16px;\n"
"color:#fff;")
        self.local_port_contenido = QLabel(self.centralwidget)
        self.local_port_contenido.setObjectName(u"local_port_contenido")
        self.local_port_contenido.setGeometry(QRect(710, 670, 150, 30))
        self.local_port_contenido.setStyleSheet(u"font-size: 16px;\n"
"color:yellow;")
        self.ecu_port = QLabel(self.centralwidget)
        self.ecu_port.setObjectName(u"ecu_port")
        self.ecu_port.setGeometry(QRect(610, 710, 80, 30))
        self.ecu_port.setStyleSheet(u"font-size: 16px;\n"
"color:#fff;")
        self.ecu_port_contenido = QLabel(self.centralwidget)
        self.ecu_port_contenido.setObjectName(u"ecu_port_contenido")
        self.ecu_port_contenido.setGeometry(QRect(700, 700, 150, 30))
        self.ecu_port_contenido.setStyleSheet(u"font-size: 16px;\n"
"color:yellow;")
        self.esmart_por = QLabel(self.centralwidget)
        self.esmart_por.setObjectName(u"esmart_por")
        self.esmart_por.setGeometry(QRect(600, 740, 120, 30))
        self.esmart_por.setStyleSheet(u"font-size: 16px;\n"
"color:#fff;")
        self.esmart_port_contenido = QLabel(self.centralwidget)
        self.esmart_port_contenido.setObjectName(u"esmart_port_contenido")
        self.esmart_port_contenido.setGeometry(QRect(750, 730, 150, 30))
        self.esmart_port_contenido.setStyleSheet(u"font-size: 16px;\n"
"color:yellow;")
        self.local_ip = QLabel(self.centralwidget)
        self.local_ip.setObjectName(u"local_ip")
        self.local_ip.setGeometry(QRect(20, 680, 80, 30))
        self.local_ip.setStyleSheet(u"font-size: 16px;\n"
"color:#fff;")
        self.local_ip_contenido = QLabel(self.centralwidget)
        self.local_ip_contenido.setObjectName(u"local_ip_contenido")
        self.local_ip_contenido.setGeometry(QRect(110, 680, 450, 30))
        self.local_ip_contenido.setStyleSheet(u"font-size: 16px;\n"
"color:yellow;")
        self.detected_local = QLabel(self.centralwidget)
        self.detected_local.setObjectName(u"detected_local")
        self.detected_local.setGeometry(QRect(20, 710, 51, 40))
        self.detected_local.setStyleSheet(u"font-size: 20px;\n"
"color:#fff;")
        self.local_icon = QPushButton(self.centralwidget)
        self.local_icon.setObjectName(u"local_icon")
        self.local_icon.setGeometry(QRect(100, 710, 40, 40))
        self.local_icon.setStyleSheet(u"background-color:rgba(1, 17, 165, 255);")
        self.detected_ecu = QLabel(self.centralwidget)
        self.detected_ecu.setObjectName(u"detected_ecu")
        self.detected_ecu.setGeometry(QRect(140, 710, 40, 40))
        self.detected_ecu.setStyleSheet(u"font-size: 20px;\n"
"color:#fff;")
        self.detected_esmart = QLabel(self.centralwidget)
        self.detected_esmart.setObjectName(u"detected_esmart")
        self.detected_esmart.setGeometry(QRect(230, 710, 71, 40))
        self.detected_esmart.setStyleSheet(u"font-size: 20px;\n"
"color:#fff;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1299, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BACHET Tool", None))
        self.btn_try.setText(QCoreApplication.translate("MainWindow", u"try / Start Server", None))
        self.prueba.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.add_signal.setText(QCoreApplication.translate("MainWindow", u"Add Signal", None))
        self.local_port.setText(QCoreApplication.translate("MainWindow", u"Local Port:", None))
        self.local_port_contenido.setText(QCoreApplication.translate("MainWindow", u"-------------------------------------------------------------", None))
        self.ecu_port.setText(QCoreApplication.translate("MainWindow", u"ecu Port:", None))
        self.ecu_port_contenido.setText(QCoreApplication.translate("MainWindow", u"-------------------------------------------------------------", None))
        self.esmart_por.setText(QCoreApplication.translate("MainWindow", u"eSmart Port:", None))
        self.esmart_port_contenido.setText(QCoreApplication.translate("MainWindow", u"-------------------------------------------------------------", None))
        self.local_ip.setText(QCoreApplication.translate("MainWindow", u"Local Ip: ", None))
        self.local_ip_contenido.setText(QCoreApplication.translate("MainWindow", u"-------------------------------------------------------------", None))
        self.detected_local.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.local_icon.setText("")
        self.detected_ecu.setText(QCoreApplication.translate("MainWindow", u"ECU", None))
        self.detected_esmart.setText(QCoreApplication.translate("MainWindow", u"eSmart", None))
    # retranslateUi

