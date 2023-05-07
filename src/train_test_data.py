import numpy as np
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization, Dropout
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from sklearn.model_selection import KFold

num_classes = 82

# assume X_train and y_train are your training data
X = np.load('images_array.npy')
y = np.load('labels_array.npy')

#define the object to use for data augmentation
datagen = ImageDataGenerator(
    rotation_range=30, # rotate the image by up to 30 degrees
    width_shift_range=0.1, # shift the image horizontally by up to 10% of the width
    height_shift_range=0.1, # shift the image vertically by up to 10% of the height
    shear_range=0.1, # apply shearing transformation with a maximum of 10% shear
    zoom_range=0.1, # zoom in/out of the image by up to 10%
)

#ensure the object is in the correct shape
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

# # split the data into training, validation, and testing sets
# #in general it is a 60, 20, 20 split
num_train_samples = int(0.6*num_samples) 
num_val_samples = int(0.2*num_samples)
num_test_samples = num_samples - num_train_samples - num_val_samples

X_val = X[num_train_samples:num_train_samples+num_val_samples]
y_val = y[num_train_samples:num_train_samples+num_val_samples]

#implement a kfold object
num_folds = 5

#initialize the kfold object
kf = KFold(n_splits=num_folds, shuffle=True)

# Initialize an empty list to store the accuracy scores for each fold
accuracy_scores = []
models = []

# Loop over each fold
for fold_idx, (train_index, test_index) in enumerate(kf.split(X)):
    print(f"Fold {fold_idx+1}...")
    # Split the data into training and test sets for this fold
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Initialize the CNN model
    model = tf.keras.Sequential([
        Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(45,45,1)),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2,2)),
        Conv2D(filters=64, kernel_size=(3,3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(pool_size=(2,2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.15),
        Dense(64, activation='relu'),
        Dropout(0.15),

        Dense(num_classes, activation='softmax')
    ])
    #.legacy is used for m1 & m2 macs as the non-legacy version is slower
    model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.001), 
                  loss='categorical_crossentropy', metrics=['accuracy']
                  )

    # Define the callback
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.25, patience=5, verbose=2, min_lr=0.00001)

    # Train the model
    history = model.fit(datagen.flow(X_train.reshape((-1, 45, 45, 1)), y_train, batch_size=64),
                        epochs=35,
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

    # Add the accuracy score to the list
    accuracy_scores.append(test_acc)
    models.append(model)

best_model_idx = np.argmax(accuracy_scores)
model = models[best_model_idx]

model.save("model.h5")

print("Model saved successfully")


