'''
Flächenberechnung: Berechne die Fläche eines Rechtecks aus eingegebenen Werten.
Area calculation: Calculate the area of a rectangle from entered values.
'''

def user_input():
    try:
        length = int(input("Length of rectangle: "))
        height = int(input("Height of rectangle: "))
        return length,height
    except ValueError:
        print(f"Enter integers only!")
        user_input()

def calculate_rectangle_area(a,b):
    return a,b, a * b

user_input = user_input()
result = calculate_rectangle_area(user_input[0],user_input[1])
print(result)
print(f'Area of a rectangle of height {result[0]} * length {result[1]} = {result[2]}')