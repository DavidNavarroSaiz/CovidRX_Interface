# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_designer.ui'
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
        MainWindow.resize(1012, 622)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frameDisplayImage = QFrame(self.centralwidget)
        self.frameDisplayImage.setObjectName(u"frameDisplayImage")
        self.frameDisplayImage.setGeometry(QRect(10, 20, 1021, 481))
        self.frameDisplayImage.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayImage.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frameDisplayImage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(810, 130, 171, 221))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.SaveButton = QPushButton(self.frame)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setGeometry(QRect(30, 130, 111, 41))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 20, 71, 20))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 161, 31))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frameDisplayImage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 40, 371, 381))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.frameDisplayImage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 40, 371, 381))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(30, 0, 171, 31))
        self.pushload = QPushButton(self.centralwidget)
        self.pushload.setObjectName(u"pushload")
        self.pushload.setEnabled(True)
        self.pushload.setGeometry(QRect(70, 500, 171, 41))
        self.pushload.setFlat(False)
        self.pushButtonRun = QPushButton(self.centralwidget)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        self.pushButtonRun.setGeometry(QRect(370, 500, 221, 41))
        self.labelLogoFlir = QLabel(self.centralwidget)
        self.labelLogoFlir.setObjectName(u"labelLogoFlir")
        self.labelLogoFlir.setGeometry(QRect(240, 0, 111, 31))
        self.HelpButton = QPushButton(self.centralwidget)
        self.HelpButton.setObjectName(u"HelpButton")
        self.HelpButton.setGeometry(QRect(900, 500, 91, 31))
        self.settings = QPushButton(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(780, 500, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushload.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"Save HeatMap", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RESULT", None))
        self.label.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.labelLogo.setText("")
        self.pushload.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.pushButtonRun.setText(QCoreApplication.translate("MainWindow", u"Run diagnosis", None))
        self.labelLogoFlir.setText("")
        self.HelpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

