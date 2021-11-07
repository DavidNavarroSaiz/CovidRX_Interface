
from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel
import numpy as np
import cv2, os, pathlib, time, torch
from controllers.Model_controller import ModelController
from PySide2.QtCore import *
from PySide2.QtGui import * 
from torchcam.utils import overlay_mask
from torchvision.transforms.functional import normalize, resize, to_pil_image
import torch.nn.functional as F
from collections import Counter
from scipy.stats import mode
from scipy import stats
class Loading():
    def __init__(self, label):
        super().__init__()
        # self.label = QLabel()
        self.label = label
        dir_path = pathlib.Path(__file__).parent.parent.resolve().as_posix()
        image = dir_path + "/views/icons/giphy2.gif"
        self.movie = QMovie(image)
        self.label.setScaledContents(True)
        self.label.setMovie(self.movie)

    def start(self):
        self.movie.start()
        # self.show()
    
    def stop(self):
        self.movie.stop()
        self.close()




class Events():
    """
    Set the respective events for the buttons

    """
    
    def __init__(self, mainWindow):
        self.window = mainWindow.window
        self.initialize_butttons()
        self.connectButtons()
        mainWindow.show()
    def initialize_butttons(self):
        self.window.pushload.setEnabled(True)
        self.window.pushButtonRun.setEnabled(False)
        self.window.SaveButton.setEnabled(False)
        
        
    def connectButtons(self):
        """
        Connect each button with is respective event
        """
        self.window.pushload.clicked.connect(self.load_image)
        # self.window.pushButtonRun.pressed.connect(self.loading)
        self.window.pushButtonRun.released.connect(self.run)
        self.window.SaveButton.clicked.connect(self.save_image)

    def load_image(self):
        """
        Load and display the coresponding image

        """
        try:
            self.filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open image file", r"~/Desktop/","image files(*.jpg *.jpeg *.png)")
            imagePixmap = QtGui.QPixmap.fromImage( self.filename)
            pixmap_resized = imagePixmap.scaled(320, 280, QtCore.Qt.KeepAspectRatio)
            self.window.label_4.setPixmap(pixmap_resized)
            self.window.label_4.setScaledContents(True)
            self.window.pushButtonRun.setEnabled(True)
            self.pixmap_ok  =QtGui.QPixmap('./views/icons/done.png')
            self.ok_resized = self.pixmap_ok.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
            self.window.done_load.setPixmap(self.ok_resized)
        except:
            QMessageBox.about(None,"Error",'Error Loading Image')

    


    def save_image(self):
        try:
            self.filename,_ = QtWidgets.QFileDialog.getSaveFileName(None,"Save image file", "image.png","image files(*.jpg *.jpeg *.png)")
            self.window.label_5.pixmap().save(self.filename)
            self.window.done_saved.setPixmap(self.ok_resized)
        except:
            QMessageBox.about(None,"Error",'Error Saving the Image')

    def popup(self):
        try:
            self.final_prediction = self.window.FinalPrediction.objectName()
            if (self.final_prediction == "covid" ):
            # QMessageBox.about(self.window, "AboutBox", "This is about application")
                QMessageBox.warning(None, "Warning", "You have a chance of "+str(round(self.window.progressBar_3.value(),2))+'%' 
                                    ' of having COVID-19 dissease \n Please communicate with your medical entity ')
            elif(self.final_prediction=="viral"):
                QMessageBox.warning(None,"Warning","you have a chance of "+str(round(self.window.progressBar_2.value(),2))+'%'' of having pneumonia \n Please communicate with your medical entity')
            
            elif(self.final_prediction == "normal"):
                QMessageBox.warning(None,"Warning","you have a chance of "+str(round(self.window.progressBar.value(),2))+'%'' of being OK \n Congratulations')
        except:
            QMessageBox.about(None,"Error","Error showing results - PopUp")
    def loading(self):
        # dir_path = pathlib.Path(__file__).parent.parent.resolve().as_posix()
        # image = dir_path + "/views/icons/loading.png"
        # self.window.label_5.setPixmap(image)
        loading = Loading(self.window.label_5)
        loading.start()
        print("displayed image")

    def activate_run(self):
        
        
        statement = (
            self.window.actionVgg19.isChecked() | self.window.actionDenseNet.isChecked() | self.window.actionMobileNet.isChecked() |
            self.window.actionAlexNet.isChecked() | self.window.actionEfficientNet.isChecked() | self.window.actionInceptionV3.isChecked() |
            self.window.actionResNet_2.isChecked() | self.window.actionRexNet.isChecked() | self.window.actionInception_ResNet.isChecked() |
            self.window.actionXception.isChecked()
        )
        
        
        self.window.pushButtonRun.setEnabled(True) if statement else self.window.pushButtonRun.setEnabled(False)
        self.window.pushButtonRun.setText("Run diagnosis") if statement else self.window.pushButtonRun.setText("Select Models on the top Menu")

