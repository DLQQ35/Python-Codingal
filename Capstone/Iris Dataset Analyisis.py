import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\Capstone\\heart.csv')

df.head()

df.shape

df.columns

df.describe

df.isnull().sum()

print(df.info())

plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.show()

df.hist(figsize=(12,12), layout=(5,3))
plt.show()

df.plot(kind='box', subplots=True, layout=(5,3), figsize=(12,12))
plt.show()

sns.barplot(data=df, x='sex', y='chol', hue='target', palette='spring')
plt.show()

df["sex"].value_counts()

df["target"].value_counts()

df["thal"].value_counts()

sns.countplot(x="sex", data=df, palette="husl", hue="target")
plt.show()

sns.countplot(x="target", palette="BuGn", data=df)
plt.show()

sns.countplot(x="ca", hue="target", data=df)
plt.show()