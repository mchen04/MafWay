from preprocess_numpy import *

# assume X_train and y_train are your training data
X_train = images_array 
y_train = np.ones(375974) 

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