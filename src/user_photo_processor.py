from PIL import Image
import numpy as np

def process_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Converted image to 28 x 28
    image = image.resize((28,28))

    # Convert the image to black and white (grayscale)
    image_bw = image.convert('L')

    # Convert the black and white image to a NumPy array
    image_array = np.array(image_bw)

    return image_array
