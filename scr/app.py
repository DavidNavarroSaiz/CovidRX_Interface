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
    window.show()
    app.exec_()











# if (__name__ == '__main__'):

#     path_image = 'resources/images/test/COVID/COVID (13).png'
#     path_model = 'resources/saved_models/vgg19.pt'
#     controller = ModelController()
#     controller.load__transformed_image(path_image)
#     controller.load_model(path_model)
#     controller.evaluate()
#     controller.heat_map()
