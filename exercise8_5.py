# TASK: ask the user for a list of numbers,
# and create a bar chart based on them

import matplotlib.pyplot as plt
import seaborn as sns


# values for x-axis
x=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# valueds for y-axis
y=[10.5, 12.5, 11.4, 11.2, 9.2, 14.5, 10.1]
# plotting with seaborn
my_plot = sns.barplot(y)
# assigning x-axis and y-axis labels
my_plot.set(xlabel ='Day Names', ylabel ='Turn Over (In Million Dollars)')
# assigning plot title
plt.title('Scatter Plot');
# function to show plot
plt.show()