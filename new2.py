# a. Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# b. Read the CSV file
dataset = pd.read_csv("iris_data.csv")
print(dataset.head())

# c. Data preprocessing
# Check for missing values
print(dataset.isnull().sum())

# Imputation of missing values
dataset['Gender'].fillna(dataset['Gender'].mode()[0], inplace=True)
dataset['Married'].fillna(dataset['Married'].mode()[0], inplace=True)
dataset['Dependents'].fillna(dataset['Dependents'].mode()[0], inplace=True)
dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0], inplace=True)
dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0], inplace=True)
dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0], inplace=True)
dataset['LoanAmount'].fillna(dataset['LoanAmount'].median(), inplace=True)

# Check missing values after imputation
print(dataset.isnull().sum())

# Drop unnecessary columns
dataset.drop(columns=['Loan_ID'], inplace=True)

# d. Exploratory Data Analysis
# I. Dataset shape
print(dataset.shape)

# II. Dataset info
print(dataset.info())

# III. Gender obtaining the maximum number of loans
sns.countplot(y='Gender', hue='Loan_Status', data=dataset)
plt.show()
print(dataset['Gender'].value_counts())

# IV. Does marital status affect loan approval?
sns.countplot(y='Married', hue='Loan_Status', data=dataset)
plt.show()

# V. Does education status affect loan approval?
sns.countplot(y='Education', hue='Loan_Status', data=dataset)
plt.show()

# VI. Does employment affect loan approval?
sns.countplot(y='Self_Employed', hue='Loan_Status', data=dataset)
plt.show()

# VII. Does credit history affect loan approval?
sns.countplot(y='Credit_History', hue='Loan_Status', data=dataset)
plt.show()

# e. Model Building
# Label encoding for categorical variables
gender = {"Female": 0, "Male": 1}
yes_no = {'No': 0, 'Yes': 1}
dependents = {'0': 0, '1': 1, '2': 2, '3+': 3}
education = {'Not Graduate': 0, 'Graduate': 1}
property = {'Semiurban': 0, 'Urban': 1, 'Rural': 2}
output = {"N": 0, "Y": 1}

dataset['Gender'] = dataset['Gender'].replace(gender)
dataset['Married'] = dataset['Married'].replace(yes_no)
dataset['Dependents'] = dataset['Dependents'].replace(dependents)
dataset['Education'] = dataset['Education'].replace(education)
dataset['Self_Employed'] = dataset['Self_Employed'].replace(yes_no)
dataset['Property_Area'] = dataset['Property_Area'].replace(property)
dataset['Loan_Status'] = dataset['Loan_Status'].replace(output)

# Dataset after converting object data types into integers
print(dataset.head())

# f. Set the values for independent (X) and dependent (Y) variables
X = dataset.drop('Loan_Status', axis=1)
Y = dataset['Loan_Status']

# g. Split the dataset into train and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# Standardizing the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# h. Fit the KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)

# i. Prediction on the test set
prediction_knn = knn.predict(X_test)
print("Prediction for test set: {}".format(prediction_knn))

# j. Get the Actual values and the predicted values
results = pd.DataFrame({'Actual value': Y_test, 'Predicted value': prediction_knn})
print(results.head())

# k. Evaluate the Model
print("Confusion Matrix:\n", confusion_matrix(Y_test, prediction_knn))
print("\nClassification Report:\n", classification_report(Y_test, prediction_knn))
print("\nAccuracy Score:", accuracy_score(Y_test, prediction_knn))
