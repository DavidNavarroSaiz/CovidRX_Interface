
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
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open image file", r"~/Desktop/","image files(*.jpg *.jpeg *.png)")
        imagePixmap = QtGui.QPixmap.fromImage(filename)
        self.window.label_4.setPixmap(imagePixmap)
        self.window.label_4.setScaledContents(True)  
        # BGR_image = cv2.imread(filename)
        # RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_BGR2RGB)
        # cv2.imshow('image', RGB_image)
        # #waits for user to press any key 
        # #(this is necessary to avoid Python kernel form crashing)
        # cv2.waitKey(0) 
        
        # #closing all open windows 
        # cv2.destroyAllWindows() 
       