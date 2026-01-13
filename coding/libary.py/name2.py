import pandas as pd 
import numpy as np



# Pandas Serises - Like a table Column- 1 Dimensional Array Holding Any Holding any type of data 


""""my_series = [5,9,12,27]
my_var = pd.Series(my_series)
print(my_var)


# Print specific Value 

'''my_var[2]
print(my_var)'''



# Lables using the index argument 
my_index = ["A","B","C","D"]
my_var2 = pd.Series(my_series,my_index)
print(my_var2)


'''print(f"{my_var2[1]}")'''


#Key Value Dictionary

cars= {"Tesla":12, "Mercedes":42, "BMW":3}
my_var3 = pd.Series(cars)
print(my_var3)

print(f"{my_var3["Tesla"]}") """



from numpy.random import randn

'''my_data = randn(4,3)  #Rows, Columns
my_rows = ["A","B","C","D"]
my_cols = ["Monday","Tuesday", "Friday"]


#Create DataFrame

my_df = pd.DataFrame(my_data, my_rows, my_cols)
print(my_df)'''

# import csv file 
my_df2 = pd.read_csv('dog_data.csv')
'''print(my_df2)# This is use to import and if i had the same file in the same  directiory 


#Pull out rows

print(f"{my_df2.loc[1]}")


#Pull out multiple rows


print(f"{my_df2.loc[[0,5,8]]}") '''




#pull data from pandas dataframes
#Grab first 5 rows
print(f"{my_df2.head()}")


#Grab certain number of first rows 
print(f"{my_df2.head(9)}")


#Grab last 5 rows 
print(f"{my_df2.tail()}")

#Grab certain number of last rows 

print(f"{my_df2.tail(8)}")


#Get info about dataframe 
print(f"{my_df2.info()}")

#Get shape of rows and columns 

print(f"{my_df2.shape}")


#Get number of dimensions

print(f"{my_df2.ndim}")

#Get the column datatypes 
print(f"{my_df2.dtypes}")


#Get some statistic about the data
print(f"{my_df2.describe()}")


#Describe a specififc column 
print(f"{my_df2['Breed'].describe()}")

#Select specific column using brackets
print(f"{my_df2['DogName']}")
 



#Select specific column using Location 
print(f"{my_df2.iloc[:, 0]}") 
print(f"{my_df2.iloc[:, 1]}")
