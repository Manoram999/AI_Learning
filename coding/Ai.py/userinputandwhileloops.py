#How the Input() Function Work

'''''''''message = input("Tell me something, and I will repeat it back to you:")
print(message) 


#Writing Clear Prompts

Each time you use the input() function, you should include a clear, easy-to-
follow prompt that tells the user exactly what kind of information you’re
looking for. 


name = input("Please enter your name: ")
print(f"\nHello, {name}!")



prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")  '''''''''


#Using itn() to Accept Numerical Input 
'''When you use the input() function, Python interprets everything the user
enters as a string.
The user enters the number 21, but when we ask Python for the value of
age, it returns '21', the string representation of the numerical value entered.
We know Python interpreted the input as a string because the number is now
enclosed in quotes. If all you want to do is print the input, this works well. But
if you try to use the input as a number, you’ll get an error

When you try to use the input to do a numerical comparison u, Python
produces an error because it can’t compare a string to an integer: the string
'21' that’s assigned to age can’t be compared to the numerical value 18 v.
We can resolve this issue by using the int() function, which tells
Python to treat the input as a numerical value. The int() function con-
verts a string representation of a number to a numerical representation,
as shown here:
'''
age = input("\nHow old are you? ")
age = int(age) 
age >= 18 #here this no use
print(age)


height = input("How tall are you,in inches? ")
height = int(height)

if height >= 48 : 
    print("\n You're tall enough to ride!")

else: 
    print(f"\nYou'll be able to ride when you're a little older ")


# The Modulo Operator
#4%3 =1
#5%3 =2
#6%3 =0
#7%3 =1
'''The modulo operator doesn’t tell you how many times one number fits
into another; it just tells you what the remainder is

When one number is divisible by another number, the remainder is 0,
so the modulo operator always returns 0. You can use this fact to determine
if a number is even or odd:'''



number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0 :
    print(f"\nThe number {number} is even.")

else:
    print(f"The number {number} is odd.")


    
# Introducting while loop

'''The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true.'''


# The while loop in Action

current_number = 1 
while current_number <= 5: 
    print(current_number)
    current_number += 1 


# Letting the user choose when to Quit 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program"

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)



prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program"

message = ""
while message != 'quit':
    message = input(prompt)
   

    if message != 'quit':
     print(message)




#Using a Flag

'''In the previous example, we had the program perform certain tasks while
a given condition was true. But what about more complicated programs in
which many different events could cause the program to stop running?
For example, in a game, several different events can end the game.
When the player runs out of ships, their time runs out, or the cities they
were supposed to protect are all destroyed, the game should end. It needs
to end if any one of these events happens. If many possible events might
occur to stop the program, trying to test all these conditions in one while
statement becomes complicated and difficult.
For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire pro-
gram is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop run-
ning when any of several events sets the value of the flag to False. As a result,
our overall while statement needs to check only one condition: whether or
not the flag is currently True. Then, all our other tests (to see if an event has
occurred that should set the flag to False) can be neatly organized in the rest
of the program.
Let’s add a flag to parrot.py from the previous section. This flag, which
we’ll call active (though you can call it anything), will monitor whether or
not the program should continue running:'''


prompt = "\nTell me something, and I will repeat it bak to you:"
prompt += "\nEnter 'quit' to end the program"

active = True 
while active:
    message = input(prompt)

    if message == 'quit': 
        active = False 
    else: 
        print(message)




#Using break to Exit loop 

prompt ="\n Please enter the name of a city you have visited:"
prompt +=" \n (Enter 'quit' when you are finished.)"

while True: 
    city = input (prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd Love to go {city.title()}!")

#Using a continue in a loop

'''Rather than breaking out of a loop entirely without executing the rest of its
code, you can use the continue statement to return to the beginning of the
loop based on the result of a conditional test. For example, consider a loop
that counts from 1 to 10 but prints only the odd numbers in that range'''


current_number = 0 
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:#divisible by 2
        continue 
    print(current_number)
'''First we set current_number to 0. Because it’s less than 10, Python
enters the while loop. Once inside the loop, we increment the count by 1
at u, so current_number is 1. The if statement then checks the modulo of
current_number and 2. If the modulo is 0 (which means current_number is
divisible by 2), the continue statement tells Python to ignore the rest of
the loop and return to the beginning. If the current number is not divis-
ible by 2, the rest of the loop is executed and Python prints the current
number:'''


#Avoiding infinite loop
x = 1 
while x <= 5:
    print(x)
    x += 1

#but if u accidentally omit the line x += 1

#This loop runs forever!
x = 1
while x <=5:
    print(x)

#Using a while loop with list and Dictionaries
#Moving items from one list to another 

#Start with users that need to be verified,
#and an empty list to hold confirmed users.

unconfirmed_users = ['alice','brain','candace']
confirmed_users = []

#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

#Display all confirmed users.

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())



#Removing All Instance of Specific Value from a list
pets = ['dog', 'cat','dog','goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets: 
    pets.remove('cat')
print(pets)



#Filling a Dictionary with User Input 

responses = {}

#Set a flag to indicate that polling is active 
polling_active = True

while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday")

#Store the response in the dictionary
responses[name] = response 

#Find out if anyone else is going to take the poll.
repeat = input("Would you like to let another person respond")
if repeat == 'no':
    polling_active = False 

#Polling is complete.Show the result 
print("\n---Poll Result---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
