#create and print a dictionary in Python to record these data and construct a pie chart from the data
#use pyplot in matplotlib
import matplotlib.pyplot as plt
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Comedy', 'Action', 'Romance', 'Fantacy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
sizes = [27.34, 15.73, 14.23, 10.49, 8.23, 7.12, 6.74, 4.49, 3.00, 2.63]
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink', 'lightsteelblue', 'aquamarine', 'thistle', 'mediumpurple', 'silver'
explode = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()

#create a dictionary
my_dict={}
genes={'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, "Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War':7}

