from controllers.Model_controller import ModelController
from PySide2 import QtWidgets, QtGui
import sys
import os

"""
Añadir directorios al path del proyecto
"""

#xdirs = ['views', 'controllers', 'acquisition']
#x
#xfor nameDir in dirs:
#x    path = os.path.join(sys.path[0], nameDir)
#x    sys.path.append(path)

"""
Importar librerias principales
"""

from views.mainGUI import MainWindow
from controllers.events import Events


"""
Correr la aplicación
"""
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    controller = Events(window)
    # window.window.show()
    sys.exit(app.exec_())
    # app.exit()
