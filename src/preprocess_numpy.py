from PIL import Image
import numpy as np
import os

# specify path to folder containing images
folder_path = '../CitrusHackProject/extracted_images/'

# initialize empty list to store images
images = []

# loop through subfolders in folder
for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)
    # loop through images in subfolder
    for filename in os.listdir(subfolder_path):
        if filename.endswith('.jpg'):
            # open image using PIL
            img = Image.open(os.path.join(subfolder_path, filename)).convert('L')

            # resize image to 28x28
            img = img.resize((28, 28))

            # convert image to numpy array
            img_array = np.array(img)

            # append image array to list
            images.append(img_array)


# convert list of images to numpy array
images_array = np.array(images)

# normalize pixel values
images_array = images_array / 255.0

# reshape array and convert values to integers
images_array = np.reshape(images_array, (375974, 28, 28, 1))
np.set_printoptions(precision=0)
images_array = np.round(images_array).astype(int)

# print shape of images array
print(images_array.shape)