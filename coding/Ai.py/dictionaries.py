alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

'''A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of key-
value pairs inside the braces'''

'''The string 'color' is a key in this dictionary, and its associated
value is 'green'.'''


#Accessing Values in a fictionary 
alien_0 = {'color':'green'}
print(alien_0['color'])


alien_0 = {'color': 'green', 'points':5}
new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")


#Adding New key-value Pairs

alien_0 = {'color': 'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#Starting with an Empty Dictionary 

alien_0 ={}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

'''''For a more interesting example, let’s track the position of an alien that
can move at different speeds. We’ll store a value representing the alien’s
current speed and then use it to determine how far to the right the alien
should move:'''''


alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

#move the alien to right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1 
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
#This must be a fast alien.
    x_increment = 3 
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment 
print(f"New position: {alien_0['x_position']}") 


# Removing Key-Value Pairs

alien_0 = {'color': 'green', 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

'''When you no longer need a piece of information that’s stored in a dictionary,
you can use the del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key that you want to
remove'''

#A dictionary of similar object

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
     }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
favorite_languages['sarah'] 


#Using get() to access values

alien_0 = {'color': 'green','speed' : 'slow '}
point_value = alien_0.get('points','\nNo point value assigned.')
print(point_value)


#Looping through a Dictionary. 

#Loopping through All key-value Paris

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last' : 'fermi',
    }

for key,value in user_0.items(): #for k, v in user_0.items()
    print(f"\nkey: {key}")
    print(f"value: {value}")


favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")


#Looping Through All the Keys in a Dictionary
'''The keys() method is useful when you don’t need to work with all of the
­ values in a dictionary. '''

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }

for name in favorite_languages.keys():
    print(name.title())



favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
  
    if name in friends:
      language = favorite_languages[name].title()
      print(f"\t{name.title()}, I see you love {language}!")




'''You can also use the keys() method to find out if a particular person
was polled. This time, let’s find out if Erin took the poll:'''


favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("\nErin,please take our poll!")

#Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
   print(f"\n{name.title()}, thank you for taking the poll.")

#Looping Through All Values in a Dictionary

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
   print(language.title())


favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

'''A set is a collection in which each item must be unique:
When you wrap set() around a list that contains duplicate items, Python
identifies the unique items in the list and builds a set from those items. At u
we use set() to pull out the unique languages in ­ favorite_­ languages.values().
The result is a nonrepetitive list of languages that have been mentioned
by people taking the poll:'''




#Nesting
'''Sometimes you’ll want to store multiple dictionaries in a list, or a list of
items as a value in a dictionary. This is called nesting. You can nest dictionaries
inside a list, a list of items inside a dictionary, or even a dictionary inside
another dictionary. Nesting is a powerful feature, as the following examples
will demonstrate.'''


alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
   print(alien)



# Make an empty list for storing aliens.
aliens = []
   
    # Make 30 green aliens.
for alien_number in range(30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
   aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
   print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")





# Make an empty list for storing aliens.
aliens = []


# Make 30 green aliens.
for alien_number in range (30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

for alien in aliens[:3]:
  if alien['color'] == 'green':
      alien['color'] = 'yellow'
      alien['speed'] = 'medium'
      alien['points'] = 10


# Show the first 5 aliens.
for alien in aliens[:5]:
  print(alien)
print("...")



'''Because we want to modify the first three aliens, we loop through a
slice that includes only the first three aliens. All of the aliens are green now
but that won’t always be the case, so we write an if statement to make sure
we’re only modifying green aliens. If the alien is green, we change the color
to 'yellow', the speed to 'medium', and the point value to 10, as shown in the
following output:'''



'''You could expand this loop by adding an elif block that turns yellow
aliens into red, fast-moving ones worth 15 points each. Without showing the
entire program again, that loop would look like this:'''

for alien in aliens[0:3]:
  if alien['color'] == 'green':
   alien['color'] = 'yellow'
   alien['speed'] = 'medium'
   alien['points'] = 10
  elif alien['color'] == 'yellow':
   alien['color'] = 'red'
   alien['speed'] = 'fast'
   alien['points'] = 15


'''It’s common to store a number of dictionaries in a list when each dictionary
contains many kinds of information about one object. For example,
you might create a dictionary for each user on a website, as we did in user.py
on page 100, and store the individual dictionaries in a list called users. All
of the dictionaries in the list should have an identical structure so you can
loop through the list and work with each dictionary object in the same way.'''



# A List in Dictionary

#Store information about a pizza being ordered.

pizza = {
   'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    } 

#Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")

for topping in pizza['toppings']:
   print("\t" + topping)
      



favorite_languages = {
   'jen': ['python', 'ruby'],
   'sarah': ['c'],
   'edward': ['ruby', 'go'],
   'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
   print(f"\n{name.title()}'s favorite languages are:")
   for language in languages:
    print(f"\t{language.title()}")


#A dictionary in a Dictionary 

users ={
   'aeinstein': {
      'first' : 'albert',  
      'last': 'einstein',
      'location': 'princeton',
      },

   'mcurie': {
      'first' : 'marie',
      'last' : 'curie',
      'location' : 'paris'
      },
   
}



for username, user_info in users.items():
   print(f"\nUsername: {username}")
   full_name = f"{user_info['first']} {user_info['last']}"
   location = user_info['location']

   print(f"\tFull name: {full_name.title()}")
   print(f"\tlocation: {location.title()}")
