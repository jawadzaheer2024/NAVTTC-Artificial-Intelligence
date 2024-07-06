#calculate mean

import pandas as pd
iris=pd.read_csv("D:\\HITECH NAVTTC\\LECTURES\\used_device_data.csv")

# for each feature

iris=iris.drop(["device_brand","os","4g","5g"], axis=1)
# Remove rows with null values
iris = iris.dropna()
mean=iris.mean()
print(mean)

#calculate median
median_values = iris.median()
print("Median:\n", median_values)

#for each feature
median=iris.median()
print(median)

#Calculate mode for each feature
mode_values = iris.mode()
print("Mode:\n", mode_values)

#Check for multiple modes

for column in iris:  # Exclude the 'species' column
    modes = iris[column].mode()
    if len(modes) > 1:
        print(f"{column} is multimodal: {modes.tolist()}")
    else:
        print(f"{column} is unimodal: {modes[0]}")

#Range and Variance
# Calculate range for each feature
range_values = iris.max() - iris.min()
print("Range:\n", range_values)


# Calculate variance for each feature
variance_values = iris.var()
print("Variance:\n", variance_values)

#Calculate standard deviation for each feature
std_dev_values = iris.std()
print("Standard Deviation:\n", std_dev_values)

# Calculate the 25th, 50th, and 75th percentiles for each feature
percentiles = iris.quantile([0.25, 0.5, 0.75])
print("Percentiles:\n", percentiles)



# Calculate correlation matrix
correlation_matrix = iris.corr()
print("Correlation Matrix:\n", correlation_matrix)


#Calculate covariance matrix
covariance_matrix = iris.cov()
print("Covariance Matrix:\n", covariance_matrix)



