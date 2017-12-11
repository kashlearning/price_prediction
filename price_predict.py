import pandas as pd
from sklearn.preprocessing import Imputer

train_data = pd.read_pickle("train.pkl")

# print(train_data.isnull().sum()) # to get the no. of missing values in each columns

# Taking care of the missing values


x_train = train_data.iloc[:, train_data.columns != 'price'].values
y_train = train_data.iloc[:, 5].values

