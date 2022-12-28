import tensorflow as tf
import numpy as np
# from tensorflow.keras.preprocessing.image import load_img
# from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image


model = tf.keras.models.load_model('MobileNet_Car_detection.model')
print(model.summary())

img_path='0073.jpg'



# image = load_img(img_path, target_size=(224, 224))
# image = img_to_array(image)

# Open the image file
image = Image.open('0073.jpg')
image=image.resize((224,224))
image.show()

image_array = np.array(image)

#Set to 4 D
x = np.expand_dims(image, axis=0)

#Fit into the Model

predIdxs=model.predict(x)
predIdxs = np.argmax(predIdxs, axis=1)
print(predIdxs)
# Display the image




# print(image_array.shape)