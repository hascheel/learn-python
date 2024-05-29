#////////////////////
#// If-else statement
# The if statement alone tells us that if a condition is true it will execute a block of statements
# and if the condition is false it won’t. But if we want to do something else if the condition
# is false, we can use the else statement with the if statement to execute a block of code when
# the if condition is false.

x = 12
if x > 11:
    print("greater than 11")
else:
    print("less than or equal to 11")

# if-elif-else ladder
i = 20
if (i == 10):  
    print("i is 10")  
elif (i == 15):  
    print("i is 15")  
elif (i == 20):  
    print("i is 20")  
else:  
    print("i is not present") 

#///////////////
#// For Loops
# Python For loop is used for sequential traversal i.e. it is used for iterating over an iterable
# like String, Tuple, List, Set, or Dictionary.
iterable = 1,3,5,7
for var in iterable:    # statement
    print("For:", var)

# Here we will see a “for” loop in conjunction with the range() function to generate a sequence of numbers starting from 0, up to (but not including) 10, and with a step size of 2. For each number in the sequence, the loop prints its value using the print() function.
for i in range(0, 10, 2):
	print(i)


#/////////////////
#// While Loop
count = 0
while count < 3:   # expression
    count += 1   # statement(s)
    print("Loop:", count)     

countdown = 5
while countdown > 0:
    print("countdown:", countdown)
    countdown -= 1
print("Blast off!")