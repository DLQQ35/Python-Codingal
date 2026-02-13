import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\After-Class Projects\\Titanic Dataset.csv')

df.head()
df.isnull().sum()
df.dropna()
df.isnull().sum()

plt.figure()
sns.countplot(x='Survived', data=df)
plt.title("Survived vs Dead")
plt.show()

male_data = df[df['Gender'] == 'male']
plt.figure()
sns.countplot(x='Survived', data=male_data)
plt.title("Survived Males")
plt.show()

female_data = df[df['Gender'] == 'female']
plt.figure()
sns.countplot(x='Survived', data=female_data)
plt.title("Survived Females")
plt.show()

plt.figure()
sns.countplot(x='Pclass', hue = 'Survived', data=df)
plt.title("Survived vs Class")
plt.show()