import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('survey_data.csv')

# Bar chart - Satisfaction vs Count
satisfaction_counts = df['Satisfaction'].value_counts()
satisfaction_counts.plot(kind='bar', color='green')
plt.title('Satisfaction Count')
plt.xlabel('Satisfaction')
plt.ylabel('Number of Responses')
plt.tight_layout()
plt.savefig('bar_satisfaction.png')
plt.show()

# Pie chart - Platform Preference
platform_counts = df['PreferredPlatform'].value_counts()
platform_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Preferred Platforms')
plt.ylabel('')
plt.tight_layout()
plt.savefig('pie_platform.png')
plt.show()

# Heatmap - Ratings by Platform
pivot = df.pivot_table(values='Rating', index='PreferredPlatform', columns='Satisfaction')
sns.heatmap(pivot, annot=True, cmap='coolwarm')
plt.title('Ratings Heatmap: Platform vs Satisfaction')
plt.tight_layout()
plt.savefig('heatmap_rating.png')
plt.show()
