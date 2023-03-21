import numpy as np
import matplotlib.pyplot as plt
import matplotlib

data = [1,8,15,7,5,14,43,40]
labels = ["Los Angeles 1984", "Seoul 1988", "Barcelona 1992", "Atlanta 1996", "Sydney 2000", "Athens 2003", "Beijing 2008", "London 2012"]
colors = ["lightcoral","gold", "yellowgreen", "lightgreen", "lightseagreen", "deepskyblue", "dodgerblue", "mediumpurple"]

plt.bar(range(len(data)),data,color=colors,width=0.5)
plt.xticks(range(len(data)),labels)
plt.xlabel("Olympic Games")
plt.ylabel("Costs")
plt.show()

sort() and ()
reverse()
costs=[1,8,15,7,5,14,43,40]
sorted(costs)
costs=sorted(costs)
costs.sort()
costs.reverse()
