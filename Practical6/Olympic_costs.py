#print a list of sorted vlue for the cost of hosting the Olympic games
#Enter the value of costs
costs=[1,8,15,7,5,14,43,40]
#Enter the value of costs
costs.sort()
print(costs)

#a bar plot displaying this sorted distribution of marks
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#Enter the value of costs in ascending order
data = [1,5,7,8,14,15,40,43]
#Add the city and year corresponding to costs
labels = ["Los Angeles 1984", "Sydney 2000", "Atlanta 1996", "Seoul 1988", "Athens 2003", "Barcelona 1992", "London 2012", "Beijing 2008"]
colors = ["lightcoral","gold", "yellowgreen", "lightgreen", "lightseagreen", "deepskyblue", "dodgerblue", "mediumpurple"]
#Use the values entered above and the elements to start drawing
#Ensure the output of the bars
plt.bar(range(len(data)),data,color=colors,width=0.5)
plt.xticks(range(len(data)),labels)
#Determine what the horizontal axis and the vertical axis look like
plt.xlabel("Olympic Games")
plt.ylabel("Costs")
plt.show()


