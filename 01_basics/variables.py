#///////////////
#// Variables
# Variables in Python are essentially named references pointing to objects in memory.
# Unlike some other languages, in Python, you don’t need to declare a variable’s type explicitly.
# Based on the value assigned, Python will dynamically determine the type.

# dynamic typing - which means variable’s data type can change during runtime.
a=9
print(type(a))  # <class 'int'> 
a="Hello"
print(type(a))  # <class 'str'>