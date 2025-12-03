import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("s.csv")

plt.figure(figsize=(12,6))
sn.boxplot(data = df[['Maths','Physics','Chemistry','English','Biology']])
plt.title("Distribution of marks")
plt.xlabel("Subjects")
plt.ylabel("Grades")
plt.savefig("Saved.png")
print("Image saved")