#Inheritance 

'''Concept: The ability to define a new class with little or no modification to an existing class.

Basic: Parent and Child
At its simplest, inheritance allows a Child class to acquire the properties and methods of a Parent class.'''

'''class Vehicle:  # Parent Class
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):  # Child Class
    def drive(self):
        print("Driving the car")

my_car = Car()
print(my_car.start_engine())# Inherited method
print(my_car.drive())       # Child's own method'''


'''The super() function
When you want to add functionality to a method that already exists in the parent (like __init__), you use super().'''

'''class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Let the Parent handle the name and salary
        super().__init__(name, salary)
        # The Child handles the new attribute
        self.prog_lang = programming_language '''



'''Multiple Inheritance & MRO
Python allows a class to inherit from multiple parents.
 This introduces complexity: if two parents have the same method, 
 which one gets called? Python uses MRO (Method Resolution Order) to decide.'''

'''class A:
    def process(self): print("A process")

class B(A):
    def process(self): print("B process")

class C(A):
    def process(self): print("C process")

class D(B, C):
    pass

obj = D()
obj.process()'''
# Output: "B process"
# Why? Python looks at D, then the first parent (B). 
# You can view the order via: print(D.mro())




#Iterators and Generators


'''Concept: Efficiently handling streams of data.

Basic: Iterators vs. Iterables
Iterable: Something you can loop over (List, Tuple, String).
Iterator: The internal object that actually does the fetching, one by one.
Intermediate: Custom Iterators
To make your own object loopable, you must implement __iter__ and __next__.'''


'''class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration # Signals the loop to stop
        num = self.current
        self.current -= 1
        return num

for i in CountDown(3):
    print(i)''' # Output: 3, 2, 1 


'''Generators (yield)
Generators are syntactic sugar for Iterators. 
They allow you to write a function that can "pause" execution and resume later, saving massive amounts of memory.
Why is this advanced? It allows for Lazy Evaluation. 
You can generate an infinite sequence of numbers without crashing your RAM because you only generate the number you need right now.'''
# A generator that yields Fibonacci numbers infinitely
def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a # Pauses here, returns a, waits for next call
        a, b = b, a + b

'''gen = infinite_fibonacci()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) '''# 2
# This list is infinite, but we only consumed 4 items.


#List Comprehensions
'''Concept: A concise way to create lists. It is generally faster than a for-loop because the iteration happens at the C-language level inside Python.

Basic: Syntax Replacement
Converting a standard loop into a comprehension.'''
'''# Old way
squares = []
for x in range(5):
    squares.append(x * x)

# Comprehension
squares = [x * x for x in range(5)]'''

#Filtering
#Adding if logic to select specific items
# Get only even numbers
#evens = [x for x in range(10) if x % 2 == 0]

'''Advanced: Nested Comprehensions
You can flatten matrices or run double loops in a single line.
However, be careful—if it gets too complex, it becomes hard to read.'''

'''matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Flatten the matrix into [1, 2, 3, 4, 5, 6...]
# Read: "For every row in matrix, for every num in row, give me num"
flat = [num for row in matrix for num in row]'''




'''Decorators
Concept: Functions that modify other functions.

Basic: Higher-Order Functions
In Python, functions are objects. You can pass a function into another function.

Intermediate: The Wrapper Pattern
A decorator wraps a function, adding code before and after execution.'''


'''def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()'''

'''Advanced: Decorators with Arguments & functools
Real-world decorators (like in Flask or Django) often need arguments. 
This requires a three-layer function structure. 
Also, we use functools.wraps to prevent the decorator from "hiding" the original function's name and documentation.'''
'''import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func) # Preserves metadata of 'func'
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")'''
# Prints "Hello Alice" 3 times






#Multithreading vs. Multiprocessing
'''Concept: Doing multiple things at the same time.

The Critical Constraint: The GIL
To understand this, you must know about the Global Interpreter Lock (GIL).
 Python (CPython) allows only one thread to execute Python bytecode at a time.

This means Multithreading in Python is not "true" parallelism for CPU tasks.
1. Multithreading
Best For: I/O Bound tasks (Waiting for something).

Examples: Downloading files, scraping websites, database queries.
While one thread waits for a download, the CPU switches to another thread.
Advanced: Race Conditions
When threads share memory, they can corrupt data if they access it simultaneously. We use a Lock to prevent this.'''

'''import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock: # Only one thread can enter this block at a time
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()'''


 #Multiprocessing
'''Best For: CPU Bound tasks (Heavy Calculation).

Examples: Image processing, Machine Learning, Video rendering.
It creates separate memory spaces. It bypasses the GIL. Each process runs on a separate CPU core.
Advanced: Process Pools
Managing individual processes is messy. 
Using a Pool allows you to map a function across a list of data using all available CPU cores.'''



'''from multiprocessing import Pool
import time

def slow_square(n):
    time.sleep(1) # Simulate heavy work
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    # Creates a pool of workers equal to your CPU cores
    with Pool() as p:
        # Maps the function to the list and runs in parallel
        result = p.map(slow_square, numbers)
    
    print(result)'''
