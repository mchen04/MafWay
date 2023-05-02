import numpy as np
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
import matplotlib.pyplot as plt

num_classes = 82

# assume X and y are your data and labels
X = np.load('images_array.npy')
y = np.load('labels_array.npy')

datagen = ImageDataGenerator(
    rotation_range=30, # rotate the image by up to 30 degrees
    width_shift_range=0.1, # shift the image horizontally by up to 10% of the width
    height_shift_range=0.1, # shift the image vertically by up to 10% of the height
    shear_range=0.1, # apply shearing transformation with a maximum of 10% shear
    zoom_range=0.1, # zoom in/out of the image by up to 10%
)

datagen.fit(X.reshape((-1, 45, 45, 1)))

# one-hot encode the labels
y = to_categorical(y, num_classes)

# shuffle the data
num_samples = len(X)
indices = np.arange(num_samples)
np.random.seed(42)
np.random.shuffle(indices)

X = X[indices]
y = y[indices]

# split the data into training, validation, and testing sets
num_train_samples = int(0.6*num_samples)
num_val_samples = int(0.2*num_samples)
num_test_samples = num_samples - num_train_samples - num_val_samples

X_train = X[:num_train_samples]
y_train = y[:num_train_samples]

X_val = X[num_train_samples:num_train_samples+num_val_samples]
y_val = y[num_train_samples:num_train_samples+num_val_samples]

X_test = X[num_train_samples+num_val_samples:]
y_test = y[num_train_samples+num_val_samples:]

# build and compile the model
model = tf.keras.Sequential([
    Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(45,45,1)),
    BatchNormalization(),
    Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    BatchNormalization(),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    Conv2D(filters=128, kernel_size=(3,3), activation='relu'),
    BatchNormalization(),
    Conv2D(filters=128, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Define the callback
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5, verbose=1, min_lr=0.00001)

import numpy as np
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
import matplotlib.pyplot as plt

num_classes = 82

# assume X and y are your data and labels
X = np.load('images_array.npy')
y = np.load('labels_array.npy')

datagen = ImageDataGenerator(
    rotation_range=30, # rotate the image by up to 30 degrees
    width_shift_range=0.1, # shift the image horizontally by up to 10% of the width
    height_shift_range=0.1, # shift the image vertically by up to 10% of the height
    shear_range=0.1, # apply shearing transformation with a maximum of 10% shear
    zoom_range=0.1, # zoom in/out of the image by up to 10%
)

datagen.fit(X.reshape((-1, 45, 45, 1)))

# one-hot encode the labels
y = to_categorical(y, num_classes)

# shuffle the data
num_samples = len(X)
indices = np.arange(num_samples)
np.random.seed(42)
np.random.shuffle(indices)

X = X[indices]
y = y[indices]

# split the data into training, validation, and testing sets
num_train_samples = int(0.6*num_samples)
num_val_samples = int(0.2*num_samples)
num_test_samples = num_samples - num_train_samples - num_val_samples

X_train = X[:num_train_samples]
y_train = y[:num_train_samples]

X_val = X[num_train_samples:num_train_samples+num_val_samples]
y_val = y[num_train_samples:num_train_samples+num_val_samples]

X_test = X[num_train_samples+num_val_samples:]
y_test = y[num_train_samples+num_val_samples:]

# build and compile the model
model = tf.keras.Sequential([
    Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(45,45,1)),
    BatchNormalization(),
    Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    BatchNormalization(),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    Conv2D(filters=128, kernel_size=(3,3), activation='relu'),
    BatchNormalization(),
    Conv2D(filters=128, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Define the callback
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5, verbose=2, min_lr=0.00001)

# Train the model
history = model.fit(datagen.flow(X_train.reshape((-1, 45, 45, 1)), y_train, batch_size=32),
                    epochs=20,
                    validation_data=(X_val.reshape((-1, 45, 45, 1)), y_val),
                    callbacks=[reduce_lr])

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test.reshape((-1, 45, 45, 1)), y_test)

# Print the validation loss, validation accuracy, test loss, and test accuracy for each epoch
for i, acc in enumerate(history.history['accuracy']):
    val_acc = history.history['val_accuracy'][i]
    val_loss = history.history['val_loss'][i]
    train_loss = history.history['loss'][i]
    train_acc = history.history['accuracy'][i]
    print(f"Epoch {i+1}: val_loss={val_loss:.4f}, val_acc={val_acc:.4f}, " 
          f"train_loss={train_loss:.4f}, train_acc={train_acc:.4f}, " 
          )

'''
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test loss:', test_loss)
print('Test accuracy:', test_acc)

# Find epoch where validation accuracy is highest
best_epoch = np.argmax(history.history['val_accuracy']) + 1
print('Best epoch:', best_epoch)

# Evaluate model on test set at best epoch
model.load_weights('model.h5')  # Load weights at best epoch

# Check when cross-validation error crosses testing error
for epoch in range(1, len(history.history['val_loss']) + 1):
    val_loss = history.history['val_loss'][epoch-1]
    test_loss_at_epoch = model.evaluate(X_test, y_test, verbose=0)[0]
    if val_loss > test_loss_at_epoch:
        print(f"Cross-validation error ({val_loss:.4f}) crossed testing error ({test_loss_at_epoch:.4f}) at epoch {epoch}")
        break

test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test loss at best epoch:', test_loss)
print('Test accuracy at best epoch:', test_acc)
'''
