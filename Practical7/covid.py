# import a new oython libraries
# os allows us to work with files and directories, and pandas is for working with dataframes.
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/Downloads")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
# know the type of the data points, name of the columns, number of rows in the data
covid_data.describe()
# learn the count, mean, standard deviation, minimum, percentile, maximum of the data
covid_data.iloc[0,1]
# shows what's in the first row, second column
covid_data.iloc[2,0:5]
# show the data in row 2, column from 0 to 5
covid_data.iloc[0:2,:]
# row from 0 to 2, print all the column
covid_data.iloc[0:10:2,0:5]
# row: from 0 to 10, only print odd-numbered line, column:from 0 to 5
covid_data.iloc[0:1001:100,1]
print(covid_data.iloc[0:3,[0,1,3]])
# The first three rows are expected to see, but only the first, second, and fourth column, are shown
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3,my_columns])
# use Boolean index to get the same outcome as just insert numbers
print(covid_data.loc[2:4,"date"])
# print the date from row 2 to 4
covid_data.loc[0:12,"total_cases"]
covid_data.loc[0:81,"total_cases"]
Afghanistan = covid_data.loc[covid_data.loc[:,"location"]=="Afghanistan","total_cases"]
# Only extract the row with Afghanistan
print(Afghanistan)
my_columns=[True, False, True, True, False, False]
print(covid_data)
new_data = covid_data.loc[covid_data["date"]=="2020-03-31",["location","new_cases","new_deaths"]]
# The data of location, new_cases and new_deaths with date 2022-03-31 were screened
print(new_data)
# Print out the result
import numpy as np
my_columns=[False,False,True,True,False,False]
# Sort out the columns I want to maintain, "new_cases","new_deaths"

# Use numpy to compute the mean new cases and new deaths on this date.
column1=[False,True,False]
# Select out the column of new_cases
a=np.mean(new_data.loc[new_data["location"]!="World",column1])
# Get rid of the world value
print(a)
column2=[False,False,True]
# Select out the column of new_cases
b=np.mean(new_data.loc[new_data["location"]!="World",column2])
# Get rid of the world value
print(b)
import matplotlib.pyplot as plt
import numpy as np
labels = 'new_cases'
data1 = new_data.loc[new_data["location"]!="World",column1]
# Import data
plt.grid(True)
# Display grid
plt.boxplot(data1.values,
            showfliers=False)
# Plot box plot
plt.title('Box Plot new_cases')
plt.xlabel('Data')
plt.ylabel('Values')
# Add title and axis labels
plt.show()

import matplotlib.pyplot as plt
import numpy as np
labels = 'new_cases'
data2 = new_data.loc[new_data["location"]!="World",column2]
# Import data
plt.grid(True)
# Display grid
plt.boxplot(data2.values,
            showfliers=False)
# Plot box plot
plt.title('Box Plot new_deaths')
plt.xlabel('Data')
plt.ylabel('Values')
# Add title and axis labels
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Read data in Excel
world_date=covid_data.loc[covid_data["location"]== 'World',"date"]
world_new_cases=covid_data.loc[covid_data["location"]== 'World',"new_cases"]
print(world_date)
print(world_new_cases)
# Drawing
plt.plot(world_date, world_new_cases, 'c+')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.title('New cases in the world')
plt.show()

import matplotlib.pyplot as plt
world_date=covid_data.loc[covid_data["location"]== 'World',"date"]
world_new_deaths=covid_data.loc[covid_data["location"]== 'World',"new_deaths"]

# Drawing
plt.plot(world_date, world_new_deaths,'b+')
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.title('New deaths in the world')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Select the data about Austria from the table
x = covid_data.loc[covid_data["location"]== 'Austria',"date"]
y1 = covid_data.loc[covid_data["location"]== 'Austria',"total_cases"]
y2 = covid_data.loc[covid_data["location"]== 'Austria',"total_deaths"]

# Drawing plot
plt.scatter(x, y1, label='total_cases', c='b')
plt.scatter(x, y2, label='total_deaths', c='r')
plt.xticks(world_date.iloc[0:len(x):4],rotation=-90)

# Add som elements to the plot
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Total cases and deaths in Austria')
plt.legend()

# Display plot
plt.show()


import matplotlib.pyplot as plt
import numpy as np
# Select the data about Austria from the table
date_UK = covid_data.loc[covid_data["location"]== 'United Kingdom',"date"]
UK1 = covid_data.loc[covid_data["location"]== 'United Kingdom',"new_cases"]
UK2 = covid_data.loc[covid_data["location"]== 'United Kingdom',"total_cases"]

# Drawing plot
plt.plot(date_UK, UK1, label='new_cases', c='b')
plt.plot(date_UK, UK2, label='total_cases', c='r')
plt.xticks(world_date.iloc[0:len(date_UK):4],rotation=-90)

# Add som elements to the plot
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('New and total cases in UK')
plt.legend()

# Display plot
plt.show()





























