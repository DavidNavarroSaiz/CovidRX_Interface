<h1 align="center">COVID RX </h1>
<h1 align="center">Covid and pneumonia diagnosis using Xray images </h1>
<h1 align="center"> Desktop and Web App</h1>
<p>
    Radiometric images  have become a very important tool to detect and diagnose COVID-19, due that most of the COVID-19 cases have similar features, just like ground glass opacity and/or consolidation.

    Pulmonary lesions have been detected in computer tomography(CT) studies from even before the onset of symptoms until day 14 after the onset of symptoms. However, to date, most diagnostic tools based on CT are developed in hospitals with expensive equipment and where a high experience of radiologists is required.

    Therefore, due to the wide availability of chest x-rays in various health care treatments, they are an attractive option for a quick, accurate and less expensive diagnosis of COVID-19. Although RT images can detect suspicious cases early, the images of various viral pneumonias are similar and tend to be confused with other respiratory infections and inflammations, which is why diagnosis through the use of X-rays (RX) can leave a misdiagnosis
   So, for the X-ray tool to be adequate, it requires a team of expert radiologists who are able to identify and differentiate infections, which is the greatest difficulty with this technology.
   
    Currently, many biomedical health problems are using solutions based on artificial intelligence, the use of Convolution Neural Networks (CNN) has proven to be an extremely beneficial tool to extract characteristics from the image and to perform learning of these characteristics to perform image classification. . Deep learning techniques in chest radiographs are gaining popularity and show promising results in different applications, with results that are similar to that of a human expert when solving tasks such as classification in lung diseases, detection of metastases in breast cancer, lesions of the skin, identify diabetic retinopathy, Alzheimer's, reconstruction by magnetic resonance imaging and computed tomography. Detecting COVID-19 through imaging is one of the biggest challenges around the world.
</p>
<p>
Numerous methods for the detection of COVID-19 based on RT images and different architectures have been published in recent months with accuracies of more than 90%.
</p>
<p>
A partir de los datos libres encontrados en diferentes bases de datos, se recopilo un dataset compuesto por:
* mas de 10000 imagenes de COVID-19
* mas de 15000 imagenes de personas en buen estado de salud 
* mas de 11000 imagenes ed personas con pneumonia(diferente de covid)

Los datasets usados se encuentran a continuacion:
https://github.com/samxmot/RANDGAN - Randomized Generative Adversarial Network for Detection of COVID-19 in Chest X-ray

https://github.com/jdariasl/COVIDNET - Artificial Intelligence applied to chest X-Ray images for the automatic detection of COVID-19. A thoughtful evaluation approach

https://github.com/ieee8023/covid-chestxray-dataset

https://www.kaggle.com/tawsifurrahman/covid19-radiography-database

https://www.kaggle.com/bachrr/covid-chest-xray

https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

https://github.com/IAM-CVC/CovAIR

https://academictorrents.com/details/557481faacd824c83fbf57dcf7b6da9383b3235a
</p>

<p>
    Utilizando Pytorch se entrenaron diferentes modelos y se eligieron los 10 con mejor performance:
    Vgg19
    Densenet
    Mobilenet
    Alexnet
    Efficientnet
    InceptionV3
    Resnet
    Rexnet
    Inception_resnet
    Xception
</p>

<p>
    Se creo una interfaz grafica utilizando Qt y se realizo una pagina web, que permite al usuario cargar una imagen radiomedica del torax y utilizando las redes entrenadas se diagnostica el estado del paciente.
</p>



<h2>Run the applications</h2>

<h3>Setting your Virtual environment</h3>

<p>
    it is an optional step but is highly recommended to work over a virtual environment based on python 3.8, . You can create your virtual enviorment running the following code line:
</p>


```
    python3.8 -m venv <env_name>
```
<p>
    if you are using anaconda you just can write the following code line:
</p>
```
    conda create --name <env_name> python=3.8
```

<p>Activating the virtual environment:<p>

```
    cd <env_name> \Scripts\activate.bat
```
<p>Anaconda:<p>
```
    conda activate <env_name>
```




<h3>Download Repository</h3>
<p>it can be downloaded using:</p>

```
    git clone https://github.com/DavidNavarroSaiz/CovidRX_Interface.git
```

<h3>Install libraries</h3>

```
    pip install -r requirements.txt
```






<h3>Desktop App: How to use</h3>

<p>Exectuing the desktop app</p>

```
    cd src
    python app.py
```
<div align="center">
    <img src="./resources/images/app.jpg" width="800"><img>
</div>

<p> Click load image Button, an emerging window will display. Please choose the image you want to evaluate and click Open image.</p>

<div align="center">
    <img src="./resources/images/Load_image.jpg" width="800"><img>
</div>
<p> You can click now Run Diagnosis button, and wait a moment until the diagnosis is completed, it will display a message, you can read your final diagnosis and then click OK </p>
<div align="center">
    <img src="./resources/images/diagnosis2.jpg" width="800"><img>
</div>
<p> A heat map is displayed, it shows the main zones activated by the Convolutional neural network layers. It can be an indicator about what are the most affected zones in the person. however, it is not a trustable indicator and it is not based on qualitative methods, it is just an analysis about the activation map of the neural networks, so does not necessarily represent valid medical information</p>


<p> On the right side of the application you can check the probabilities to be Normal, to have pneumonia or to have covid. If the bar is green it means that you have low probabilities( less than 30%), if it is yellow it is a high-mid probability(30% - 60%) and if the bar is red it means that it is a high probability(higher than 60%) </p>

<div align="center">
    <img src="./resources/images/Diagnosis.jpg" width="800"><img>
</div>


<p> The user can save the heatmap clicking Save heatmap button, it will appear an emerging window, where you can choose the location and the name to save the heatmap </p>


<p> As said before, the diagnosis is based on CNN so there are 10 trained models that you can select or deselect, if you select more than one model, then it will average the results of the selected models. You can change the models selection in the top bar menu,and you can choose the models of your preference:</p>
<div align="center">
    <img src="./resources/images/models.jpg" width="800"><img>
</div>

<h3>web App: How to use</h3>

<p>Exectuing the Web app</p>

```
    cd src
    cd sites
    python webApp.py

```
<p> copy and paste the http://127.0.0.1:5000/ in any navigator of preference. </p>
<div align="center">
    <img src="./resources/images/webapp.jpg" width="800"><img>
</div>

<p> Click load image, choose the image that you want to diagnose and click open. </p>

<div align="center">
    <img src="./resources/images/cargar.jpg" width="800"><img>
</div>

<p> Click diagnosis and the algorithm will analyze the image. </p>
<div align="center">
    <img src="./resources/images/webdiag.jpg" width="800"><img>
</div>
<p>
it will display a heatmap of the diagnosis, and a plot with the distribution of probbility of being normal, pneumonia or covid. 

</p>


