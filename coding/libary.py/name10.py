import pandas as pd 
import numpy as np 

#Create Data 
stuff ={
    'Corporation' : ['Apple', 'Google', 'Meta', 'Apple', 'Google', 'Meta'],
    'Employees': ['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'Salary':[200, 220, 190, 130, 120, 150],
}


#Create DataFrame
my_df = pd.DataFrame(stuff)
print(my_df) 




#Sort Salaries from lowest to highest 
print(f"{my_df.sort_values("Salary")}")

#Sort Salaries Highest to Lowest 
print(f"{my_df.sort_values("Salary", ascending=False)}")

#Not Permanent without inplace=True 
print(my_df) 


#Inplace
#y_df.sort_values("Salary", ascending=False, inplace=True)
my_df.sort_values("Salary", ascending=False, inplace=True)
print(my_df)

#Sort Strings Alphabetically 
print(f'{my_df.sort_values("Corporation")}')


#Sort Strings Alphabetically Descending 
print(f'{my_df.sort_values("Corporation", ascending=False)}')