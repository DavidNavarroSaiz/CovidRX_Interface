
from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2

class Events():
    """
    Set the respective events for the buttons

    """

    def __init__(self, mainWidget):
        self.window = mainWidget
        self.connectButtons()


    def connectButtons(self):
        """
        Connect each button with is respective event
        """
        self.window.pushload.clicked.connect(self.load_image)
        # self.window.pushButtonLoad.clicked.connect(self.load_image)

    def load_image(self):
        """
        Load and display the coresponding image

        """
        label = QtWidgets.QLabel("hello")
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open image file", r"C:\\Users\\David\\Desktop\\COVID-RX","image files(*.jpg *.jpeg *.png)")
        # img = QtGui.QImage(filename)
        imagePixmap = QtGui.QPixmap.fromImage(filename)
        # self.window.label_2.setPixmap(imagePixmap)
        label.setPixmap(imagePixmap)
        self.window.Layout_image.addWidget(self.window,label)
        # BGR_image = cv2.imread(filename)
        # RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2RGB)
        # cv2.imshow('image', RGB_image)
        # #waits for user to press any key 
        # #(this is necessary to avoid Python kernel form crashing)
        # cv2.waitKey(0) 
        
        # #closing all open windows 
        # cv2.destroyAllWindows() 
        ## leer image con CV2
        ##utilizar el metodo de abajo para convertir en widget y ya no necesito la linea de arriba

        # image_widget = self.imageToQtWidget(RGB_image)
        # # pixmap=QtGui.QPixmap(img)

        # self.window.layoutShowImage.addWidget(image_widget)
        # self.window.Layout_image.addWidget(image_widget)
        # self.window.layoutShowImage.  
   

    def imageToQtWidget(self, image):
        """
        Transforma una imagen a un widget de QT
        parameter:
            frame: frame de la imagen a transformar
        """
        self.dimensionsImage= np.shape(image)
        w,h,z= np.shape(image)
        print("Dimensiones",w,h,z)
        # frame = self.imageResize(frame, self.scalaImage)
        image = QtGui.QImage(image, *self.dimensionsImage, QtGui.QImage.Format_RGB888).rgbSwapped()
        print(type(image),"Tipo de archivo")
        imagePixmap = QtGui.QPixmap.fromImage(image)
        viewCamera = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene()
        imagePixmap = QtGui.QPixmap(w,h)
        imagePixmapItem = scene.addPixmap(imagePixmap)
        viewCamera.setScene(scene)
        return viewCamera
        