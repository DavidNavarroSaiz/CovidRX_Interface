<h1 align="center">COVID RX </h1>
<h1 align="center">Covid and pneumonia diagnosis using Xray images </h1>
<h1 align="center"> Desktop and Web App</h1>

    Radiometric images  have become a very important tool to detect and diagnose COVID-19, due that most of the COVID-19 cases have similar features, just like ground glass opacity and/or consolidation.

    Pulmonary lesions have been detected in computer tomography(CT) studies from even before the onset of symptoms until day 14 after the onset of symptoms. However, to date, most diagnostic tools based on CT are developed in hospitals with expensive equipment and where a high experience of radiologists is required.

    Therefore, due to the wide availability of chest x-rays in various health care treatments, they are an attractive option for a quick, accurate and less expensive diagnosis of COVID-19. Although RT images can detect suspicious cases early, the images of various viral pneumonias are similar and tend to be confused with other respiratory infections and inflammations, which is why diagnosis through the use of X-rays (RX) can leave a misdiagnosis
   So, for the X-ray tool to be adequate, it requires a team of expert radiologists who are able to identify and differentiate infections, which is the greatest difficulty with this technology.
   
    Currently, many biomedical health problems are using solutions based on artificial intelligence, the use of Convolution Neural Networks (CNN) has proven to be an extremely beneficial tool to extract characteristics from the image and to perform learning of these characteristics to perform image classification. . Deep learning techniques in chest radiographs are gaining popularity and show promising results in different applications, with results that are similar to that of a human expert when solving tasks such as classification in lung diseases, detection of metastases in breast cancer, lesions of the skin, identify diabetic retinopathy, Alzheimer's, reconstruction by magnetic resonance imaging and computed tomography. Detecting COVID-19 through imaging is one of the biggest challenges around the world.

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

