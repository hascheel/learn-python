###########
# Variables
''' Variables in Python are essentially named references pointing to objects in memory.
Unlike some other languages, in Python, you don’t need to declare a variable’s type explicitly.
Based on the value assigned, Python will dynamically determine the type.
We do not need to declare variables before using them or declare their type. A variable is
created the moment we first assign a value to it. A Python variable is a name given to a memory location. '''

# dynamic typing
''' which means variable’s data type can change during runtime. Python is not “statically typed”. '''
a=9
print(type(a))  # <class 'int'> 
a="Hello"
print(type(a))  # <class 'str'>


# Local variables
''' Local variables in Python are the ones that are defined and declared inside a function.
We can not call this variable outside the function. '''
# This function uses local variable s.
def f(): 
	s = "Welcome geeks"
	print(s) 

f() # output: Welcome geeks


# Global variables
''' in Python are the ones that are defined and declared outside a function, 
and we need to use them inside a function. '''
# This function has a variable with 
# name same as s 
def f(): 
	print(s) 

# Global scope 
s = "I love Geeksforgeeks"
f() # output: I love Geeksforgeeks
