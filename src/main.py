import numpy as np
import tensorflow as tf
from preprocess_numpy import *
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# assume X_train and y_train are your training data
X_train = images_array 
y_train = np.ones(25112) 

# split the data into training and testing sets
num_samples = len(X_train)
indices = np.arange(num_samples)
np.random.shuffle(indices)

train_size = int(0.8*num_samples)
train_indices = indices[:train_size]
test_indices = indices[train_size:]

X_train_new = X_train[train_indices]
y_train_new = y_train[train_indices]
X_test = X_train[test_indices]
y_test = y_train[test_indices]

# build and compile the model
model = tf.keras.Sequential([
    Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# fit the model using the training data and evaluate it using the testing data
model.fit(X_train_new, y_train_new, batch_size=32, epochs=10, validation_data=(X_test, y_test))
