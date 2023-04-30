from PIL import Image
import numpy as np
import os

def process_image(image_path):
    # Open the image file
    image = Image.open(image_path).convert('L')

    # Converted image to 28 x 28
    image = image.resize((28,28))

    # Convert the black and white image to a NumPy array
    image_array = np.array(image)
    
    filename = os.path.basename(image_path)
    image.save('../CitrusHackProject/processed_user_inputs/'+filename)

    return image_array
