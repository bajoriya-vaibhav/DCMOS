# ## Importing necessary libraries

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score

# ## Loading the train dataset

train_file_path = '/kaggle/input/mlassign1/train.csv'  # Update the path if needed
train_data = pd.read_csv(train_file_path)

# ## Loading the test dataset

test_file_path = '/kaggle/input/mlassign1/test.csv'  # Test dataset path
test_data = pd.read_csv(test_file_path)

# ## Checking if 'id' column exists in the test dataset

if 'id' not in test_data.columns:
    test_data.insert(0, 'id', range(1, len(test_data) + 1))

# ## Removing duplicate values

train_data = train_data.drop_duplicates()

# ## Handling missing values

numeric_features = ['Feature1', 'Feature4']
imputer = SimpleImputer(strategy='mean')
train_data[numeric_features] = imputer.fit_transform(train_data[numeric_features])

# ## Handling missing values in test data similarly

test_data[numeric_features] = imputer.transform(test_data[numeric_features])

# ## Removing outliers using the IQR method

numeric_columns = train_data.select_dtypes(include=[np.number]).columns
Q1 = train_data[numeric_columns].quantile(0.25)
Q3 = train_data[numeric_columns].quantile(0.75)
IQR = Q3 - Q1

train_data = train_data[~((train_data[numeric_columns] < (Q1 - 1.5 * IQR)) | 
                          (train_data[numeric_columns] > (Q3 + 1.5 * IQR))).any(axis=1)]

# ## Splitting data into features and labels

X = train_data.drop('Label', axis=1)  # All features
y = train_data['Label']  # Target variable

# ## Performing train/test split

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=1)

# ## Processing the test dataset similarly

X_test = test_data.drop('Label', axis=1, errors='ignore')

# ## One-hot encoding categorical features

X_train = pd.get_dummies(X_train, columns=['Feature2'], drop_first=True)
X_val = pd.get_dummies(X_val, columns=['Feature2'], drop_first=True)
X_test = pd.get_dummies(X_test, columns=['Feature2'], drop_first=True)

# ## Making train, validation, and test data have the same columns after encoding

X_val = X_val.reindex(columns=X_train.columns, fill_value=0)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

# ## Polynomial Features

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_val_poly = poly.transform(X_val)
X_test_poly = poly.transform(X_test)

# ## Standardizing the features

scaler = StandardScaler()
X_train_poly = scaler.fit_transform(X_train_poly)
X_val_poly = scaler.transform(X_val_poly)
X_test_poly = scaler.transform(X_test_poly)

# ## Fit Lasso Regression model

lasso = Lasso(alpha=1)  # Fixed alpha value
lasso.fit(X_train_poly, y_train)

# ## Predictions on validation set

y_val_pred_lasso = lasso.predict(X_val_poly)

# ## Calculating R² score on validation set

r2_lasso = r2_score(y_val, y_val_pred_lasso)
print(f'R² Score for Lasso Regression on Validation Set: {r2_lasso}')

# ## Using the fitted model for final predictions

best_predictions = lasso.predict(X_test_poly)

# ## Preparing submission dataframe

submission = pd.DataFrame({
    'id': test_data['id'],
    'Label': best_predictions
})

# ## Saving to submission.csv

submission.to_csv('submission.csv', index=False)
print("successful")
