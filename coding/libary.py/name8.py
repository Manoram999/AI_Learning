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
def times1000(x):
    return format(x * 1000,"d") 


#Use Apply Function 
print(f'{my_df["Salary"].apply(times1000)}')


#Make it Into a DataFrame
print(f"{pd.DataFrame(my_df["Salary"].apply(times1000))}")


#Add Elder last Name 
def namer(x):
    if x == "John":
        return "John Elder"
    else:
        return "Not Important"            #return x 
    
#Show Elder Last Name 
print(f"{my_df["Employees"].apply(namer)}") 


#Use Lambda 
print(f"{pd.DataFrame(my_df["Salary"].apply(lambda x: format(x * 1000, ",d")))}")



