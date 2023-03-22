#create a dictionary
#Store different types of movies and their corresponding data in this dictionary
dict={"Comedy":"73", "Action":"42", "Romance":"38", "Fantasy":"28", "Science-fiction":"22", "Horror":"19", "Crime":"18", "Documentary":"12", "History":"8", "War":"7"}

#create and print a dictionary in Python to record these data and construct a pie chart from the data
#use pyplot in matplotlib
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = list(dict.keys())
#input the sizes, colors,explode
sizes = list(dict.values())
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink', 'lightsteelblue', 'aquamarine', 'thistle', 'mediumpurple', 'silver'
explode = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()

#The number	of university students who prefer a	movie	genre	taken	from the input list
#use the dictionary I created
genres=dict["Comedy"]
print(genres)







