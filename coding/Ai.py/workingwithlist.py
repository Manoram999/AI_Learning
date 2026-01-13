#looping though an entire list 
magicians = [ 'alice','david','carolina']
for magician in magicians: 
    print(magician)

#Doing more work within a for loop 
magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")

magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")


magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
print("Thank you,everyone.That was a great magic show!")


#Forgetting to indent 
'''magicians = ['alice','david','carolina']
for magician in magicians:
print(magician) forgeting to take space '''

# Making Numerical List 
#Using the range() Function

for value in range(1,5):
    print(value)

#using range() to make a list of Number 

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
'''In this example, the range() function starts with the value 2 and then
adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
value, 11, and produces this result'''


#Simple Statistic with a list of Numbers

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


squares = []
for value in range(1,11):
    square = value ** 2 
    squares.append(square)
print(squares)

#List Comprehensions

squares = [value **2 for value in range(1,11)]
print(squares)

#Working with part of a list 
# Slicing a list 

players = ['charles','martina','michael','florence','eli'] 
print(players[0:3])



players = ['charles','martina','michael','florence','eli'] 
print(players[:4])


players = ['charles','martina','michael','florence','eli'] 
print(players[-3:])

#Looping though a slice 
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a list 

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite food are:")
print(friend_foods)

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite food are:")
print(friend_foods)

#Tuples 
'''A tuple look just like a list except you ise parentheses instead of square brackets'''
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])


#looping thought All Values in a tuple 
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dimensions = (200,50)
print('original dimension:')
for dimension in dimensions:
    print(dimension)

dimensions =( 400,100)
print('\nModified dimension:')
for dimension in dimensions:
    print(dimension)
    