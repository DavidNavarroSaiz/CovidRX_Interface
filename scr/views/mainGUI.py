from PySide2.QtWidgets import QApplication,QWidget,QFileDialog 
from PySide2.QtGui import QIcon , QPixmap 
from PySide2 import QtCore
from PySide2 import QtUiTools
import sys
from PySide2 import QtWidgets

# To convert a ui file to a .py using pyside2
# pyside2-uic gui_designer.ui -o gui_designer_ui.py
class MainWindow(QtWidgets.QMainWindow):
        
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        
        file = QtCore.QFile("./views/gui_designer.ui")
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader(file)
        self.window = loader.load(file)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)
        self.setWindowTitle("Covid RX detection")
        # self.setGeometry(300, 100, 1012, 622)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.window.show()
    app.exec_()

    
if __name__ == "__main__":
    main()









# myApp = QApplication(sys.argv)
# window = Window()
# window.show()
# myApp.exec_()
# sys.exit(0)