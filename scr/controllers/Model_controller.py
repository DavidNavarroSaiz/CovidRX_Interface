import cv2
import torch
import torchvision
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from torchcam.utils import overlay_mask
from torchcam.cams import SmoothGradCAMpp,XGradCAM,SSCAM
from torchvision.transforms.functional import normalize, resize, to_pil_image
from torchvision.models.vgg import model_urls
import torch.nn.functional as F
import timm
import pathlib


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

        if(self.model_name == "Densenet"):
            path = dir_path + "/resources/saved_models/final_models/dense_2_2_0.97.pt"
            self.model = torchvision.models.densenet201()
            self.model.classifier= torch.nn.Linear(in_features=1920, out_features=3)

        if(self.model_name == "Mobilenet"):
            path = dir_path + "/resources/saved_models/final_models/mobilenetv3_3_7_5500_0.97.pt"
            self.model = timm.create_model('tf_mobilenetv3_large_075')
            self.model.classifier = torch.nn.Linear(in_features=1280, out_features=3)

        if(self.model_name == "Alexnet"):
            path = dir_path + "/resources/saved_models/final_models/alex_final_16.0000_0.948.pt"
            self.model = torchvision.models.alexnet()
            self.model.classifier[6]= torch.nn.Linear(in_features=4096, out_features=3)

        if(self.model_name == "Efficientnet"):
            path = dir_path + "/resources/saved_models/final_models/efficientnetb7_1_3500_3_0.97.pt"
            self.model = timm.create_model('tf_efficientnet_b7_ns')
            self.model.classifier = torch.nn.Linear(in_features=2560, out_features=3)

        if(self.model_name == "InceptionV3"):
            path = dir_path + "/resources/saved_models/final_models/InceptionV3_3_8_0.95.pt"
            self.model = torchvision.models.inception_v3()
            self.model.AuxLogits.fc = torch.nn.Linear(768, 3)
            self.model.fc = torch.nn.Linear(2048, 3)

        if (self.model_name == "Resnet"):
            path = dir_path + "/resources/saved_models/final_models/ResNet152_11400_5_0.97.pt"
            self.model = torchvision.models.resnet152()
            self.model.fc = torch.nn.Linear(2048, 3)
            
        if (self.model_name == "Rexnet"):
            path = dir_path + "/resources/saved_models/final_models/rexnet_3_7_7800_0.95.pt"
            self.model = timm.create_model('rexnet_100')
            self.model.classifier = torch.nn.Linear(in_features=2560, out_features=3)
            
            
        self.model.eval()
        # self.model.to('cpu')
        self.model.load_state_dict(torch.load(path, map_location=torch.device('cpu')),strict=False)
        self.cam_extractor = SmoothGradCAMpp(self.model)

    def load__transformed_image(self,image_path):
        """
        Load image and apply transformations
        """
        img = cv2.imread(image_path)
        self.rgbimage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
        img_pil = Image.open(image_path)
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
        self.prob_normal = self.prob[0]
        self.prob_viral = self.prob[1]
        self.prob_covid = self.prob[2]
        # top_p, top_class = self.prob.topk(1, dim = 1)
        # print(self.output)
        # print(self.output.tolist())
        # print(self.prob)
    
    def heat_map(self):
        """
        apply heat map to the image and show result
        """
        activation_map = self.cam_extractor(self.output.squeeze(0).argmax().item(), self.output)
        result = overlay_mask(to_pil_image(self.rgbimage), to_pil_image(activation_map, mode='F'), alpha=0.7)
        img_result = np.array(result)
        # cv2.imshow('Result',img_result)
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows()   
        return img_result,self.prob_normal,self.prob_viral, self.prob_covid
        
    

        


if (__name__ == '__main__'):

    path_image = 'COVID (13).png'
    path_model = './../resources/saved_models/vgg19.pt'
    controller = ModelController()
    controller.load__transformed_image(path_image)
    controller.load_model(path_model)
    controller.evaluate()
    controller.heat_map()





