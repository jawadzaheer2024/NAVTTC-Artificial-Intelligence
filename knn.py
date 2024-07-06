# Importing Necessary Libraries
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_dataset = load_iris()
X = iris_dataset.data
y = iris_dataset.target

# Visualize the dataset using histogram distributions
fig, ax = plt.subplots(2, 2, figsize=(12, 8))
for i, ax in enumerate(ax.flat):
    ax.hist(X[:, i], bins=20)
    ax.set_title(iris_dataset.feature_names[i])
plt.tight_layout()
plt.show()

# Visualize the dataset using scatter plots
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel(iris_dataset.feature_names[0])
plt.ylabel(iris_dataset.feature_names[1])
plt.show()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the KNN classifier
kn = KNeighborsClassifier()

# Train the classifier with the training data
kn.fit(X_train, y_train)

# Make predictions on the test data
predictions = kn.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = kn.score(X_test, y_test)
print("ACCURACY: " + str(accuracy))

# Print the predicted and actual species for each test data point
target_names = iris_dataset.target_names
for pred, actual in zip(predictions, y_test):
    print("Prediction is " + str(target_names[pred]) + ", Actual is " + str(target_names[actual]))
