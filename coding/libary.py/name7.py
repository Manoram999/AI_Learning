import pandas as pd 
import numpy as np 

# import cvs file
my_df = pd.read_csv('dog_data.csv')
print(my_df)

# Grab  A Specific Column 

print(my_df["DogName"])


#Count Values 

print(f'{my_df["DogName"].value_counts()}')

#Pass as Dataframe 
print(f'{pd.DataFrame(my_df["DogName"].value_counts()).head(50)}')


#Grab Uniques 
print(f'{my_df["DogName"].unique()}')


#Show as Dataframe

print(pd.DataFrame(my_df["DogName"].unique()).head(50))