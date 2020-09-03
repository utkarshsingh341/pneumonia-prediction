from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = load_model('model_vgg16.h5')
img = image.load_img('Datasets/val/PNEUMONIA/person1947_bacteria_4876.jpeg',target_size=(224,224))
#img = image.load_img('Datasets/val/NORMAL/NORMAL2-IM-1442-0001.jpeg',target_size=(224,224))
x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
img_data = preprocess_input(x)
classes = model.predict(img_data)

print("\n#########OUTPUT#########\n")
print("\nClass Array: ",classes)
x = classes[0]
if(x[0]==1):
    print("\nThe person is normal\n")
else:
    print("\nThe person has pneumonia\n")