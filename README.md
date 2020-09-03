# Predicting Pnuemonia Disease
### Creating a deep-learning project to predict pneumonia disease in a patient through patterns observed in lung X-rays using transfer learning


## Motivation for selecting the problem statement
Pneumonia can range in seriousness from mild to life-threatening as it causes inflammation and fluid accumulation in the lungs, making it hard to breathe. It is most serious for infants and young children, people older than age 65. ***It is also a potential complication of COVID-19***

To help detect which patients require more medical care, we can use artificial intelligence to analyze lung imaging as part of a clinical research study. The goal would be develop a model that can predict the severity of a pneumonia patient’s lung disease through images of their lung X-ray.

## Dataset Details

Dataset link - https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

Chest X-ray images were selected from retrospective cohorts of patients from five to thirty years old from Guangzhou Women and Children’s Medical Center, Guangzhou. All chest X-ray imaging was performed as part of patients’ routine clinical care.


## DL Algorithms/Model details

### VGG-16
- VGG-16 Neural Network consists of 16 layers of deep neural network trained on more than a million from the “ImageNet” database.
- After training for 5 epochs, **we received an accuracy of 91%**
### VGG-19
- The concept of the VGG19 is same as the VGG16 except that the model is more complex as the network is 19 layers deep.
- After training for 5 epochs, **we received an accuracy of 92%**
### RESNET-50
- Resnets are a kind of CNNs called Residual Networks. They are very deep compared to VGG-16 and VGG-19.
- After training for 5 epochs, **we received an accuracy of 85%**


## Training and Testing details

### Training
Training the model for more than 5216 chest x-ray images. Trained each model for 5 epochs to achieve best accuracy
### Testing
Comparing with the training model to achieve an accuracy and loss graph. Testing with 624 images. Altering the parameters, number of epochs to achieve highest accuracy and minimal loss


## Results

We receive output in 2 classes (one denoting NORMAL case, other denoting PNEUMONIA case) Upon judging from this output, we can deduce if the person is suffering from pneumonia or not. 

### Accuracy & Loss graphs

![Screenshot](https://user-images.githubusercontent.com/33038093/92111092-67188d00-ee09-11ea-9562-372e01a73aa7.png)

### Results obtained by calculations

![result](https://user-images.githubusercontent.com/33038093/92111779-72b88380-ee0a-11ea-9797-99160c59e984.jpg)

_Comma separated values indicates values for NORMAL and PNUEMONIA class_



