import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("dataset.csv")

# Sort the data based on the 'Growth' column in ascending order
data.sort_values(by=['Growth'], ascending=True, inplace=True)

# Plot the bar chart
plt.bar(data['Domain'], data['Growth'], color='skyblue')
plt.title('Growth by Domain - Bar Chart')
plt.xlabel('Domain')
plt.ylabel('Growth')
plt.show()

# Plot the histogram for 'Growth' data
plt.hist(data['Growth'], bins=10, color='orange', edgecolor='black')
plt.title('Histogram of Growth')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.show()