#
    # def threads(self):
    #     thread = Processing(self.window)
    #     thread.start()
    #     i=0
    #     while(thread.isRunning()):
    #         i+=1
    #         print('corriendo'+'.'*i, end = '\r')
    #         time.sleep(1)
    #     print("Finalizado!")
    #     self.popup()
# class Processing(QThread):
    # def __init__(self,window):
    #     super().__init__()
    #     self.window = window
# #   

        
    def run(self):
        """
        Evaluate a list of models
        
        """

        self.probabilities_normal = []
        self.probabilities_viral = []
        self.probabilities_covid = []
        self.result_ActivationMap =[]
        self.diagnosis = []
        self.model_list = []
        statement = (
            self.window.actionVgg19.isChecked() | self.window.actionDenseNet.isChecked() | self.window.actionMobileNet.isChecked() |
            self.window.actionAlexNet.isChecked() | self.window.actionEfficientNet.isChecked() | self.window.actionInceptionV3.isChecked() |
            self.window.actionResNet_2.isChecked() | self.window.actionRexNet.isChecked() | self.window.actionInception_ResNet.isChecked() |
            self.window.actionXception.isChecked())
        
        if statement :
            try:
                if self.window.actionVgg19.isChecked(): self.model_list.append("Vgg19")
                if self.window.actionDenseNet.isChecked(): self.model_list.append("DenseNet")
                if self.window.actionMobileNet.isChecked(): self.model_list.append("MobileNet")
                if self.window.actionAlexNet.isChecked(): self.model_list.append("AlexNet")
                if self.window.actionEfficientNet.isChecked(): self.model_list.append("EfficientNet")
                if self.window.actionInceptionV3.isChecked(): self.model_list.append("InceptionV3")
                if self.window.actionResNet_2.isChecked(): self.model_list.append("ResNet")
                if self.window.actionInception_ResNet.isChecked(): self.model_list.append("Inception_ResNet")
                if self.window.actionXception.isChecked(): self.model_list.append("Xception")
                model_counter = 0

                for model in self.model_list:
                    print("Evaluating model: ",self.model_list[model_counter])
                    controller = ModelController()
                    controller.load_model(model)
                    controller.load__transformed_image( self.filename)
                    controller.evaluate()
                    self.rgbimage,result_actmap,prob_normal,prob_viral,prob_covid = controller.heat_map()
                    
                    self.probabilities_normal.append(prob_normal)
                    self.probabilities_viral.append(prob_viral)
                    self.probabilities_covid.append(prob_covid)
                    if (result_actmap.shape[0]< 7):
                        padding = np.pad(result_actmap, ((7-result_actmap.shape[0], 0), (7-result_actmap.shape[0], 0)), 'constant', constant_values=(0, 0))
                        result_actmap  =padding
                    elif(result_actmap.shape[0]> 7):
                        result_actmap = result_actmap[1:8, 1:8]
                    else:
                        result_actmap = result_actmap
                    result_actmap = result_actmap[0:7, 0:7]
                    result_actmap = np.pad(result_actmap, ((2, 2), (2, 2)), 'constant', constant_values=(0.3, 0.3))
                    if model_counter == 0 :
                        self.result_ActivationMap= result_actmap 
                    else:
                        self.result_ActivationMap= result_actmap + self.result_ActivationMap

                    
                    model_counter += 1
                self.FinalActivationMap = (self.result_ActivationMap / len(self.model_list))*(1.5+len(self.model_list)/8)
                res = stats.mode(self.FinalActivationMap.ravel())[0][0]
                self.FinalActivationMap = (self.FinalActivationMap>res)*self.FinalActivationMap

                self.compute_final_results()
            except:
                QMessageBox.about(None,"Error","Error Computing results" )
        else:
            QMessageBox.about(None,"Error",'Please Choose a model to evaluate the chest Xray image')

    def compute_final_results(self):
        """
        Compute the final probability based on the results of the models
        """
        try: 
            labels = ["normal","viral","covid"]
            self.normal_prob = np.mean(self.probabilities_normal)*100
            self.viral_prob = np.mean(self.probabilities_viral)*100
            self.covid_prob = np.mean(self.probabilities_covid)*100
            list_probabilities = [self.normal_prob, self.viral_prob, self.covid_prob]

            self.final_prediction = labels[np.argmax(list_probabilities)]
            self.window.FinalPrediction.setObjectName(self.final_prediction) 
            print("Final diagnosis: ",self.final_prediction)
            self.window.SaveButton.setEnabled(True)
            self.display_results()
        except:
            QMessageBox.about(None,"Error","Error Calculating final results")
    
    
    def display_results(self):
        try: 
            result = overlay_mask(to_pil_image(self.rgbimage), to_pil_image(self.FinalActivationMap, mode='F'), alpha=0.7)
            self.img_result = np.array(result)

            h,w,z = np.shape(self.img_result)
            QResult = QtGui.QImage(self.img_result.data, h, w, 3*h, QtGui.QImage.Format_RGB888)  

            self.imagePixmap_result = QtGui.QPixmap.fromImage(QResult)
            self.imagePixmap_result = self.imagePixmap_result.scaled(320, 280, QtCore.Qt.KeepAspectRatio)

            self.window.label_5.setPixmap(self.imagePixmap_result)
            self.window.label_5.setScaledContents(True)  
            
            DEFAULT_STYLE = """
            QProgressBar{
                border: 2px solid grey;
                text-align: center
            }

            QProgressBar::chunk {
                background-color: #5DE43F;
                width: 10px;
                
                margin: 1px;
            }
            """
            warning_STYLE = """
            QProgressBar{
                border: 2px solid grey;
                text-align: center
            }

            QProgressBar::chunk {
                background-color: #FEC02F;
                width: 10px;
                margin: 1px;
            }
            """
            danger_STYLE = """
            QProgressBar{
                border: 2px solid grey;
                text-align: center
            }

            QProgressBar::chunk {
                background-color: #FC3131;
                width: 10px;
                margin: 1px;
            }
            """
            if (self.normal_prob<33): 
                self.window.progressBar.setStyleSheet(DEFAULT_STYLE) 
            elif (self.normal_prob>33 and self.normal_prob<66):
                self.window.progressBar.setStyleSheet(warning_STYLE) 
            else:
                self.window.progressBar.setStyleSheet(danger_STYLE) 
                
            if (self.viral_prob<33): 
                self.window.progressBar_2.setStyleSheet(DEFAULT_STYLE) 
            elif (self.viral_prob>33 and self.viral_prob<66):
                self.window.progressBar_2.setStyleSheet(warning_STYLE) 
            else:
                self.window.progressBar_2.setStyleSheet(danger_STYLE) 
                
            if (self.covid_prob<33): 
                self.window.progressBar_3.setStyleSheet(DEFAULT_STYLE) 
            elif (self.covid_prob>33 and self.covid_prob<66):
                self.window.progressBar_3.setStyleSheet(warning_STYLE) 
            else:
                self.window.progressBar_3.setStyleSheet(danger_STYLE) 
                
                
                
                
            self.window.progressBar.setValue(self.normal_prob)
            self.window.progressBar_2.setValue(self.viral_prob)
            self.window.progressBar_3.setValue(self.covid_prob)
            # cv2.imshow('ImageWindow', self.rgbimage)
            # cv2.waitKey()
            # pixmap_ok  =QtGui.QPixmap('./views/icons/done.png')
            # ok_resized = pixmap_ok.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
            self.window.done_run.setPixmap(self.ok_resized)
            self.popup()
        except:
            QMessageBox.about(None,"Error","Error showing results")
class ThreadLoading(QThread):
    def __init__(self,window):
        super().__init__()
        self.window = window
        # self.loading = Loading()

    def run(self):
        print('corriendo')
        self.loading.start()

    def stop(self):
        print('ya')
        self.loading.stop()
