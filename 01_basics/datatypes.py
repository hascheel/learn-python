''' Data types are the classification or categorization of data items.
It represents the kind of value that tells what operations can be performed 
on a particular data. Since everything is an object in Python programming, data 
types are classes and variables are instances (objects) of these classes.

Integers: Whole numbers without decimals.
Floats: Numbers with decimals.
Strings: Text enclosed in single or double quotes.
Lists: Ordered collections of items.
Tuples: Immutable collections of items.
Dictionaries: Key-value pairs.'''

x = "Hello World" # string 
x = 50 # integer 
x = 60.5 # float 
x = 3j # complex 
x = ["geeks", "for", "geeks"] # list 
x = ("geeks", "for", "geeks") # tuple 
x = {"name": "Suraj", "age": 24} # dict 
x = {"geeks", "for", "geeks"} # set 
x = True # bool 
x = b"Geeks" # binary 

# Check their data types with type() function:
a=9
print(type(a))  # <class 'int'>