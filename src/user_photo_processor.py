from PIL import Image
import glob
import numpy as np
import os

# Set the path to the folder containing the pictures
folder_path = '../CitrusHackProject/user_inputs/'
output_folder = '../CitrusHackProject/processed_user_inputs/'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define the list of supported image extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

# Use the glob module to retrieve all picture files with supported extensions in the folder
picture_files = []
for ext in image_extensions:
    picture_files.extend(glob.glob(folder_path + '/*' + ext))

# Iterate through the picture files
for file_path in picture_files:
    # Open the image file
    image = Image.open(file_path)

    # Converted image to 28 x 28
    image = image.resize((28,28))
    
    # Convert the image to black and white (grayscale)
    image_bw = image.convert('L')
    
    # Convert the black and white image to a NumPy array
    image_array = np.array(image_bw)
    
    # Get the size of the image
    width, height = image.size

    filename = os.path.basename(file_path)
    filename = os.path.splitext(filename)[0]  # Remove the original file extension
    output_path = os.path.join(output_folder, filename + '.jpg')  # Add .jpg extension
    image_bw.save(output_path, 'JPEG')
    

    #Can delete prints

    print(f"Grayscale image saved: {output_path}")

    # Print the size
    print(f"Image size: {width}x{height}")

