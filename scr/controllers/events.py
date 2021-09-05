
from PySide2 import QtGui, QtWidgets, QtCore
import numpy as np
import cv2
import os
from controllers.Model_controller import ModelController
class Events():
    """
    Set the respective events for the buttons

    """

    def __init__(self, mainWindow):
        self.window = mainWindow.window
        self.connectButtons()


    def connectButtons(self):
        """
        Connect each button with is respective event
        """
        self.window.pushload.clicked.connect(self.load_image)
        # self.window.pushButtonLoad.clicked.connect(self.load_image)
        self.window.pushButtonRun.clicked.connect(self.evaluate_selected_models)
        self.window.SaveButton.clicked.connect(self.save_image)
        
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
        a = os.path.abspath('')               
        # path_model = a+"\\scr\\resources\\saved_models\\vgg19.pt"
        
        controller = ModelController()
        controller.load_model("Rexnet")
        controller.load__transformed_image( self.filename)
        
        controller.evaluate()
        result,prediction,proba = controller.heat_map()
        h,w,z = np.shape(result)
        
        
        QResult = QtGui.QImage(result.data, h, w, 3*h, QtGui.QImage.Format_RGB888)  
        self.imagePixmap_result = QtGui.QPixmap.fromImage(QResult)
        self.window.label_5.setPixmap(self.imagePixmap_result)
        self.window.label_5.setScaledContents(True)  
        self.window.label.setText(str(prediction))

    def save_image(self):
        self.filename,_ = QtWidgets.QFileDialog.getSaveFileName(None,"Save image file", "image.png","image files(*.jpg *.jpeg *.png)")
        self.imagePixmap_result.save(self.filename)
    
    
    def evaluate_selected_models(self):
        """
        Evaluate a list of models
        
        """
        probabilities = []
        result_images =[]
        diagnosis = []
        model_list = ["Vgg19","Densenet"]
        for model in model_list:
            controller = ModelController()
            controller.load_model(model)
            controller.load__transformed_image( self.filename)
            controller.evaluate()
            result,prediction,proba = controller.heat_map()
            h,w,z = np.shape(result)
            probabilities.append(proba)
            result_images.append(result)
            diagnosis.append(prediction)
            QResult = QtGui.QImage(result_images[0].data, h, w, 3*h, QtGui.QImage.Format_RGB888)  
            self.imagePixmap_result = QtGui.QPixmap.fromImage(QResult)
            self.window.label_5.setPixmap(self.imagePixmap_result)
            self.window.label_5.setScaledContents(True)  
            self.window.label.setText(str(diagnosis[-1]))
            print(probabilities)
        