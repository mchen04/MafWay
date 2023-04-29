from keras.models import load_model
from train_test_data import *

model = load_model('model.h5')

# generate predictions on test data
predictions = model.predict(X_test)

# convert predicted labels from one-hot encoding to integers
#predictions_int = np.argmax(predictions, axis=1)

# compare predicted labels with true labels
accuracy = np.mean(predictions == y_test)

# print accuracy
print("Accuracy: ", accuracy)
