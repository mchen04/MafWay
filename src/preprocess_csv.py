import os
import csv
from PIL import Image
import numpy as np

folder_path = '../CitrusHackProject/+/'
csv_path = '../CitrusHackProject/images_data.csv'

# open csv file for writing
with open(csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # loop through images in folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            # open image using PIL
            img = Image.open(os.path.join(folder_path, filename)).convert('L')

            # resize image to 28x28
            img = img.resize((28, 28))

            # convert image to numpy array
            img_array = np.array(img)

            # flatten image into a 1D array
            img_array = img_array.flatten()

            # write image array to csv file
            writer.writerow(img_array)
