import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\ANN Implementation using Keras-1\\Churn_Modelling.csv')
df.head()
df.info()
df.describe()

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])
print(df.head())
print(df.info())

df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
df.shape

y = df.pop('Exited')
x = df

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
x_train