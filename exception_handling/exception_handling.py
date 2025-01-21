a = 4
b = 0
try:
	k = a//b
	print(k)
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')

print("The value of a / b is : ")
assert b != 0, "Divide by 0 error"
print(a / b)

temp = "geeks for geeks"
if temp != "geeks":
	raise TypeError("Both the strings are different.")
