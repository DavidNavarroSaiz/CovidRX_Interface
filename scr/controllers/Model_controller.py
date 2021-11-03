import cv2
import torch
import torchvision
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from torchcam.utils import overlay_mask
from torchcam.cams import SmoothGradCAMpp,XGradCAM,GradCAMpp,GradCAM
from torchvision.transforms.functional import normalize, resize, to_pil_image
from torchvision.models.vgg import model_urls
import torch.nn.functional as F
import timm
import pathlib
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

model_urls['vgg19'] = model_urls['vgg19'].replace('https://', 'http://')

class ModelController():
    """
    a class who will load the model used to predict
    """
    def __init__(self):

        """
        initialize the model 
        """
        pass
    
    def load_model(self,model_name):
        """
        Load trained model
        """
        try:
            self.model_name  = model_name
            dir_path = pathlib.Path(__file__).parent.parent.resolve().as_posix()
            # try:
            if (self.model_name == "Vgg19"):
                path = dir_path + "/resources/saved_models/final_models/vgg19_1_3_0.97.pt"
                self.model = torchvision.models.vgg19(pretrained=True)
                # self.model.classifier = torch.nn.Linear(in_features=1920, out_features=3)
                self.model.classifier[6]= torch.nn.Linear(in_features=4096, out_features=3)
                self.target_layers = 'features'
                
            if(self.model_name == "DenseNet"):
                path = dir_path + "/resources/saved_models/final_models/dense_2_2_0.97.pt"
                self.model = torchvision.models.densenet201()
                self.model.classifier= torch.nn.Linear(in_features=1920, out_features=3)
                self.target_layers = 'features'
                
            if(self.model_name == "MobileNet"):
                path = dir_path + "/resources/saved_models/final_models/mobilenetv3_3_7_5500_0.97.pt"
                self.model = timm.create_model('tf_mobilenetv3_large_075')
                self.model.classifier = torch.nn.Linear(in_features=1280, out_features=3)
                self.target_layers = 'blocks'
                
            if(self.model_name == "AlexNet"):
                path = dir_path + "/resources/saved_models/final_models/alex_final_16.0000_0.948.pt"
                self.model = torchvision.models.alexnet()
                self.model.classifier[6]= torch.nn.Linear(in_features=4096, out_features=3)
                self.target_layers  ='features'
                
            if(self.model_name == "EfficientNet"):
                path = dir_path + "/resources/saved_models/final_models/efficientnetb7_1_3500_3_0.97.pt"
                self.model = timm.create_model('tf_efficientnet_b7_ns')
                self.model.classifier = torch.nn.Linear(in_features=2560, out_features=3)
                self.target_layers  ='blocks'
                
            if(self.model_name == "InceptionV3"):
                path = dir_path + "/resources/saved_models/final_models/InceptionV3_5_14_300_0.96.pt"
                self.model = torchvision.models.inception_v3()
                self.model.AuxLogits.fc = torch.nn.Linear(768, 3)
                self.model.fc = torch.nn.Linear(2048, 3)
                self.target_layers  ='Mixed_7c'
                
            if (self.model_name == "ResNet"):
                path = dir_path + "/resources/saved_models/final_models/ResNet152_11400_5_0.97.pt"
                self.model = torchvision.models.resnet152()
                self.model.fc = torch.nn.Linear(2048, 3)
                self.target_layers  ='layer4'
                
            if (self.model_name == "RexNet"):
                path = dir_path + "/resources/saved_models/final_models/Rexnet_4_8_1800_0.96.pt"
                self.model = timm.create_model('rexnet_200')
                self.model.head.fc = torch.nn.Linear(in_features=2560, out_features=3)
                self.target_layers  ='features'
            if (model_name == "Inception_ResNet"):
                path = dir_path + "/resources/saved_models/final_models/inception_resnet_1_3_7100_0.96.pt"
                self.model = timm.create_model('ens_adv_inception_resnet_v2')
                self.model.classifier = torch.nn.Linear(in_features=1280, out_features=3)
                self.target_layers = 'block8'
                
            if (model_name == "Xception"):
                path = dir_path + "/resources/saved_models/final_models/Xception_1_7_1700_0.97.pt"

                self.model = timm.create_model('gluon_xception65')
                self.model.fc = torch.nn.Linear(in_features=2048, out_features=3)
                self.target_layers = 'block20_act'
                    
            # dir_path + /resources/saved_models/final_models/
            self.model.eval()
            # self.model.to('cpu')
            self.model.load_state_dict(torch.load(path, map_location=torch.device('cpu')),strict=False)
            # self.cam_extractor = SmoothGradCAMpp(self.model)
            self.cam_extractor1 = XGradCAM(self.model,self.target_layers)
            self.cam_extractor2 = SmoothGradCAMpp(self.model,self.target_layers)
            self.cam_extractor3 = GradCAMpp(self.model,self.target_layers)
            self.cam_extractor4 = GradCAM(self.model,self.target_layers)
        except:
            QMessageBox.about(None,"Error","Error loading model")

    def load__transformed_image(self,image_path):
        """
        Load image and apply transformations
        """
        try:
            img = cv2.imread(image_path)
            self.rgbimage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.rgbimage = cv2.resize(self.rgbimage, (256, 256)) 
            if (self.model_name == "InceptionV3"):
                image_size = (299,299)
            else: 
                image_size = (224,224)
            transform = torchvision.transforms.Compose([
                        torchvision.transforms.Resize(size=image_size),
                        torchvision.transforms.ToTensor(),
                        torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                        ])
            img_pil = Image.open(image_path)
            self.image = img_pil.convert('RGB')
            self.image_transformed = transform(self.image)
        except:
            QMessageBox.about(None,"Error","Error loading image")
        
    def evaluate(self):
        """
        predict the result based on the model
        """
        try:
            self.output = self.model(self.image_transformed.unsqueeze(0))
            self.prob = F.softmax(self.output, dim=1).detach().numpy()[0]
            self.prob_normal = self.prob[0]
            self.prob_viral = self.prob[1]
            self.prob_covid = self.prob[2]
            print('normal: ',self.prob_normal,' Viral: ',self.prob_viral, ' Covid: ',self.prob_covid)
        except:
            QMessageBox.about(None,"Error","Error Evaluating the model")
    def heat_map(self):
        """
        apply heat map to the image and show result
        """
        try:
            
            activation_map1 = self.cam_extractor1(self.output.squeeze(0).argmax().item(), self.output)
            activation_map2 = self.cam_extractor2(self.output.squeeze(0).argmax().item(), self.output)
            activation_map3 = self.cam_extractor3(self.output.squeeze(0).argmax().item(), self.output)
            activation_map4 = self.cam_extractor4(self.output.squeeze(0).argmax().item(), self.output)
            if (torch.isnan(activation_map1).any() == True): activation_map1[torch.isnan(activation_map1)] = 0.5
            if (torch.isnan(activation_map2).any() == True): activation_map2[torch.isnan(activation_map2)] = 0.5
            if (torch.isnan(activation_map3).any() == True): activation_map3[torch.isnan(activation_map3)] = 0.5
            if (torch.isnan(activation_map4).any() == True): activation_map4[torch.isnan(activation_map4)] = 0.5
            sum_activation_map = activation_map1 + activation_map2 +activation_map3+activation_map4
            activation_map =  sum_activation_map / 4


            return self.rgbimage,activation_map.numpy(),self.prob_normal,self.prob_viral, self.prob_covid
        except:
            QMessageBox.about(None,"Error","Error Extracting Heatmap")
    

        


if (__name__ == '__main__'):

    path_image = 'COVID (13).png'
    path_model = './../resources/saved_models/vgg19.pt'
    controller = ModelController()
    controller.load__transformed_image(path_image)
    controller.load_model(path_model)
    controller.evaluate()
    controller.heat_map()





