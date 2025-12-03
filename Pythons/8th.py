import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Minimal DataFrame with website traffic data
data = {
    'Date': ['2024-07-01', '2024-07-02', '2024-07-03'],
    'Visitors': [120, 150, 170],
    'Source': ['Direct', 'Search', 'Social'],
    'DayType': ['Weekday', 'Weekday', 'Weekend']
}
df = pd.DataFrame(data)

# Line Plot: Daily number of visitors
sns.lineplot(x='Date', y='Visitors', data=df, marker='o')
plt.title('Daily Number of Visitors')
plt.show()

# Bar Plot: Compare visitors on weekdays vs weekends
sns.barplot(x='DayType', y='Visitors', data=df,errorbar=None)
plt.title('Visitors: Weekdays vs Weekends')
plt.show()

# Pie Chart: Traffic sources distribution
df['Source'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie chart")
plt.ylabel('')  # Hide y-label for better appearance
plt.show()
