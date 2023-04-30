from PIL import Image
import numpy as np
import os
import random
from keras.utils import to_categorical

# specify path to folder containing images
folder_path = '../CitrusHackProject/extracted_images/'

# initialize empty list to store images
images = []
labels = []
image_categories = []

# create dictionary mapping categories to numerical labels
categories = ["-","!","(",")","[","]","+","=","0","1","2","3","4","5","6","7","8","9","A","b","C","cos","d","div",
              "e","f","forward_slash","G","H","i","in","infty","int","j","k","l","lim",
              "log","M","N","o","p","pi","q","R","rightarrow","S","sigma","sin","sqrt","sum","T","tan","theta",
              "times","u","v","w","X","y","z"]
label_dict = {"-": 0, "!": 1, "(": 2, ")": 3, "[": 4, "]": 5, "+": 6, "=": 7, "0": 8, "1": 9, "2": 10, "3": 11, "4": 12, "5": 13, "6": 14, 
              "7": 15, "8": 16, "9": 17, "A": 18, "b": 19, "C": 20, "cos": 21, "d": 22, "div": 23, "e": 24, "f": 25, "forward_slash": 26, "G": 27, "H": 28, "i": 29, "in": 30, "infty": 31, "int": 32, 
              "j": 33, "k": 34, "l": 35, "lim": 36, "log": 37, "M": 38, "N": 39, "o": 40, "p": 41, "pi": 42, "q": 43, "R": 44, "rightarrow": 45, "S": 46, "sigma": 47, "sin": 48, "sqrt": 49, "sum": 50, "T": 51, "tan": 52,
              "theta": 53, "times": 54, "u": 55, "v": 56, "w": 57, "X": 58, "y": 59, "z": 60}

i = 0
# loop through subfolders in folder
for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)
    # loop through images in subfolder
    for filename in os.listdir(subfolder_path):
        if filename.endswith('.jpg'):
            # open image using PIL
            img = Image.open(os.path.join(subfolder_path, filename)).convert('L')

            # convert image to numpy array
            img_array = np.array(img)

            # append image array to list
            images.append(img_array)

            # append label to list
            labels.append(i)

            # y_train values
            image_categories.append(subfolder)
    
    i = i + 1

# convert list of images to numpy array
images_array = np.array(images)
labels_array = np.array(image_categories)

# normalize pixel values
images_array = images_array / 255.0 

np.set_printoptions(precision=0)
images_array = np.round(images_array).astype(int)

# save the array to a file
np.save('images_array.npy', images_array)
np.save('labels_array.npy', labels_array)

print("completed")