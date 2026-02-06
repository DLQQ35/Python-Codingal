import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\Understanding more about Data\\Titanic Dataset.csv')
titanic.head()
titanic.shape
print(titanic.shape)

titanic.isnull().sum()
print(titanic.isnull().sum())
sns.heatmap(titanic.isnull(), cbar=False, cmap='spring')
titanic.drop('Cabin', axis=1, inplace=True)
titanic.head()
titanic.dropna(inplace=True)
sns.heatmap(titanic.isnull(), cbar=False)
titanic.isnull().sum()
print(titanic.isnull().sum())

pd.get_dummies(titanic['Gender']).head()
sex = pd.get_dummies(titanic['Gender'], drop_first=True)
sex.head(4)
arked = pd.get_dummies(titanic['Embarked'], drop_first=True)
pclass = pd.get_dummies(titanic['Pclass'], drop_first=True)
pclass.head(4)
titanic = pd.concat([titanic, sex, pclass], axis=1)
titanic.head()
print(titanic.head())
plt.show()