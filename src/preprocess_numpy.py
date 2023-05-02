from PIL import Image
import numpy as np
import os

# specify path to folder containing images
# coud be '../CitrusHackProject/extracted_images/' based on your computer
folder_path = 'extracted_images'

# initialize empty list to store images
images = []
labels = []
image_categories = []

# create dictionary mapping categories to numerical labels
categories = ['!', '(', ')', '+', ',', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=','A', 'alpha', 'ascii_124', 'b', 'beta', 'C', 'cos', 'd', 'Delta', 
              'div', 'e', 'exists', 'f', 'forall', 'forward_slash','G', 'gamma', 'geq', 'gt', 'H', 'i', 'in', 'infty', 'int', 'j', 'k', 'l', 'lambda', 
              'ldots', 'leq', 'lim', 'log', 'lt', 'M', 'mu', 'N', 'neq', 'o', 'p', 'phi', 'pi', 'pm', 'prime', 'q', 'R', 'rightarrow', 'S', 'sigma', 
              'sin', 'sqrt', 'sum','T', 'tan', 'theta', 'times', 'u', 'v', 'w', 'X', 'y', 'z', '[', ']', '{', '}']

label_dict = {'!': 0, '(': 1, ')': 2, '+': 3, ',': 4, '-': 5, '0': 6, '1': 7, '2': 8, '3': 9, '4': 10, '5': 11, '6': 12, '7': 13, '8': 14, '9': 15, '=': 16, 'A': 17, 
              'alpha': 18, 'ascii_124': 19, 'b': 20, 'beta': 21, 'C': 22, 'cos': 23, 'd': 24, 'Delta': 25, 'div': 26, 'e': 27, 'exists': 28, 'f': 29, 'forall': 30, 
              'forward_slash': 31, 'G': 32, 'gamma': 33, 'geq': 34, 'gt': 35, 'H': 36, 'i': 37, 'in': 38, 'infty': 39, 'int': 40, 'j': 41, 'k': 42, 'l': 43, 
              'lambda': 44, 'ldots': 45, 'leq': 46, 'lim': 47, 'log': 48, 'lt': 49, 'M': 50, 'mu': 51, 'N': 52, 'neq': 53, 'o': 54, 'p': 55, 'phi': 56, 'pi': 57, 
              'pm': 58, 'prime': 59, 'q': 60, 'R': 61, 'rightarrow': 62, 'S': 63, 'sigma': 64, 'sin': 65, 'sqrt': 66, 'sum': 67, 'T': 68, 'tan': 69, 'theta': 70, 
              'times': 71, 'u': 72, 'v': 73, 'w': 74, 'X': 75, 'y': 76, 'z': 77, '[': 78, ']': 79, '{': 80, '}': 81}

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
            labels.append(label_dict[subfolder])

            # y_train values
            image_categories.append(subfolder)
    
    #prints progress
    print(subfolder)

# convert list of images to numpy array
images_array = np.array(images)
labels_array = np.array(labels)

# normalize pixel values
images_array = images_array / 255.0 

# save the array to a file
np.save('images_array.npy', images_array)
np.save('labels_array.npy', labels_array)

print("completed")