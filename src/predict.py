from keras.models import load_model
from train_test_data import *

model = load_model('model.h5')

# generate predictions on test data
predictions = model.predict(X_test)

# compare predicted labels with true labels
accuracy = np.mean(predictions == y_test)

# print accuracy
print("Accuracy: ", accuracy)
