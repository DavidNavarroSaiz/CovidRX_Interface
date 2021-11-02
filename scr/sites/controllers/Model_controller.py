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
import pathlib, os


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
        self.model_name  = model_name
        dir_path = pathlib.Path(__file__).parent.parent.resolve().as_posix()

        if (self.model_name == "Vgg19"):
            path = dir_path + "/resources/saved_models/final_models/vgg19_1_3_0.97.pt"
            self.model = torchvision.models.vgg19(pretrained=True)
            # self.model.classifier = torch.nn.Linear(in_features=1920, out_features=3)
            self.model.classifier[6]= torch.nn.Linear(in_features=4096, out_features=3)
            self.target_layers = 'features'
            
        if(self.model_name == "Densenet"):
            path = dir_path + "/resources/saved_models/final_models/dense_2_2_0.97.pt"
            self.model = torchvision.models.densenet201()
            self.model.classifier= torch.nn.Linear(in_features=1920, out_features=3)
            self.target_layers = 'features'
            
        if(self.model_name == "Mobilenet"):
            path = dir_path + "/resources/saved_models/final_models/mobilenetv3_3_7_5500_0.97.pt"
            self.model = timm.create_model('tf_mobilenetv3_large_075')
            self.model.classifier = torch.nn.Linear(in_features=1280, out_features=3)
            self.target_layers = 'blocks'
            
        if(self.model_name == "Alexnet"):
            path = dir_path + "/resources/saved_models/final_models/alex_final_16.0000_0.948.pt"
            self.model = torchvision.models.alexnet()
            self.model.classifier[6]= torch.nn.Linear(in_features=4096, out_features=3)
            self.target_layers  ='features'
            
        if(self.model_name == "Efficientnet"):
            path = dir_path + "/resources/saved_models/final_models/efficientnetb7_1_3500_3_0.97.pt"
            self.model = timm.create_model('tf_efficientnet_b7_ns')
            self.model.classifier = torch.nn.Linear(in_features=2560, out_features=3)
            self.target_layers  ='blocks'
            
        if(self.model_name == "InceptionV3"):
            path = dir_path + "/resources/saved_models/final_models/InceptionV3_3_8_0.95.pt"
            self.model = torchvision.models.inception_v3()
            self.model.AuxLogits.fc = torch.nn.Linear(768, 3)
            self.model.fc = torch.nn.Linear(2048, 3)
            self.target_layers  ='Mixed_7c'
            
        if (self.model_name == "Resnet"):
            path = dir_path + "/resources/saved_models/final_models/ResNet152_11400_5_0.97.pt"
            self.model = torchvision.models.resnet152()
            self.model.fc = torch.nn.Linear(2048, 3)
            self.target_layers  ='layer4'
            
        if (self.model_name == "Rexnet"):
            path = dir_path + "/resources/saved_models/final_models/rexnet_3_7_7800_0.95.pt"
            self.model = timm.create_model('rexnet_100')
            self.model.classifier = torch.nn.Linear(in_features=2560, out_features=3)
            self.target_layers  ='features'
            
        self.model.eval()
        # self.model.to('cpu')
        self.model.load_state_dict(torch.load(path, map_location=torch.device('cpu')),strict=False)
        # self.cam_extractor = SmoothGradCAMpp(self.model)
        self.cam_extractor1 = XGradCAM(self.model,self.target_layers)
        self.cam_extractor2 = SmoothGradCAMpp(self.model,self.target_layers)
        self.cam_extractor3 = GradCAMpp(self.model,self.target_layers)
        self.cam_extractor4 = GradCAM(self.model,self.target_layers)
        
    def load__transformed_image(self,img):
        """
        Load image and apply transformations
        """

        self.rgbimage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.rgbimage = cv2.resize(self.rgbimage, (256, 256)) 
        if (self.model_name == "InceptionV3"):
            image_size = (299,299)
        else: 
            image_size = (224,224)
        transform = torchvision.transforms.Compose([
                    torchvision.transforms.Resize(size=image_size),
                    torchvision.transforms.RandomHorizontalFlip(),
                    torchvision.transforms.ToTensor(),
                    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                    ])
        img_pil = Image.fromarray(img)
        self.image = img_pil.convert('RGB')
        self.image_transformed = transform(self.image)
        
    def evaluate(self):
        """
        predict the result based on the model
        """
        # labels = ["normal","viral","covid"]
        
        self.output = self.model(self.image_transformed.unsqueeze(0))
        # if (self.model_name == "InceptionV3"):
        #     print( self.output)
        # else:
        # self.prediction = labels[np.argmax(self.output.tolist())]
        self.prob = F.softmax(self.output, dim=1).detach().numpy()[0]
        
        print(self.prob)
        self.prob_normal = self.prob[0]
        self.prob_viral = self.prob[1]
        self.prob_covid = self.prob[2]
        # top_p, top_class = self.prob.topk(1, dim = 1)
        # print(self.output)
        # print(self.output.tolist())
        # print(self.prob)
        return self.prob_covid, self.prob_normal, self.prob_viral
    
    def     heat_map(self):
        """
        apply heat map to the image and show result
        """
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
        
    

        


if (__name__ == '__main__'):

    path_image = 'COVID(13).png'
    path_model = './../resources/final_models/vgg19_1_3_0.97.pt'
    controller = ModelController()
    controller.load_model("Vgg19")
    controller.load__transformed_image(path_image)
    controller.evaluate()
    controller.heat_map()





