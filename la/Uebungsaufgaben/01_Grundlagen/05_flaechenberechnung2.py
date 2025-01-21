'''
Flächenberechnung: Berechne die Fläche eines Rechtecks aus eingegebenen Werten.
Area calculation: Calculate the area of a rectangle from entered values.
'''
length = 0
height = 0

def user_input():
    try:
        length = int(input("Length of rectangle: "))
        height = int(input("Height of rectangle: "))
    except TypeError:
        print(f"Bitte nur Ganzzahlen eingeben!")
        user_input()
    except ValueError:
        print(f"Nur Ganzzahlen eingeben!")
        user_input()

def calculate_rectangle_area(a,b):
    return a * b

user_input()
print(f'Area of a rectangle of height {height} * length {length} = {calculate_rectangle_area(length,height)}')