from views.gui_designer_ui import *
from PySide2.QtWidgets import QApplication,QWidget,QFileDialog 
from PySide2.QtGui import QIcon , QPixmap 
import sys
from PySide2 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
# from PySide2 import QtCore, QtUiTools, QtWidgets, QtGui
# # from views.acqGUI import Ui_MainWindow
# # from views.style import Styles
# import cv2
# import sys
# import os

# class MainWindow(QtWidgets.QMainWindow):
#     """
#     Main QTWidget para la adquisicion de la cámara FLIR
#     """    

#     def __init__(self, *args, **kwargs):
#         """
#         Inicializa la clase FlirCameraWidget
#         """

#         super(MainWindow, self).__init__(*args, **kwargs)
#         #self.loadForm()
#         self.loadForm()
#         # self.window.setupUi(self)

#         self.initUI()
#         # Styles(self)

#     def initUI(self):
#         """
#         Setea los valores iniciales de la GUI
#         """
        
#         self.setWindowTitle("Intecol Flir camera")
#         self.setGeometry(300, 100, 1012, 622)

#     def loadForm(self):
#         """
#         Carga el archivo .ui de la GUI
#         """

#         formUI = os.path.join(sys.path[0], 'views/gui_prueba.ui')
#         print(sys.path[0])
#         file = QtCore.QFile(formUI)
#         file.open(QtCore.QFile.ReadOnly)
#         loader = QtUiTools.QUiLoader()
#         self.window = loader.load(file)
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.window)
#         self.setLayout(layout)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()








# class Window (QWidget):

#     def __init__ (self):
#         super().__init__()

#         self.setWindowTitle("Covid app")
#         self.setGeometry(450,50,800,600)
#         self.setMinimumHeight(100)
#         self.setMinimumWidth(100)
#         self.setMaximumHeight(1200)
#         self.setMaximumWidth(1200)
#         self.setIcon()
#     def setIcon(self):
#         appIcon = QIcon('icons/icon.png')
#         self.setWindowIcon(appIcon)





# myApp = QApplication(sys.argv)
# window = Window()
# window.show()
# myApp.exec_()
# sys.exit(0)