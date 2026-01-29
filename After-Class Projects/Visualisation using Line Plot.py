import pandas as pd
import matplotlib.pyplot as plt

july_data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "New Births": [12, 15, 11, 9, 1, 9, 21]
}

df_july = pd.DataFrame(july_data)
print(df_july)

plt.figure()
plt.plot(df_july["Day"], df_july["New Births"])
plt.title('July Birth Rate')
plt.xlabel('Days')
plt.ylabel('New Births')
plt.show()