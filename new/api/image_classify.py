# import tensorflow as tf
import numpy as np
from PIL import Image

import os
def predict_classify(image):
    path = os.getcwd()
    path = os.path.join(path, "model\\MobileNet_Car_detection.model")
    path = path.replace("\\","/")
    model = tf.keras.models.load_model(path)
    # print(model.summary())
    image = Image.open(image)
    image=image.resize((224,224))
    image_array = np.array(image)
    x = np.expand_dims(image_array, axis=0)
    predIdxs=model.predict(x)
    predIdxs = np.argmax(predIdxs, axis=1)
    # print(predIdxs)
    return predIdxs
    

    
    
    