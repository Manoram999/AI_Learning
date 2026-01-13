bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)


bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])
'''Python has a special syntax for accessing the last element in a list. By ask-
ing for the item at index -1,'''

bicycles = ['trek','cannondale','redline','specialized']
message = f'\nMy first bicycle was a {bicycles[0].title()}' 
print(message)


 #Modifying Element in List

motorcycles =['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'#this remove honda and add ducati
print(motorcycles)

#Adding Elements to list 

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)


#Inserting Element into a list

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)


#Removing Elements from a list using del

motorcycles =[ 'honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Removing an item using pop() method

motorcycles = ['honda','yamaha','suzuki']#1 Note; If nothing inside of pop then it will remove last one
print(motorcycles)
popped_motorcycle = motorcycles.pop()#2
print(motorcycles)#3
print(popped_motorcycle)#4

'''We start by defining and printing the list motorcycles at first. At second we pop
a value from the list and store that value in the variable popped_motorcycle.
We print the list at 3rd to show that a value has been removed from the list.
Then we print the popped value at 4rdto prove that we still have access to
the value that was removed'''

motorcycles = ['honda','yamaha','suzuki']
motorcycles.pop()
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycles I owned was a {last_owned.title()}")



motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(1)
print(f"The last motorcycles I owned was a {last_owned.title()}")

#Removing an item by Value 


motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)



motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive= 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#Organizing a list 

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)


cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)


#sorting a list Temporarily with the sorted()Function

cars=['bmw','audi','tyota','subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list')
print(sorted(cars))
print('\nHere is the original list again')
print(cars)


#printing a list in reverse order 
cars =['bmw','audi','toyota','subaru'] 
print(cars)
cars.reverse()
print(cars)

#Finding the length of a list 
cars = ['bmw','audi','toyota','subaru']
print(len(cars))




