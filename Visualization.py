import pandas as pd
import matplotlib.pyplot as plt

#filtering the data 
data = pd.read_csv("dataset.csv")

#sorting the data  based on the growth
data.sort_values(by=['Growth'],ascending=True,inplace=True)

#plotting the bar chart
plt.bar(data['Domain'],data['Growth'])

#giving the title to the bar chart
plt.title('Bar chart')

#labelling the bar chart
plt.xlabel('Domain')
plt.ylabel('Growth')

#showing the bar chart
plt.show()