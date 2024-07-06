# Import necessary libraries
import numpy as np
import pandas as pd
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB

# Load the data
data = pd.read_csv('D:\\HITECH NAVTTC\\LECTURES\\breast-cancer.csv')  # Replace with your regression dataset path
print(data.head())

# Prepare the data
x = data.drop(['id', 'diagnosis'], axis=1)  # Replace 'target' with your actual target column name
y = data['diagnosis']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# Standardize the features
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

print(x_train)
print(x_test)

# Train the K-Nearest Neighbors regressor
gnb = GaussianNB()
gnb.fit(x_train, y_train)

# Make predictions
predictions = gnb.predict(x_test)
print(predictions)
print("Accuracy: ",accuracy_score(y_test,predictions))

print("Confudion Matrix: ",confusion_matrix(y_test,predictions))

