#Grab Rows, Points, and subsets from dataframe

import pandas as pd 
import numpy as np 
#import csv file

'''my_df = pd.read_csv('dog_data_short.csv') 
print(my_df)


#Grab Row Method 1 Location 
print(my_df.loc[2])


#Grab row Method 2 Index Location   
print(my_df.iloc[3])

#Specific points. (row and column)
#my_df.loc['Row','Column']
print(my_df.loc[1, "DogName"])


#Subsets
#my_df.loc[['row','row'],['column','column']]
print(my_df.loc[[1,3],["DogName", "Breed"]])'''



#How To Make Conditional Selections 
'''my_df3 = pd.read_csv('dog_data.csv') 
print(my_df3) 


#Conditional Selection 
# > < = >= <= etc
#Return Booleans
print( my_df3 == "BROWN" ) 


#Returns Dataframe with data 
print(f"{my_df3[my_df3 == "BROWN"]}") #NaN Not a Number


# Run them on a Column 
print(f"{my_df3[my_df3 == "BROWN"]["Color"]}") 

#Return Multiple Columns 

print(f"{my_df3[my_df3 == "BROWN"][["Color","Breed"]]}")

#If we had data 
#print(f"{my_df3[my_df3 > 159][["Color","Breed"]]}")'''


#Multiple Conditional Selection

'''my_df = pd.read_csv('dog_data.csv')
print(my_df)


#Multiple Conditional AND
print(f"{my_df[(my_df["Color"] == "BROWN") & (my_df["Breed"]== "MIXED")]}")

#Get Length
print(f"{len(my_df[(my_df["Color"] == "BROWN") & (my_df["Breed"] == "MIXED")])}")


# Multiple Conditional OR 
print(f"{my_df[(my_df["Color"] == "BROWN") | (my_df["Breed"]== "MIXED")]}")

#length

print(f"{len(my_df[(my_df["Color"] == "BROWN") | (my_df["Breed"]== "MIXED")])}")


#Return Specific Coloumn 
print(f"{my_df[(my_df["Color"] == "BROWN") & (my_df["Breed"]== "MIXED")]["DogName"]}")'''




#How to change and reset index 

#Create New Column 
'''my_df = pd.read_csv('dog_data_short.csv') 
print(my_df)


my_df["Frame Header"] = ["Dog 1", "Dog 2", "Dog 3", "Dog 4", "Dog 5" ]
print(my_df)

#Set Index 
print(f"{my_df.set_index("Frame Header", inplace=True)}")


#Show DataFrame 
print(my_df)

# Reset Index 
my_df.reset_index(inplace=True)
print(my_df)

#Drop Column 
my_df.drop("Frame Header", axis = 1, inplace = True)
print(my_df)'''



# How To Fix Incomplete Data 

'''stuff = {'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9], 'D':[10,11,12]}
my_df = pd.DataFrame(stuff)
print(my_df)'''
stuff = {'A':[1,2,3], 'B':[4,np.nan,6], 'C':[7,8,9], 'D':[10,11,12]}
my_df = pd.DataFrame(stuff)
print(my_df)

#Drop Rows with null data
print(my_df.dropna())


#Drop Columns with null data inplace= True for permamemt
print(my_df.dropna(axis=1))


#Not Permanent, inplace= False if to make permanent then inplace True
print(my_df)


#More than one? Set Threshold 

'print(my_df.dropna(thresh=2#the number of nan it has , axis=1))'

#Replace thins with fillna()
print(my_df.fillna(value="BOB"))

#Use Math. Functions 
print(f'{my_df.fillna(value=my_df['B'].mean())}')


#Use min/max
print(f'{my_df.fillna(value=my_df['B'].min())}')

print(f'{my_df.fillna(value=my_df['B'].max())}')