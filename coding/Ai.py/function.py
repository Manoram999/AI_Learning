'''In this chapter you’ll learn to write
functions, which are named blocks of code
that are designed to do one specific job'''

def greet_user(): #the def is keyword used to define a function.
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#Passing information to a Function 
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

'''The variable username in the definition of greet_user() is an example of a
parameter, a piece of information the function needs to do its job. The value
'jesse' in greet_user('jesse') is an example of an argument'''



#Positional Argument 
def describe_pet(animal_type, pet_name):
    '''Diplay information about a pet '''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')


#Multiple Function Calls 

def describe_pet(animal_type, pet_name):
    '''Diplay information about a pet '''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


#Order Matters in positional Arguments

'''You can get unexpected results if you mix up the order of the arguments in
a function call when using positional arguments'''

def describe_pet(animal_type, pet_name):
    '''Diplay information about a pet '''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')



#Keyword Arguments


'''A keyword argument is a name-value pair that you pass to a function'''


def describe_pet(animal_type, pet_name): 
   """Display information about a pet."""
   print(f"\nI have a {animal_type}.")
   print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster', pet_name = 'harry')

'''The order of keyword arguments doesn’t matter because Python
knows where each value should go. The following two function calls are
equivalent:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')'''



#default Values 

'''When writing a function, you can define a default value for each parameter.
If an argument for a parameter is provided in the function call, Python uses
the argument value. If not, it uses the parameter’s default value. So when
you define a default value for a parameter, you can exclude the correspond-
ing argument you’d usually write in the function call. Using default values
can simplify your function calls and clarify the ways in which your functions
are typically used.'''


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


#Equivalent Function Call 

""""Because positional arguments, keyword arguments, and default values can
all be used together, often you’ll have several equivalent ways to call a func-
tion.


With this definition, an argument always needs to be provided for
pet_name, and this value can be provided using the positional or keyword
format. If the animal being described is not a dog, an argument for
animal_type must be included in the call, and this argument can also be
specified using the positional or keyword format.
All of the following calls would work for this function:"""




# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


#Avoiding Argument Errors
'''When you start to use functions, don’t be surprised if you encounter errors
about unmatched arguments. Unmatched arguments occur when you
provide fewer or more arguments than a function needs to do its work.
For example, here’s what happens if we try to call describe_pet() with no
arguments:'''

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet()

'''Python recognizes that some information is missing from the function
call, and the traceback tells us that'''


#Return values 

'''A function doesn’t always have to display its output directly. Instead, it can
process some data and then return a value or set of values. The value the
function returns is called a return value.The return statement takes a value
from inside a function and sends it back to the line that called the function '''

#Returning a simple value
def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#Making an Argument optional

def get_formatted_name(first_name, middle_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {middle_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)



def get_formatted_name(first_name, last_name, middle_name=''):
  """Return a full name, neatly formatted."""
  if middle_name:
   full_name = f"{first_name} {middle_name} {last_name}"
  else:
   full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



#Returning a Dictionary 
def build_person(first_name, last_name):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=None):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  if age:
     person['age'] = age
  return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


#Using a Function wtih a while loop
''' def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

# This is an infinite loop!
while True:
  print("\nPlease tell me your name:")
  f_name = input("First name: ")
  l_name = input("Last name: ")
  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\nHello, {formatted_name}!") '''



def get_formatted_name(first_name, last_name):
   """Return a full name, neatly formatted."""
   full_name = f"{first_name} {last_name}"
   return full_name.title()

while True:
  print("\nPlease tell me your name:")
  print("(enter 'q' at any time to quit)")
  
  f_name = input("First name: ")
  if f_name == 'q':
   break
  l_name = input("Last name: ")
  if l_name == 'q':
    break

  formatted_name = get_formatted_name(f_name, l_name)
  print(f"\nHello, {formatted_name}!") 


#Passing a List

def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = f"Hello, {name.title()}!"
    print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



#Modifying a List in a Function

#Start with some designs that need to be printed

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until nono are left.
# Move each design to completed_models after printing.
while unprinted_designs:
   current_design = unprinted_designs.pop()
   print(f"Printing model: {current_design}")
   completed_models.append(current_design)

#Display all completed models.
print("\nThe following models have beeen printed:")
for completed_model in completed_models:
   print(completed_model)

'''We can reorganize this code by writing two functions, each of which
does one specific job. Most of the code won’t change; we’re just making
it more carefully structured. The first function will handle printing the
designs, and the second will summarize the prints that have been made:'''

def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to completed_models after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):

  """Show all the models that were printed."""
  for completed_model in completed_models:
     print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



#Peventing a Function from Modifying a list
#print_models(unprinted_designs[:], completed_models)

'''The function print_models() can do its work because it still receives the
names of all unprinted designs. But this time it uses a copy of the origi-
nal unprinted designs list, not the actual unprinted_designs list. The list
completed_models will fill up with the names of printed models like it did
before, but the original list of unprinted designs will be unaffected by the
function'''


#Passing an Arbbitray Number of Arguments

def make_pizza(toppings):
  """Print the list of toppings that have been requested."""
  print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')




def make_pizza(*toppings):
  """Summarize the pizza we are about to make."""
  print("\nMaking a pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#Mixing Positional and Arbitrary Argument

def make_pizza(size, *toppings):
  """Summarize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
      print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#Using Arbitrary Arguments

def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein',
                              location='princeton',
                              field='physics')

print(user_profile)


#Storing your functions in Modules 
#Importing an entire module


def make_pizza(size, toppings):
  """Summarize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}") 

'''
import pizza 

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms','green peppers', ' extra cheese')'''


#Importing Specific Functions

'''from pizza import make_pizza 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')'''




#Using as to give a function an Alias 

'''from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms','green peppers','extra cheese')'''

#Using As to give a Module an Alias

'''import pizza as p 

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')'''


#Importing All Function in a Module

'''from pizza import 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom','green peppers','extra cheese')'''


#Styling Function 
'''def function_name(parameter_0, parameter_1='default value')

function_name(value_0, parameter_1='value')

def function_name(
parameter_0, parameter_1, parameter_2,
parameter_3, parameter_4, parameter_5):
function body...'''





