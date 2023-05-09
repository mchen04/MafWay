import tensorflow as tf
import numpy as np
from PIL import Image
import user_photo_processor
import keras
import glob

import os

# Set the path to the input images folder
input_folder = "user_inputs/"

num_correct_predictions = 0
total_predictions = 0

# Load the saved model
model = keras.models.load_model('model.h5')

# Load the class labels
class_labels = ['!', '(', ')', '+', ',', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=','A', 'alpha', 'ascii_124', 'b', 'beta', 'C', 'cos', 'd', 'Delta', 
              'div', 'e', 'exists', 'f', 'forall', 'forward_slash','G', 'gamma', 'geq', 'gt', 'H', 'i', 'in', 'infty', 'int', 'j', 'k', 'l', 'lambda', 
              'ldots', 'leq', 'lim', 'log', 'lt', 'M', 'mu', 'N', 'neq', 'o', 'p', 'phi', 'pi', 'pm', 'prime', 'q', 'R', 'rightarrow', 'S', 'sigma', 
              'sin', 'sqrt', 'sum','T', 'tan', 'theta', 'times', 'u', 'v', 'w', 'X', 'y', 'z', '[', ']', '{', '}']

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file has an image extension
    if filename.endswith((".jpg", ".jpeg", ".png", ".PNG")):
        # Load the input image and preprocess it
        input_image = os.path.join(input_folder, filename)
        processed_image = user_photo_processor.process_image(input_image)

        # Make a prediction on the input image
        predictions = model.predict(processed_image)

        # Get the predicted class index
        predicted_class_index = np.argmax(predictions[0])
        predicted_class_label = class_labels[predicted_class_index]

        # Print the predicted class label
        print("Predicted class for {}: {}".format(filename, predicted_class_label))
