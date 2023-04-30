import numpy as np
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

num_classes = 82 

# assume X_train and y_train are your training data
X_train = np.load('images_array.npy')
y_train = np.load('labels_array.npy')

categories = ["-",",","!","(",")","[","]","{","}","+","=","0","1","2","3","4","5","6","7","8","9","A","alpha","ascii_124","b","beta","C","cos","d","Delta","div",
              "e","exists","f","forall","forward_slash","G","gamma","geq","gt","H","i","in","infty","int","j","k","l","lambda","ldots","leq","lim",
              "log","lt","M","mu","N","neq","o","p","phi","pi","pm","prime","q","R","rightarrow","S","sigma","sin","sqrt","sum","T","tan","theta",
              "times","u","v","w","X","y","z"]

# create dictionary mapping categories to numerical labels
label_dict = {cat: i for i, cat in enumerate(categories)}

# convert labels to numerical values
y_train = np.array([label_dict[label] for label in y_train])

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
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# fit the model using the training data and evaluate it using the testing data
model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))

model.save('model.h5')
