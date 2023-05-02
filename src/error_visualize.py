import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Load the model and the data
model = tf.keras.models.load_model('model.h5')

X_test = np.load('X_test.npy')
y_test = np.load('y_test.npy')

# Make predictions on the test data
y_pred = model.predict(X_test)

y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)

# Find the indices of misclassified examples
misclassified_indices = np.where(np.argmax(y_pred, axis=1) != np.argmax(y_test, axis=1))[0]

# Randomly select 10 misclassified examples and plot them
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    idx = np.random.choice(misclassified_indices)
    ax.imshow(X_test[idx], cmap='gray')
    ax.set_title(f'True: {np.argmax(y_test[idx])}, Pred: {np.argmax(y_pred[idx])}')
    ax.axis('off')
    
plt.tight_layout()
plt.show()
