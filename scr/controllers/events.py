
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel

import numpy as np
import cv2
import os
from controllers.Model_controller import ModelController
import torch
from PySide2.QtCore import *
from PySide2.QtGui import * 
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
        pixmap_resized = imagePixmap.scaled(320, 280, QtCore.Qt.KeepAspectRatio)
        self.window.label_4.setPixmap(pixmap_resized)
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
    
    def compute_final_results(self):
        """
        Compute the final probability based on the results of the models
        """
        labels = ["normal","viral","covid"]
        self.normal_prob = np.mean(self.probabilities_normal)*100
        self.viral_prob = np.mean(self.probabilities_viral)*100
        self.covid_prob = np.mean(self.probabilities_covid)*100
        list_probabilities = [self.normal_prob, self.viral_prob, self.covid_prob]
        # print(self.normal_prob*100)
        # print(self.viral_prob*100)
        # print(self.covid_prob*100)
        self.final_prediction = labels[np.argmax(list_probabilities)]
        print("Final diagnosis: ",self.final_prediction)
        # print(covid_prob)
        self.display_results()
    def evaluate_selected_models(self):
        """
        Evaluate a list of models
        
        """
        
        # ag_file = "./../views/icons/giphy.gif"
        # self.movie = QMovie(ag_file) 
        # self.movie.setCacheMode(QMovie.CacheAll) 
        # self.movie.setSpeed(100)         
        # self.window.label_5.setMovie(self.movie)
        # self.movie.start()
        self.probabilities_normal = []
        self.probabilities_viral = []
        self.probabilities_covid = []
        self.result_images =[]
        self.diagnosis = []
        # self.model_list = ["Vgg19","InceptionV3","Resnet","Densenet"]
        self.model_list = ["Resnet","Densenet"]
        for model in self.model_list:
            controller = ModelController()
            controller.load_model(model)
            controller.load__transformed_image( self.filename)
            controller.evaluate()
            result,prob_normal,prob_viral,prob_covid = controller.heat_map()
            self.probabilities_normal.append(prob_normal)
            self.probabilities_viral.append(prob_viral)
            self.probabilities_covid.append(prob_covid)
            self.result_images.append(result)
            

        self.compute_final_results()
    
    def display_results(self):
        # self.movie.stop()
        # self.movie.close()
        h,w,z = np.shape(self.result_images[0])
        QResult = QtGui.QImage(self.result_images[0].data, h, w, 3*h, QtGui.QImage.Format_RGB888)  

        self.imagePixmap_result = QtGui.QPixmap.fromImage(QResult)
        self.imagePixmap_result = self.imagePixmap_result.scaled(320, 280, QtCore.Qt.KeepAspectRatio)

        self.window.label_5.setPixmap(self.imagePixmap_result)
        self.window.label_5.setScaledContents(True)  
        self.window.label.setText(str(self.final_prediction))
        self.window.progressBar.setValue(self.normal_prob)
        self.window.progressBar_2.setValue(self.viral_prob)
        self.window.progressBar_3.setValue(self.covid_prob)
        self.popup()
        
    def popup(self):
        if (self.final_prediction == "covid" ):
        # QMessageBox.about(self.window, "AboutBox", "This is about application")
            QMessageBox.warning(self.window, "Warning", "You have a chance of "+str(round(self.covid_prob,2))+'%' 
                                ' of having COVID-19 dissease \n Please communicate with your medical entity ')
        elif(self.final_prediction=="viral"):
            QMessageBox.warning(self.window,"Warning","you have a chance of "+str(round(self.viral_prob,2))+'%'' of having pneumonia \n Please communicate with your medical entity')
        
        elif(self.final_prediction == "normal"):
            QMessageBox.warning(self.window,"Warning","you have a chance of "+str(round(self.normal_prob,2))+'%'' of being OK \n Congratulations')
