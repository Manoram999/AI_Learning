

'''Object-oriented programming is one of the most effective approaches to writing soft-
ware. In object-oriented programming you write classes that represent real-world things
and situations, and you create objects based on these classes.
Understanding object-oriented programming will help you see the
world as a programmer does. It’ll help you really know your code, not
just what’s happening line by line, but also the bigger concepts behind it.
Knowing the logic behind classes will train you to think logically so you can
write programs that effectively address almost any problem you encounter.
Classes also make life easier for you and the other programmers you’ll
work with as you take on increasingly complex challenges. When you and
other programmers write code based on the same kind of logic, you’ll be
able to understand each other’s work. Your programs will make sense to
many collaborators, allowing everyone to accomplish more. '''


#Creating and Using a Class

class Dog:#1 #This create a class name Dog
    """A simple attempt to model a dog."""#2 #This is a docstring, explaining what the class represents

    def __init__(self, name, age):#3 #This is the constructor method.It runs automatically  whenever you create a Dog object.Self refer to the object itelf and name and age are inputs when creating the dog
      """Initialize name and age attributes."""
      self.name = name #4 This store the value inside the object ""
      self.age = age   

    def sit(self):#5
      """Simulate a dog sitting in response to a command."""
      print(f"{self.name} is now sitting.") #This prints a message using the dog name

    def roll_over(self):
      """Simulate rolling over in response to a command."""
      print(f"{self.name} rolled over!") #This print another message 




'''Inside the object:

my_dog.name becomes "Buddy"

my_dog.age becomes 5 '''

'''At 1 we
define a class called Dog. By convention, capitalized names refer to classes
in Python. There are no parentheses in the class definition because we’re
creating this class from scratch. At 2 we write a docstring describing what
this class does.'''


#The _int_() Method
'''A function that’s part of a class is a method.The __init__() method at 3is a special method
that Python runs automatically whenever we create a new instance based
on the Dog class.
We define the __init__() method to have three parameters: self, name,
and age. The self parameter is required in the method definition, and it
must come first before the other parameters.

The two variables defined at 4 each have the prefix self. Any variable
prefixed with self is available to every method in the class, and we’ll also be
able to access these variables through any instance created from the class.

The Dog class has two other methods defined: sit() and roll_over() 5.
Because these methods don’t need additional information to run, we just
define them to have one parameter, self.'''  


#Making an instance from a Class


class Dog: #A class is a blueprint to create object 
   def __init__(self,name,age):#__init__ tells python when a new dog is created,give it a name and age
      self.name = name #Self represent the object itself.Means store the name inside this object 
      self.age = age
    
my_dog = Dog('Willie', 6) #1 #An object is something you create using a class.Here my_dog is object

print(f"My dog name is {my_dog.name}.")#2
print(f"My dog is {my_dog.age} years old.")#3



# Accessing Attributes 
'''To access the attributes of an instance, you use dot notation. At 2 we access
the value of my_dog’s attribute name by writing:my_dog.name
Dot notation is used often in Python. This syntax demonstrates how
Python finds an attribute’s value. Here Python looks at the instance my_dog
and then finds the attribute name associated with my_dog. This is the same attri-
bute referred to as self.name in the class Dog. At w we use the same approach
to work with the attribute age.'''

# Calling Methods



class Dog:  
   def __init__(self,name,age):
      self.name = name  
      self.age = age
    

   def sit(self):#5
      """Simulate a dog sitting in response to a command."""
      print(f"{self.name} is now sitting.") #This prints a message using the dog name

   def roll_over(self):
      """Simulate rolling over in response to a command."""
      print(f"{self.name} rolled over!")



my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over() 


#Creating Multiple Instances 
'''You can create as many instances from a class as you need. Let’s create a
second dog called your_dog:'''


class Dog: 
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def sit(self):
      print(f"{self.name} is now sitting.")


my_dog = Dog('Willie', 6)
your_dog =Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()


print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


      
#Working with classes and instances 
 
# The car class 
'''Let’s write a new class representing a car. Our class will store information
about the kind of car we’re working with, and it will have a method that
summarizes this information''' 



class Car:
   """A simple attempt to represent a car."""

   # CORRECTED LINE BELOW:
   def __init__(self, make, model, year):
      """ Initialize attributes to describe a car."""
      self.make = make 
      self.model = model 
      self.year = year 
      
   def get_descriptive_name(self):
      """Return a neatly formatted descriptive name.""" 
      long_name = f"{self.year} {self.make} {self.model}"
      return long_name.title()
   
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())


#Setting a Default Value For an Attribute. 


"""When an instance is created, attributes can be defined without being
passed in as parameters. These attributes can be defined in the __init__()
method, where they are assigned a default value.
Let’s add an attribute called odometer_reading that always starts with a
value of 0. We’ll also add a method read_odometer() that helps us read each
car’s odometer:"""



