import tensorflow as tf
import numpy as np
from PIL import Image
import user_photo_processor
import keras
# Load the saved model
model = keras.models.load_model('model.h5')

# Load the input image and preprocess it
input_image = "user_inputs/sin.jpg"
processed_image = user_photo_processor.process_image(input_image)

# Make a prediction on the input image
predictions = model.predict(processed_image)

# Get the predicted class index
predicted_class_index = np.argmax(predictions[0])

# Print the predicted class label
class_labels = ['!', '(', ')', '+', ',', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=','A', 'alpha', 'ascii_124', 'b', 'beta', 'C', 'cos', 'd', 'Delta', 
              'div', 'e', 'exists', 'f', 'forall', 'forward_slash','G', 'gamma', 'geq', 'gt', 'H', 'i', 'in', 'infty', 'int', 'j', 'k', 'l', 'lambda', 
              'ldots', 'leq', 'lim', 'log', 'lt', 'M', 'mu', 'N', 'neq', 'o', 'p', 'phi', 'pi', 'pm', 'prime', 'q', 'R', 'rightarrow', 'S', 'sigma', 
              'sin', 'sqrt', 'sum','T', 'tan', 'theta', 'times', 'u', 'v', 'w', 'X', 'y', 'z', '[', ']', '{', '}']

predicted_class_label = class_labels[predicted_class_index]
print("Predicted class: ", predicted_class_label)