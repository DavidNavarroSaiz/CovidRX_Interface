# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameDisplayImage = QtWidgets.QFrame(self.centralwidget)
        self.frameDisplayImage.setGeometry(QtCore.QRect(40, 30, 991, 471))
        self.frameDisplayImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDisplayImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDisplayImage.setObjectName("frameDisplayImage")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frameDisplayImage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 371, 391))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layoutShowImage = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutShowImage.setContentsMargins(0, 0, 0, 0)
        self.layoutShowImage.setObjectName("layoutShowImage")
        self.frame = QtWidgets.QFrame(self.frameDisplayImage)
        self.frame.setGeometry(QtCore.QRect(770, 130, 171, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButtonPlay = QtWidgets.QPushButton(self.frame)
        self.pushButtonPlay.setGeometry(QtCore.QRect(30, 130, 111, 41))
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 151, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frameDisplayImage)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 30, 341, 391))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.layoutShowImage_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layoutShowImage_2.setContentsMargins(0, 9, 0, 0)
        self.layoutShowImage_2.setObjectName("layoutShowImage_2")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(30, 0, 171, 31))
        self.labelLogo.setText("")
        self.labelLogo.setObjectName("labelLogo")
        self.pushload = QtWidgets.QPushButton(self.centralwidget)
        self.pushload.setGeometry(QtCore.QRect(70, 500, 141, 41))
        self.pushload.setObjectName("pushload")
        self.pushButtonCapture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCapture.setGeometry(QtCore.QRect(320, 500, 271, 41))
        self.pushButtonCapture.setObjectName("pushButtonCapture")
        self.labelLogoFlir = QtWidgets.QLabel(self.centralwidget)
        self.labelLogoFlir.setGeometry(QtCore.QRect(240, 0, 111, 31))
        self.labelLogoFlir.setText("")
        self.labelLogoFlir.setObjectName("labelLogoFlir")
        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setGeometry(QtCore.QRect(830, 500, 141, 41))
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonPlay.setText(_translate("MainWindow", "Save HeatMap"))
        self.label_3.setText(_translate("MainWindow", "RESULT"))
        self.pushload.setText(_translate("MainWindow", "Load Image"))
        self.pushButtonCapture.setText(_translate("MainWindow", "Run diagnosis"))
        self.pushButtonLoad.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
