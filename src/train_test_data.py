import numpy as np
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau

num_classes = 82

# assume X_train and y_train are your training data
X_train = np.load('images_array.npy')
y_train = np.load('labels_array.npy')

datagen = ImageDataGenerator(
    rotation_range=30, # rotate the image by up to 30 degrees
    width_shift_range=0.1, # shift the image horizontally by up to 10% of the width
    height_shift_range=0.1, # shift the image vertically by up to 10% of the height
    shear_range=0.1, # apply shearing transformation with a maximum of 10% shear
    zoom_range=0.1, # zoom in/out of the image by up to 10%
)

datagen.fit(X_train.reshape((-1, 45, 45, 1)))

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

reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5, verbose=1, min_lr=0.00001)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# fit the model using the training data and evaluate it using the testing data
model.fit(datagen.flow(X_train.reshape((-1, 45, 45, 1)), y_train, batch_size=32), epochs=20, validation_data=(X_test, y_test), callbacks=[reduce_lr])

model.save('model.h5')
