from PIL import Image
import numpy as np
import os
from keras.utils import to_categorical

# specify path to folder containing images
folder_path = '../CitrusHackProject/extracted_images/'

# initialize empty list to store images
images = []
labels = []
image_categories = []

# create dictionary mapping categories to numerical labels
categories = ["-",",","!","(",")","[","]","{","}","+","=","0","1","2","3","4","5","6","7","8","9","A","alpha","ascii_124","b","beta","C","cos","d","Delta","div","e", 
              "exists","f","forall","foward_slash","G","gamma","geq","gt","H","i","in","infty","int","j","k","l","lambda","idots","leq","lim","log","lt","M","mu","N", 
              "neq","o","p","phi","pi","pm","prime","q","R","rightarrow","S","sigma","sin","sqrt","sum","T","tan","theta","times","u","v","w","X","y","z"]
label_dict = {"-": 0, ",": 1, "!": 2, "(": 3, ")": 4, "[": 5, "]": 6, "{": 7, "}": 8, "+": 9, "=": 10, "0": 11, "1": 12, "2": 13, "3": 14, "4": 15, "5": 16, "6": 17, 
              "7": 18, "8": 19, "9": 20, "A": 21, "alpha": 22, "ascii_124": 23, "b": 24, "beta": 25, "C": 26, "cos": 27, "d": 28, "Delta": 29, "div": 30, "e": 31,
                "exists": 32, "f": 33, "forall": 34, "forward_slash": 35, "G": 36, "gamma": 37, "geq": 38, "gt": 39, "H": 40, "i": 41, "in": 42, "infty": 43, "int": 44, 
                "j": 45, "k": 46, "l": 47, "lambda": 48, "ldots": 49, "leq": 50, "lim": 51, "log": 52, "lt": 53, "M": 54, "mu": 55, "N": 56, "neq": 57, "o": 58, "p": 59, 
                "phi": 60, "pi": 61, "pm": 62, "prime": 63, "q": 64, "R": 65, "rightarrow": 66, "S": 67, "sigma": 68, "sin": 69, "sqrt": 70, "sum": 71, "T": 72, "tan": 73,
                  "theta": 74, "times": 75, "u": 76, "v": 77, "w": 78, "X": 79, "y": 80, "z": 81}

i = 0

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

# reshape array and convert values to integers
images_array = np.reshape(images_array, (len(images), 28, 28, 1))
np.set_printoptions(precision=0)
images_array = np.round(images_array).astype(int)

# print shape of images array, y_train, and one-hot labels array

# save the array to a file
np.save('images_array.npy', images_array)
np.save('labels_array.npy', labels_array)

print(images_array.shape)
print(labels_array.shape)