class Car:
   
   def __init__(self,make,model,year):
      """Initaialize attributes to describe a car"""
      self.make = make 
      self.model = model 
      self.year = year
      self.odometer_reading = 0 #1

   def get_descriptive_name(self):
      """Return a neatly formatted descriptive name.""" 
      long_name = f"{self.year} {self.make} {self.model} "
      return long_name.title()
   
   def read_odometer(self): #2
      """Print a statement showing the car's mileage."""
      print(f"This car has {self.odometer_reading} miles on it")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()   

'''This time when Python calls the __init__() method to create a new
instance, it stores the make, model, and year values as attributes like
it did in the previous example. Then Python creates a new attribute
called odometer_reading and sets its initial value to 0 1. We also have a
new method called read_odometer() at 2 that makes it easy to read a car’s
mileage'''

   
'''Modifying Attribute Values
You can change an attribute’s value in three ways: you can change the value
directly through an instance, set the value through a method, or increment
the value (add a certain amount to it) through a method. Let’s look at each
of these approaches.'''


#Modifying an Attribute's Value Directly 

class Car:
   def __init__(self, make, model, year):

      self.make = make 
      self.model = model
      self.year = year 
      self.odometer_reading = 0 

   def get_descriptive_name(self):
      long_name = f"{self.make} {self.model} {self.year}"
      return long_name.title()

   def read_odometer(self):
      print(f"This car has {self.odometer_reading} miles on it ")


my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading = 23 
my_new_car.read_odometer()  

#Modifying an Attributes's Value Through a Method 

class Car:
   def __init__(self, make, model, year):

      self.make = make 
      self.model = model
      self.year = year 
      self.odometer_reading = 0 

   def get_descriptive_name(self):
      long_name = f"{self.make} {self.model} {self.year}"
      return long_name.title()

   def read_odometer(self):
      print(f"This car has {self.odometer_reading} miles on it ")

   def update_odometer(self,mileage):
      """Set the odometer reading to the given value."""
      self.odometer_reading = mileage 

