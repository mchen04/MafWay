import tensorflow as tf
import numpy as np
from PIL import Image
import user_photo_processor
import keras
# Load the saved model
model = keras.models.load_model('model.h5')

# Load the input image and preprocess it
input_image = "../CitrusHackProject/user_inputs/cursive_cos.jpg"
processed_image = user_photo_processor.process_image(input_image)

# Make a prediction on the input image
predictions = model.predict(processed_image)

# Get the predicted class index
predicted_class_index = np.argmax(predictions[0])

# Print the predicted class label
class_labels = ["-","!","(",")","[","]","+","=","0","1","2","3","4","5","6","7","8","9","A","b","C","cos","d","div",
              "e","f","forward_slash","G","H","i","in","infty","int","j","k","l","lim",
              "log","M","N","o","p","pi","q","R","rightarrow","S","sigma","sin","sqrt","sum","T","tan","theta",
              "times","u","v","w","X","y","z"]
predicted_class_label = class_labels[predicted_class_index]
print("Predicted class: ", predicted_class_label)