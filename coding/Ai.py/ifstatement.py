cars = ['audi','bwm','subaru','tyota']

for car in cars:
    if car == 'bmw': 
        print(car.upper())
    else:
        print(car.title())
    
#Conditional Test
'''At the heart of every if statement is an expression that can be evaluated as
True or False and is called a conditional test. Python uses the values True and
False to decide whether the code in an if statement should be executed. If a
conditional test evaluates to True, Python executes the code following the if
statement. If the test evaluates to False, Python ignores the code following
the if statement'''

car = 'bmw'
car == 'bmw' # True

car = 'Audi'
car == 'audi'


car = 'Audi'
car.lower() == 'audi' #True

car = 'Audi'
car.lower() =='audi'#True 
car 
'Audi' 


#Checking for inequality
requested_topping ='mushrooms'

if requested_topping != 'anchovies':
    print("\nHold the anchovies")


#Numerical Comparisons
age = 18
age == 18 #True



answer = 17 
if answer !=42:
    print("\nThat is not the correct answer.Please try again!")


age = 19 
age < 21 #True
age <= 21 # True
age > 21 # False
age >= 21 # False 



# Checking Multiple Conditions 
#Using to check Multiple Conditation

age_0 = 22
age_1 = 18 
age_0 >= 21 and age_1 >= 21 #false if there is and then is one also false then false

age_1 = 22 
age_0 >= 21 and age_1 >= 21 #True 

'''To improve readability, you can use parentheses around the individual
tests, but they are not required. If you use parentheses, your test would look
like this:'''

(age_0 >= 21 ) and (age_1 >= 21) 


#using or to check multiple condition


age_0 = 22
age_1 = 18 
age_0 >= 21 or age_1 >= 21 #True if there is or then if one also true then true

age_0 = 18
age_0 >= 21 or age_1 >= 21#False bec both is false

'''The keyword or allows you to check multiple conditions as well, but it
passes when either or both of the individual tests pass. An or expression
fails only when both individual tests fail.'''

# checking whether a value is in a list 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
True
'pepperoni' in requested_toppings
False

#Checking Whether a Value is not a list
banned_users = ['andrew','carolina','david']
user ='marie'
if user not in banned_users:
    print(f"\n{user.title()},you can post a response if you wish")

#Boolean Expressions 
'''A Boolean value is either True or False, just like the value
of a conditional expression after it has been evaluated.Boolean values are often used to keep track of certain conditions, such
as whether a game is running or whether a user can edit certain content on
a website:'''


game_active = True 
can_edit = False 


#if Statement

#Simple if Statements
'''if conditional_test: 
    do something '''

age = 19
if age >= 18:
    print("\nYou are enough to vote!")


age = 19
if age >= 18:
    print("\nYou are enough to vote!")
print("Have you registered to vote yet?")

#if-else Statements 
age = 17 
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")



#if-elif_else chain 
'''Often, you’ll need to test more than two possible situations, and to evaluate
these you can use Python’s if-elif-else syntax. Python executes only one
block in an if-elif-else chain. It runs each conditional test in order until
one passes. When a test passes, the code following that test is executed and
Python skips the rest of the tests.
Many real-world situations involve more than two possible conditions.
For example, consider an amusement park that charges different rates for
different age groups:
• Admission for anyone under age 4 is free.
• Admission for anyone between the ages of 4 and 18 is $25.
• Admission for anyone age 18 or older is $40.'''


age = 12 

if age < 4: 
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else: 
    print("Your admissin cost is $40.")


age = 12 
if age < 4:
    price=0 
elif age < 18:
    price = 25 
else:
    price = 40 

print(f"\nYour admission cost is ${price}.")


#using Multiple elif Blocks

age = 12 

if age < 4: 
    price = 0 
elif age < 18: 
    price =25 
elif age < 65:
    price = 40 
else:
    price = 20 

print(f"\nYour admission cost is ${price}.")

#Omitting the else block 
'''Python does not require an else block at the end of an if-elif chain. Sometimes
an else block is useful; sometimes it is clearer to use an additional
elif statement that catches the specific condition of interest'''

age = 12 

if age < 4:
    price = 0 
elif age < 18:
    price = 25 
elif age < 65: 
    price = 40 
elif age >= 65: 
    price = 20 

print(f" Your admission cost is ${price}.")



#Testing Multiple Conditions 

'''The if-elif-else chain is powerful, but it’s only appropriate to use when you
just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient
and allows you to test for one specific condition.
However, sometimes it’s important to check all of the conditions of
interest. In this case, you should use a series of simple if statements with no
elif or else blocks. This technique makes sense when more than one condi-
tion could be True, and you want to act on every condition that is True.'''


requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding muchrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza")


#Checking for special Items 
requested_toppings = ['mushrooms','green peppers','extra cheese']
 
for requested_topping in requested_toppings:
    print(f'Adding {requested_topping}.')
print("\nFinished making your pizza")



requested_toopings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toopings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else: 
        print(f"Adding {requested_toopings}.")
print("\nFinished making your pizza!")

#Checking that a list is not empty 

'''This time we start out with an empty list of requested toppings at 1.
Instead of jumping right into a for loop, we do a quick check at2 . When the
name of a list is used in an if statement, Python returns True if the list con-
tains at least one item; an empty list evaluates to False. If requested_toppings
passes the conditional test, we run the same for loop we used in the previous
example. If the conditional test fails, we print a message asking the customer
if they really want a plain pizza with no toppings 3'''


requested_toppings = []#1

if requested_toppings:#2
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:#3
    print("Are you sure you want a plain pizza?")


#Using Multiple List 

available_toppings = ['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Addings {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
        
print("\nFinished making your pizza!")


#Styling your if Statements 

'''if age < 4:

is better than:

if age<4: '''


