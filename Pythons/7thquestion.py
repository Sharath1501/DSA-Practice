import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = {
    'maths':[23,45,67,87,66,55,43,34],
    'englsih':[24,75,87,47,26,75,93,54],
    'science':[24,65,87,17,26,95,43,94]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,6))
sns.boxplot(data = df)
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x='maths',y='science',data = df)
plt.show()
df['Overall']=df.mean(axis = 1)

plt.figure(figsize=(8,6))
sns.histplot(df['Overall'],bins =5 ,kde=True)
plt.show()