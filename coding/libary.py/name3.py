#How to count data in a DataFrame 


import pandas as pd 
import numpy as np 
#import cvs file
#my_df = pd.read_csv('dog_data.csv')
#print(my_df)


#Count Distint Values - Desending 
"""print(my_df['Color'].value_counts())


#Count Distinct Values- Ascending 
print(my_df['Color'].value_counts(ascending=True))


#Dog Names - without NaN
print(my_df['DogName'].value_counts())


#Dog Names - with NaN :where dog name missing and 1 to 20
print(my_df['DogName'].value_counts(dropna=False))


#Get Relative Frequency- Percentage 
print(my_df['Color'].value_counts(normalize=True))


#Get specific Item count
print(my_df['Color'].value_counts()['WHITE'])


#Count Unique Values - Size 
print(my_df.groupby('Color').size())


#Count Unique Values - Count 
print(my_df.groupby('Color').count())  


#get a count of all columns across all columns 
#print(my_df.apply(pd.value_counts))"""

