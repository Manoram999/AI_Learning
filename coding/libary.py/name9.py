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

#Create Function 
def times10(x):
    #return x* 100 
    return format (x * 1000, ',d')

#Use Apply Function
print(f'{my_df["Salary"].apply(times10)}')


#Append to current DF 
my_df["Salary"] = my_df["Salary"].apply(times10)
print(my_df)


#Function on multiple columns 
def namer(x):
    return "Codemy: " + x 

#Apply to Two Columns 
print(my_df[["Corporation", "Employees"]].apply(namer))


#Append to current dataframe


my_df[["Corporation", "Employees"]] = my_df[["Corporation", "Employees"]].apply(namer)
print(my_df)