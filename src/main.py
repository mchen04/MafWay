import numpy as np
import tensorflow as tf
from train_test_data import *
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

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

model.save('model.h5')
