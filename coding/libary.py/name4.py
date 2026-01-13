import pandas as pd 
import numpy as np 
#import csv file

my_df = pd.read_csv('dog_data_short.csv') 
print(my_df)

#Add Column from List 
gender = ["male", "Female", "Male", "Male", "Female"]
my_df["Gender"] = gender 
print(my_df) 


#Add Default Values  
'''my_df["Alive/Dead"] = [True]*len(my_df)
print(my_df)

#Add Nan Value 
my_df["Show Dog"] = [np.nan]*len(my_df)
print(my_df)

#Add column with.insert()-Allows Position 

my_df.insert(1,"Adopted", [True]*len(my_df), True)
print(my_df)

#Add Column with .assign()-creates new df
my_df2 = my_df.assign(Horse=[False]*len(my_df))
print(my_df2)'''
  
 

#Remove Column 
'''my_df.drop("Gender", axis=1, inplace=True)
print(my_df)


#Remove Row 
print(my_df.drop(3, axis=0))'''













