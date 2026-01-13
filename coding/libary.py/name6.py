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




# Group by corporation - To get object Location in memeory 

company = my_df.groupby('Corporation')
print(company)


#sum 

print(company.sum())


# Mean 
#print(company.mean()) mistake

#max min 
print(company.max())
print(company.min())

#Standard deviation 

#print(company.std()) mistake


# variance 
#print(company.var())  mistake


#Count 
print(company.count())


#describe 

print(company.describe())

