import numpy as np
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

num_classes = 82

# assume X_train and y_train are your training data
X_train = np.load('images_array.npy')
y_train = np.load('labels_array.npy')

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

# one-hot encode the labels
y_train = to_categorical(y_train, num_classes)

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, shuffle=True, random_state=42)

# shuffle only the training data
num_train_samples = len(X_train)
train_indices = np.arange(num_train_samples)
np.random.seed(42)
np.random.shuffle(train_indices)

X_train = X_train[train_indices]
y_train = y_train[train_indices]

# build and compile the model
model = tf.keras.Sequential([
    Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(45,45,1)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),

    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# fit the model using the training data and evaluate it using the testing data
model.fit(X_train, y_train, batch_size=120, epochs=10, validation_data=(X_test, y_test))

model.save('model.h5')