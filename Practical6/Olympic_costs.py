#make a dictionary
dict={'Los Angeles 1984':1, 'Seoul 1988':8, 'Barcelona 1992':15, 'Atlanta 1996':7, 'Sydney 2000':5, 'Athens 2003':14, 'Beijing 2008':43, 'London 2012':40}

#print a list of sorted vlue for the cost of hosting the Olympic games
#Enter the value of costs
costs=[1,8,15,7,5,14,43,40]
#Put the values of costs in ascending order and print them out
costs.sort()
print(costs)


#a bar plot displaying this sorted distribution of marks
#Define the city and the cost
cities = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']
costs = [1,8,15,7,5,14,43,40]
#import the methods to be used
import numpy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#Enter the value of costs in ascending order 
#Add the city and year corresponding to costs
cities = numpy.array(cities)
costs = numpy.array(costs)
inds = costs.argsort()
sortedcities = cities[inds]
print(sortedcities)
#Import the cities into the lables
labels = sortedcities
#Import the value of the ascending costs into the data
costs.sort()
data = costs
#Define the colors of bars
colors = ["lightcoral","gold", "yellowgreen", "lightgreen", "lightseagreen", "deepskyblue", "dodgerblue", "mediumpurple"]
#Use the values entered above and the elements to start drawing
#Ensure the output of the bars
plt.bar(range(len(data)),data,color=colors,width=0.5)
plt.xticks(range(len(data)),labels)
#Determine what the horizontal axis and the vertical axis look like
plt.xlabel("Olympic Games")
plt.ylabel("Costs")
plt.show()