my_new_car = Car('audi','a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


'''We can extend the method update_odometer() to do additional work
every time the odometer reading is modified. Let’s add a little logic to
make sure no one tries to roll back the odometer reading:'''


class Car: 
   def __init__(self, make, model, year):

      self.make = make 
      self.model = model
      self.year = year 
      self.odometer_reading = 5

   
   def get_descriptive_name(self):
      long_name = f"{self.make} {self.model} {self.year}"
      return long_name.title()

   def read_odometer(self):
      print(f"This car has {self.odometer_reading} miles on it ")

   def update_odometer(self,mileage):
      """
      Set the odometer reding to the given value.
      Reject the change if it attempts to roll the odometer back.
      """
      self.mileage = 23
      
      if mileage >= self.odometer_reading:#1
         self.odometer_reading = mileage  
      else:
         print("You can't roll back an odometer!")#2 

'''Now update_odometer() checks that the new reading makes sense before
modifying the attribute. If the new mileage, mileage, is greater than or equal
to the existing mileage, self.odometer_reading, you can update the odometer
reading to the new mileage 1. If the new mileage is less than the existing
mileage, you’ll get a warning that you can’t roll back an odometer 2.'''


#Incrementing an Attribute's Value through a Method 
'''Sometimes you’ll want to increment an attribute’s value by a certain
amount rather than set an entirely new value. Say we buy a used car and
put 100 miles on it between the time we buy it and the time we register it.
Here’s a method that allows us to pass this incremental amount and add
that value to the odometer reading:'''

class Car:
   def __init__(self, make, model, year):

      self.make = make 
      self.model = model
      self.year = year 
      self.odometer_reading = 0 

   def get_descriptive_name(self):
      long_name = f"{self.make} {self.model} {self.year}"
      return long_name.title()

   def read_odometer(self):
      print(f"This car has {self.odometer_reading} miles on it ")

   def update_odometer(self,mileage):
      """Set the odometer reading to the given value."""
      self.odometer_reading = mileage 

   def increment_odometer(self, miles):#1
      '''Add the given amount to the odometer reading.'''
      self.odometer_reading += miles 


my_used_car = Car('subaru', 'outback', 2015)#2
print(my_used_car.get_descriptive_name())


my_used_car.update_odometer(23_500)#3
my_used_car.read_odometer()

my_used_car.increment_odometer(100)#4
my_used_car.read_odometer()

'''The new method increment_odometer() at u takes in a number of miles,
and adds this value to self.odometer_reading. At v we create a used car,
my_used_car. We set its odometer to 23,500 by calling update_odometer() and
passing it 23_500 at w. At x we call increment_odometer() and pass it 100 to add
the 100 miles that we drove between buying the car and registering it:'''


#Inheritance

'''You don’t always have to start from scratch when writing a class. If the class
you’re writing is a specialized version of another class you wrote, you can
use inheritance. When one class inherits from another, it takes on the attri-
butes and methods of the first class. The original class is called the parent
class, and the new class is the child class. The child class can inherit any
or all of the attributes and methods of its parent class, but it’s also free to
define new attributes and methods of its own.'''

#The__init__() Method for a Child Class

'''When you’re writing a new class based on an existing class, you’ll often
want to call the __init__() method from the parent class. This will initialize
any attributes that were defined in the parent __init__() method and make
them available in the child class.'''



class Car:
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
   def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
       else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       self.odometer_reading += miles
 
class ElectricCar(Car):#2
   """Represent aspects of a car, specific to electric vehicles."""
   def __init__(self, make, model, year):#3
     """Initialize attributes of the parent class."""
     super().__init__(make, model, year)#4


my_tesla = ElectricCar('tesla', 'model s', 2019)#5
print(my_tesla.get_descriptive_name())

 
'''At 1 we start with Car. When you create a child class, the parent class
must be part of the current file and must appear before the child class in
the file. At 2 we define the child class, ElectricCar. The name of the par-
ent class must be included in parentheses in the definition of a child class.
The __init__() method at 3 takes in the information required to make a Car
instance.
The super() function at 4 is a special function that allows you to call
a method from the parent class. This line tells Python to call the __init__()
method from Car, which gives an ElectricCar instance all the attributes
defined in that method. The name super comes from a convention of call-
ing the parent class a superclass and the child class a subclass.

We test whether inheritance is working properly by trying to create an
electric car with the same kind of information we’d provide when making
a regular car. At y we make an instance of the ElectricCar class and assign
it to my_tesla. This line calls the __init__() method defined in ElectricCar,
which in turn tells Python to call the __init__() method defined in the par-
ent class Car. We provide the arguments 'tesla', 'model s', and 2019.
Aside from __init__(), there are no attributes or methods yet that are
particular to an electric car. At this point we’re just making sure the electric
car has the appropriate Car behaviors:'''



#Defining Attributes and Methods for the Child Class 



class Car:
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
   def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
       else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       self.odometer_reading += miles


class ElectricCar(Car):
   """Represent aspects of a car,specififc to electric to electric vehicles"""

   def __init__(self,make,model,year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """

       super().__init__(make, model, year)
       self.battery_size = 75 #1

   def describe_battery(self):#2
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery() 

'''At u we add a new attribute self.battery_size and set its initial value to,
say, 75. This attribute will be associated with all instances created from the
ElectricCar class but won’t be associated with any instances of Car. We also
add a method called describe_battery() that prints information about the
battery at v. When we call this method, we get a description that is clearly
specific to an electric car:'''


#Overriding Methods from the parent Class 

class ElectricCar(Car):



   def __init__(self,make,model,year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """

       super().__init__(make, model, year)
       self.battery_size = 75 #1

   def describe_battery(self):#2
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")



my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery() 


def fill_gas_talk(self):
   """Electric cars don't have gas tanks."""
   print("This car doesn't need a gas tank!")


#Instances as Attributes 

class Car:
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
   def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
       else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       self.odometer_reading += miles


class Battery:
   """A simple attempt to model a battery for an electric car."""

   def __init__(self, battery_size=75):
      """Initialize the battery's attributes."""
      self.battery_size = battery_size 

   def describe_battery(self):
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")

class ElectricCar(Car):
   """Represent aspect of a car, specific to electric vehicles."""
   def __init__(self,make,model,year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """

       super().__init__(make, model, year)
       self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


'''Lets add another method to battery that report 
the range pf the car based on the battery size'''


class Car:
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
   def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
       else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       self.odometer_reading += miles


class Battery:
   """A simple attempt to model a battery for an electric car."""

   def __init__(self, battery_size=75):
      """Initialize the battery's attributes."""
      self.battery_size = battery_size 

   def describe_battery(self):
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")

   def get_range(self):
      """Print a statement about the range this battery provides. """
      if self.battery_size == 75:
         range = 260
      elif self.battery_size == 100:
         range = 315

      print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
   """Represent aspect of a car, specific to electric vehicles."""
   def __init__(self,make,model,year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """

       super().__init__(make, model, year)
       self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#Importing Classes 

"""A class that cna be used to represent a car."""


class Car:
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
   def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
       else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       self.odometer_reading += miles 
       
       
#from car import Car

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()




#Storing Multiple Classes in Module

"""A set of classes used to represent gas and electric car"""



class Car:
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
       self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
   def read_odometer(self):
       print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
       else:
         print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
       self.odometer_reading += miles


class Battery:
   """A simple attempt to model a battery for an electric car."""

   def __init__(self, battery_size=75):
      """Initialize the battery's attributes."""
      self.battery_size = battery_size 

   def describe_battery(self):
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")

class ElectricCar(Car):
   """Represent aspect of a car, specific to electric vehicles."""
   def __init__(self,make,model,year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """

       super().__init__(make, model, year)
       self.battery = Battery()

















