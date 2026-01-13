import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from numpy.random import randn 

#Create a quick dataframe 
my_df = pd.DataFrame(randn(100,4),columns=["Mon", "Tues", "Wed", "Thur"])
print(my_df)


#Histogram 
my_df["Wed"].hist()
plt.show()

#Histogram with smaller bins, 50,20 
my_df["Wed"].hist(bins=50)
plt.show()

#another way without grids bars
my_df["Wed"].plot(kind="hist")
plt.show()


my_df["Wed"].hist(bins=20, grid =False)
plt.show()