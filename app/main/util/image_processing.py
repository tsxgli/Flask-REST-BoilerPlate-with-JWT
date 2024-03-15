import numpy as np
from tensorflow.keras.preprocessing import ImageDataGenerator, img_to_array

def process_image(image,target_size):
    if(image.mode != "RGB"):
        image = image.convert("RGB"
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

