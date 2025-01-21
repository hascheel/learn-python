'''
Write a program that reads two numbers from the user,
converts them to an integer, and adds them.
'''

value1 = input("Your first number: ")
value2 = input("Your second number: ")

print(value1 + value2)  # Problem: Concatenation of strings

# Determine the type of the value
type_of_value = type(value1)
print(type_of_value) # <class 'str'>

# Solution: Type Casting
value1 = int(value1)
value2 = int(value2)
print(type(value1)) # <class 'int'>
print(value1 + value2)

value3 = int(input("Your third number: "))
value4 = float(input("Your fourth number: "))
value5 = str(input("Your fifth number: "))