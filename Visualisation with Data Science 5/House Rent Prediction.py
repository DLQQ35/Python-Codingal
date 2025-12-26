import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

HouseDF = pd.read_csv("C:\\Users\\jiten\\OneDrive\\Desktop\\Python Codingal\\Visualisation with Data Science 5\\USA_Housing.csv")
HouseDF.head()
HouseDF.info()
HouseDF.describe()
HouseDF.columns

sns.pairplot(HouseDF)

sns.heatmap(HouseDF.select_dtypes(include=np.number).corr(), annot=True)

plt.show()