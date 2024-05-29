# Operators in general are used to perform operations on values and variables.
# These are standard symbols used for the purpose of logical and arithmetic operations.

# Arithmetic operators: +, -, *, /, %, ** (exponentiation), // (floor division).
# Comparison operators: ==, !=, <, >, <=, >=.
# Logical operators: and, or, not.
# Assignment operators: =, +=, -=, *=, /=, %=, **=, //=.
# Bitwise operators: &, |, ^, ~, <<, >>.
# Strings: Strings can be enclosed in single or double quotes. You can use the + operator to concatenate strings.


#////////////////////////
#// Arithmetic Operators
# Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.

# The precedence of Arithmetic Operators in Python is as follows:
# P – Parentheses
# E – Exponentiation
# M – Multiplication (Multiplication and division have the same precedence)
# D – Division
# A – Addition (Addition and subtraction have the same precedence)
# S – Subtraction

a = 9
b = 4
add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
p = a ** b
print('addition:', add)
print('subtraction:', sub)
print('multiplication:', mul)
print('division:', div)
print('modulo:', mod)
print('exponentiation:', p)


#/////////////////////
#// Logical Operators
# Python Logical operators perform Logical AND, Logical OR, and Logical NOT operations.
# It is used to combine conditional statements.
a = True
b = False
print(a and b)
print(a or b)
print(not a)


#//////////////////////
#// Assignment Operators
# Python Assignment operators are used to assign values to the variables.
a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b) 


#/////////////////////
#// Bitwise Operators
# Python Bitwise operators act on bits and perform bit-by-bit operations.
# These are used to operate on binary numbers.
a = 10
b = 4
print(a & b) 
print(a | b) 
print(~a) 
print(a ^ b) 
print(a >> 2) 
print(a << 2) 


#///////////////////////
#// Strings
greeting = "Hello"
name = "Helena"
message = greeting + ", " + name + "!"  # string concatenation
print(message)  # Output: Hello, Helena!

# f-strings (formatted string literals) - Embed expressions and variables directly into strings. The idea behind f-strings is to make string interpolation simpler.
name = 'Helena'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")