# Import necessary libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv(r'D:\\HITECH NAVTTC\\LECTURES\\Iris - all-numbers.csv')  # Replace with your regression dataset path
print(data.head())

# Prepare the data
x = data.drop('species', axis=1)  # Replace 'target' with your actual target column name
y = data['species']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Standardize the features
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

print(x_train)
print(x_test)

# Train the K-Nearest Neighbors regressor
regressor = KNeighborsRegressor(n_neighbors=3)
regressor.fit(x_train, y_train)

# Make predictions
predictions = regressor.predict(x_test)
print(predictions)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
