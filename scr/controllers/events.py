
from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
from controllers.Model_controller import ModelController
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
        self.window.pushButtonRun.clicked.connect(self.evaluate_image)
    def load_image(self):
        """
        Load and display the coresponding image

        """
        self.filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open image file", r"~/Desktop/","image files(*.jpg *.jpeg *.png)")
        imagePixmap = QtGui.QPixmap.fromImage( self.filename)
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
    def evaluate_image(self):
        
        """
        Evaluate the image using CNN

        """
                       
        path_model = "resources/saved_models/vgg19.pt"
        controller = ModelController()
        controller.load__transformed_image( self.filename)
        controller.load_model(path_model)
        controller.evaluate()
        result,prediction = controller.heat_map()
        h,w,z = np.shape(result)
        print(np.shape(result))
        QResult = QtGui.QImage(result.data, h, w, 3*h, QtGui.QImage.Format_RGB888)  
        imagePixmap_result = QtGui.QPixmap.fromImage(QResult)
        self.window.label_5.setPixmap(imagePixmap_result)
        self.window.label_5.setScaledContents(True)  
        self.window.label.setText(str(prediction))