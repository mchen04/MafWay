from PIL import Image
import numpy as np
import os

def process_image(image_path):
    # Open the image file
    image = Image.open(image_path).convert('L')

    # Converted image to 45 x 45
    image = image.resize((45,45))

    # Convert the black and white image to a NumPy array
    image_array = np.array(image)

    # Normalize pixel values
    image_array = image_array / 255.0
    image_array = np.reshape(image_array, (1, 45, 45, 1))

    filename = os.path.basename(image_path)
    image.save('../CitrusHackProject/processed_user_inputs/'+filename)

    return image_array
