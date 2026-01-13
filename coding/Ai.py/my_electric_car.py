from car import ElectricCar 

my_tesla = ElectricCar('tesla', 'model s', 2019)


print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() 

#Importing Multiple Classes from a Moduel 

from car import Car, ElectricCar 

my_beetle = Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster', 2019)
print(my_tesla.get_descriptive_name())


#import an Entire module 

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster', 2019)
print(my_tesla.get_descriptive_name())


#Importing All Classes from a Module

#from module_name import 


#Importing a Module into a Module 

""" A set of classes that can be used to represent electric cars."""

from car import Car 

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
      print(f"This car can go about the range this battery provides.")

class ElectricCar(Car):
   """Represent aspect of a car, specific to electric vehicles."""
   def __init__(self,make,model,year):
       """
       Initialize attributes of the parent class.
       Then initialize attributes specific to an electric car.
       """

       super().__init__(make, model, year)
       self.battery = Battery()


       