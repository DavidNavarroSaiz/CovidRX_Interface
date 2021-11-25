<h1 align="center">COVID RX </h1>
<h1 align="center">Covid and pneumonia diagnosis using Xray images </h1>
<h1 align="center"> Desktop and Web App</h1>
<p>
    Radiometric images  have become a very important tool to detect and diagnose COVID-19, due that most of the COVID-19 cases have similar features, just like ground glass opacity and/or consolidation.
</p>
<p>
    Pulmonary lesions have been detected in computer tomography(CT) studies from even before the onset of symptoms until day 14 after the onset of symptoms. However, to date, most diagnostic tools based on CT are developed in hospitals with expensive equipment and where a high experience of radiologists is required.
</p>
<p>
    Therefore, due to the wide availability of chest x-rays in various health care treatments, they are an attractive option for a quick, accurate and less expensive diagnosis of COVID-19. Although RT images can detect suspicious cases early, the images of various viral pneumonias are similar and tend to be confused with other respiratory infections and inflammations, which is why diagnosis through the use of X-rays (RX) can leave a misdiagnosis
   So, for the X-ray tool to be adequate, it requires a team of expert radiologists who are able to identify and differentiate infections, which is the greatest difficulty with this technology.
   </p>
   <p>
    Currently, many biomedical health problems are using solutions based on artificial intelligence, the use of Convolution Neural Networks (CNN) has proven to be an extremely beneficial tool to extract characteristics from the image and to perform learning of these characteristics to perform image classification. . Deep learning techniques in chest radiographs are gaining popularity and show promising results in different applications, with results that are similar to that of a human expert when solving tasks such as classification in lung diseases, detection of metastases in breast cancer, lesions of the skin, identify diabetic retinopathy, Alzheimer's, reconstruction by magnetic resonance imaging and computed tomography. Detecting COVID-19 through imaging is one of the biggest challenges around the world.
</p>
<p>
Numerous methods for the detection of COVID-19 based on RT images and different architectures have been published in recent months with accuracies of more than 90%.
</p>


<p>

From the free data found in different databases, a dataset composed of:
* more than 10,000 images of COVID-19
* more than 15,000 images of people in good health
* more than 11000 images of people with pneumonia (different from covid)

The datasets used are below:


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
    Using Pytorch, different models were trained and the 10 with the best performance were chosen:

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
A graphic interface was created using Qt and a web page was created, which allows the user to upload a radiomedical image of the thorax and using the trained networks to diagnose the patient's condition.
</p>

