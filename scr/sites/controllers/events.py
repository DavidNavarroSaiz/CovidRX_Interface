
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
import base64
from scipy import stats

class Events():
    """
    Set the respective events for the buttons

    """
    def __init__(self):
        # self.connectButtons()
        a =0


    def connectButtons(self):
        """
        Connect each button with is respective event
        """
        self.window.pushload.clicked.connect(self.load_image)
        self.window.pushButtonRun.pressed.connect(self.loading)
        self.window.pushButtonRun.released.connect(self.run)
        self.window.SaveButton.clicked.connect(self.save_image)
        self.window.pushButtonRun.setEnabled(False)
        self.window.pushButtonRun.setText("Select Models on the top Menu")
        self.window.actionVgg19.changed.connect(self.activate_run)
        self.window.actionDenseNet.changed.connect(self.activate_run)
        self.window.actionMobileNet.changed.connect(self.activate_run)
        self.window.actionAlexNet.changed.connect(self.activate_run)
        self.window.actionEfficientNet.changed.connect(self.activate_run)
        self.window.actionInceptionV3.changed.connect(self.activate_run)
        self.window.actionResNet_2.changed.connect(self.activate_run)
        self.window.actionRexNet.changed.connect(self.activate_run)
        
    def load_image(self):
        """
        Load and display the coresponding image

        """
        # self.filename,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open image file", r"~/Desktop/","image files(*.jpg *.jpeg *.png)")
        # imagePixmap = QtGui.QPixmap.fromImage( self.filename)
        # pixmap_resized = imagePixmap.scaled(320, 280, QtCore.Qt.KeepAspectRatio)
        # self.window.label_4.setPixmap(pixmap_resized)
        # self.window.label_4.setScaledContents(True)
        # self.window.Filename.setObjectName(self.filename)  
        print('load image')

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

        # """
        a = os.path.abspath('')               
        # path_model = a+"\\scr\\resources\\saved_models\\vgg19.pt"
        
        controller = ModelController()
        controller.load_model("Rexnet")
        controller.load__transformed_image(self.filename)
        
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
        self.window.label_5.pixmap().save(self.filename)

    def popup(self):
        self.final_prediction = self.window.FinalPrediction.objectName()
        if (self.final_prediction == "covid" ):
        # QMessageBox.about(self.window, "AboutBox", "This is about application")
            QMessageBox.warning(self.window, "Warning", "You have a chance of "+str(round(self.window.progressBar_3.value(),2))+'%' 
                                ' of having COVID-19 dissease \n Please communicate with your medical entity ')
        elif(self.final_prediction=="viral"):
            QMessageBox.warning(self.window,"Warning","you have a chance of "+str(round(self.window.progressBar_2.value(),2))+'%'' of having pneumonia \n Please communicate with your medical entity')
        
        elif(self.final_prediction == "normal"):
            QMessageBox.warning(self.window,"Warning","you have a chance of "+str(round(self.window.progressBar_1.value(),2))+'%'' of being OK \n Congratulations')

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
            self.window.actionResNet_2.isChecked() | self.window.actionRexNet.isChecked()
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
#
    def data_uri_to_cv2_img(self, uri):
        encoded_data = uri.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

    def run(self,json_data):
        """
        Evaluate a list of models
        
        """
        image64 = json_data["img64"]
        mat = self.data_uri_to_cv2_img(image64)
        self.probabilities_normal = []
        self.probabilities_viral = []
        self.probabilities_covid = []
        self.result_ActivationMap =[]
        self.diagnosis = []
        self.model_list = []

        if json_data['vgg'] == "true": self.model_list.append("Vgg19")
        if json_data['dense'] == "true": self.model_list.append("Densenet")
        if json_data['mobil'] == "true": self.model_list.append("Mobilenet")
        if json_data['alex'] == "true": self.model_list.append("Alexnet")
        if json_data['efficient'] == "true": self.model_list.append("Efficientnet")
        if json_data['inception'] == "true": self.model_list.append("InceptionV3")
        if json_data['resnet'] == "true" : self.model_list.append("Resnet")
        if json_data['rexnet'] == "true": self.model_list.append("Rexnet")
        model_counter = 0
        for model in self.model_list:
            print("Evaluating model: ",self.model_list[model_counter])
            controller = ModelController()
            controller.load_model(model)
            controller.load__transformed_image(mat)
            prob_covid, prob_normal,prob_viral = controller.evaluate()
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
        return self.compute_final_results()
        

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
        # self.window.FinalPrediction.setObjectName(self.final_prediction) 
        # print(covid_prob)
        result = overlay_mask(to_pil_image(self.rgbimage), to_pil_image(self.FinalActivationMap, mode='F'), alpha=0.7)
        self.img_result = np.array(result)
        a = os.path.abspath('')               
        
        _, buffer = cv2.imencode('.png',self.img_result)
        img_base64 = base64.b64encode(buffer)
        # self.display_results()
        probabilities = {
            "Covid" : list_probabilities[2],
            "Viral" : list_probabilities[1],
            "Normal" : list_probabilities[0],
            "img64" : img_base64.decode('utf-8')
        }
        # cv2.imwrite(a+"\\scr\\sites\\static\\images\\"+"heatmap.png",self.img_result)
        return probabilities

    def display_results(self):
        # self.movie.stop()
        # self.movie.close()
        
        result = overlay_mask(to_pil_image(self.rgbimage), to_pil_image(self.FinalActivationMap, mode='F'), alpha=0.7)
        self.img_result = np.array(result)

        h,w,z = np.shape(self.img_result)
        QResult = QtGui.QImage(self.img_result.data, h, w, 3*h, QtGui.QImage.Format_RGB888)  

        self.imagePixmap_result = QtGui.QPixmap.fromImage(QResult)
        self.imagePixmap_result = self.imagePixmap_result.scaled(320, 280, QtCore.Qt.KeepAspectRatio)

        self.window.label_5.setPixmap(self.imagePixmap_result)
        self.window.label_5.setScaledContents(True)  
        self.window.progressBar.setValue(self.normal_prob)
        self.window.progressBar_2.setValue(self.viral_prob)
        self.window.progressBar_3.setValue(self.covid_prob)
        # cv2.imshow('ImageWindow', self.rgbimage)
        # cv2.waitKey()
        self.popup()
        