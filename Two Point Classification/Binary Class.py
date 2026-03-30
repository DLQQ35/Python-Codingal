import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\Two Point Classification\\insurance_data.csv')
df.head()

plt.scatter(df.age, df.bought_insurance, marker='+', color='red')

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size=0.8)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train, y_train)
y_predicted = model.predict(X_test) 
model.predict_proba(X_test)
model.score(X_test, y_test)

import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def predict_function(age):
    z =  0.042 * age + model.intercept_[0]
    y = sigmoid(z)
    return y

age = 35
print(predict_function(age))
age = 43
print(predict_function(age))
plt.show()