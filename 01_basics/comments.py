#///////////////////
#// Types of Comments in Python
# There are three types of comments in Python:

# Single line Comments
# Multiline Comments
# String Literals
# Docstring Comments

#////////////////////
#// Single Line Comment
# Comments are ignored by the interpreter during the execution of the program.

#///////////////////////
#// Multi-line Comment
# Python does not provide the option for multiline comments.

#//////////////////////
#// String Literals

'''
Multi-line Comment using string literals
Python doesn’t have a specific syntax for multi-line comments.
However, programmers often use multiple single-line comments, one after the other,
or sometimes triple quotes (either ”’ or “””), even though they’re technically string literals. 
'''

""" Multi-line comment using 
string literals """

' Single-line comments using string literals '
" Python ignores the string literals that are not assigned to avariable so we can use these string literals as Python Comments. "

#/////////////////////
#// Docstring
'''
- Python docstring is the string literals with triple quotes that are appeared right after the function.
- It is used to associate documentation that has been written with Python modules, functions, classes, and methods.
- It is added right below the functions, modules, or classes to describe what they do. In Python, the docstring is then made available via the __doc__ attribute.
'''

def multiply(a, b): 
	"""Multiplies the value of a and b"""
	return a*b

# Print the docstring of multiply function 
print(multiply.__doc__) 
