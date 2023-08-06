# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceOiPEcc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1175, 595)
        MainWindow.setMinimumSize(QSize(0, 400))
        font = QFont()
        font.setFamily(u"Noto Sans Mono Light")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	border: none;\n"
"	color: #fff;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgba(14, 14, 22, 100);\n"
"	border: 2px solid rgb(24, 24, 36);\n"
"	border-radius: 5px;\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(24, 24, 36);\n"
"	text-align: left;\n"
"}\n"
"#footer{	\n"
"	background-color: rgb(9, 5, 13);\n"
"	padding: 10px;\n"
"}\n"
"#messages_widget,\n"
"#menu_widget,\n"
"#right_menu,\n"
"#search_widget,\n"
"#notifications_widget,\n"
"#bottom_menu,\n"
"#login_widget,\n"
"#header_search_widget{	\n"
"	background-color: rgb(9, 5, 13);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setStyleSheet(u"QPushButton, QLineEdit{\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit{\n"
"	border-bottom:  2px solid rgb(24, 24, 36);\n"
"}\n"
"background-color: rgb(114, 159, 207);")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.main_body_contents)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.right_menu = QCustomSlideMenu(self.frame_14)
        self.right_menu.setObjectName(u"right_menu")
        self.verticalLayout_21 = QVBoxLayout(self.right_menu)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.right_menu)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 300))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.section1 = QCustomSlideMenu(self.frame_13)
        self.section1.setObjectName(u"section1")
        self.section1.setMinimumSize(QSize(0, 250))
        self.section1.setMaximumSize(QSize(16777215, 200))
        self.section1.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.section1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_8 = QFrame(self.section1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 130))
        self.frame_8.setMaximumSize(QSize(350, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.frame_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 100))
        self.groupBox_4.setMaximumSize(QSize(300, 70))
        self.groupBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.groupBox_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_try = QPushButton(self.frame_10)
        self.btn_try.setObjectName(u"btn_try")
        self.btn_try.setMinimumSize(QSize(60, 25))
        self.btn_try.setMaximumSize(QSize(60, 30))
        self.btn_try.setStyleSheet(u"border-color: rgb(49, 168, 255);")

        self.horizontalLayout_17.addWidget(self.btn_try)

        self.progressserv = QProgressBar(self.frame_10)
        self.progressserv.setObjectName(u"progressserv")
        self.progressserv.setMinimumSize(QSize(0, 25))
        self.progressserv.setValue(0)

        self.horizontalLayout_17.addWidget(self.progressserv)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_16 = QFrame(self.groupBox_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.detener_servidor = QPushButton(self.frame_16)
        self.detener_servidor.setObjectName(u"detener_servidor")
        self.detener_servidor.setMinimumSize(QSize(60, 25))
        self.detener_servidor.setMaximumSize(QSize(60, 30))
        self.detener_servidor.setStyleSheet(u"border-color: rgb(49, 168, 255);")

        self.horizontalLayout_16.addWidget(self.detener_servidor)

        self.progress_cerrar = QProgressBar(self.frame_16)
        self.progress_cerrar.setObjectName(u"progress_cerrar")
        self.progress_cerrar.setMinimumSize(QSize(0, 25))
        self.progress_cerrar.setValue(0)

        self.horizontalLayout_16.addWidget(self.progress_cerrar)


        self.verticalLayout_6.addWidget(self.frame_16)


        self.verticalLayout_3.addWidget(self.groupBox_4)


        self.horizontalLayout_15.addWidget(self.frame_8)


        self.horizontalLayout_20.addWidget(self.section1)


        self.verticalLayout_21.addWidget(self.frame_13)


        self.horizontalLayout_10.addWidget(self.right_menu)


        self.verticalLayout_11.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.main_body_contents)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Server", None))
        self.btn_try.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.detener_servidor.setText(QCoreApplication.translate("MainWindow", u"Stop ", None))
    # retranslateUi

