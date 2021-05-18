from views.gui_designer_ui import *
from PySide2.QtWidgets import QApplication,QWidget,QFileDialog 
from PySide2.QtGui import QIcon , QPixmap 
import sys
from PySide2 import QtWidgets
# To convert a ui file to a .py using pyside2
# pyside2-uic gui_designer.ui -o gui_designer_ui.py
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
#


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()









# myApp = QApplication(sys.argv)
# window = Window()
# window.show()
# myApp.exec_()
# sys.exit(0)