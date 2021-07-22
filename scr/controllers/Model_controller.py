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
    
    def load_model(self,path):
        """
        Load trained model
        """
        self.model = torchvision.models.vgg19(pretrained=True)
        # self.model.classifier = torch.nn.Linear(in_features=1920, out_features=3)
        self.model.classifier[6]= torch.nn.Linear(in_features=4096, out_features=3)
        self.model.to('cpu')
        self.model.load_state_dict(torch.load(path, map_location=torch.device('cpu')),strict=False)
        self.cam_extractor = SmoothGradCAMpp(self.model)


    def load__transformed_image(self,image_path):
        """
        Load image and apply transformations
        """
        img = cv2.imread(image_path)
        self.rgbimage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        transform = torchvision.transforms.Compose([
                  torchvision.transforms.Resize(size=(224, 224)),
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
        labels = ["normal","viral","covid"]
        
        self.output = self.model(self.image_transformed.unsqueeze(0))
        self.prediction = labels[np.argmax(self.output.tolist())]
        print(self.prediction)
        
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
        return img_result,self.prediction
        
    


        
        


if (__name__ == '__main__'):

    path_image = 'images/test/COVID/COVID (43).png'
    path_model = 'saved_models/vgg19.pt'
    controller = ModelController()
    controller.load__transformed_image(path_image)
    controller.load_model(path_model)
    controller.evaluate()
    controller.heat_map()


