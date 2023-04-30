import tensorflow as tf
import numpy as np
from PIL import Image
import user_photo_processor
import keras

'''
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests

# Set up Cloudinary account credentials
cloudinary.config(
  cloud_name = 'your_cloud_name',
  api_key = 'your_api_key',
  api_secret = 'your_api_secret'
)

# Get the metadata of all uploaded images
images = cloudinary.api.resources(type="upload")

# Sort the images based on their creation timestamp in descending order
sorted_images = sorted(images["resources"], key=lambda img: img["created_at"], reverse=True)

# Get the URL of the most recent image
most_recent_image_url = sorted_images[0]["secure_url"]

# Use the requests library to download the image
response = requests.get(most_recent_image_url)

# Save the image to a file
with open("most_recent_image.jpg", "wb") as f:
    f.write(response.content)
'''



# Load the saved model
model = keras.models.load_model('model.h5')

# Load the input image and preprocess it
input_image = "../CitrusHackProject/user_inputs/colored_exclam.jpg"
processed_image = user_photo_processor.process_image(input_image)

# Make a prediction on the input image
predictions = model.predict(processed_image)

# Get the predicted class index
predicted_class_index = np.argmax(predictions[0])

# Print the predicted class label
class_labels = ["-",",","!","(",")","[","]","{","}","+","=","0","1","2","3","4","5","6","7","8","9","A","alpha","ascii_124","b","beta","C","cos","d","Delta","div",
              "e","exists","f","forall","forward_slash","G","gamma","geq","gt","H","i","in","infty","int","j","k","l","lambda","ldots","leq","lim",
              "log","lt","M","mu","N","neq","o","p","phi","pi","pm","prime","q","R","rightarrow","S","sigma","sin","sqrt","sum","T","tan","theta",
              "times","u","v","w","X","y","z"]
predicted_class_label = class_labels[predicted_class_index]
print("Predicted class: ", predicted_class_label)

'''
# Call the function to upload the text file
filename = "predicted_class.txt"
url = upload_text_file_to_cloudinary(predicted_class_label, filename)
print("Uploaded file URL:", url)
'''
