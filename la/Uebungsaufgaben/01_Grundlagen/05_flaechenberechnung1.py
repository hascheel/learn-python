'''
Flächenberechnung: Berechne die Fläche eines Rechtecks aus eingegebenen Werten.
Area calculation: Calculate the area of a rectangle from entered values.
'''

length = int(input("Length of rectangle: "))
height = int(input("Height of rectangle: "))
  
def calculate_rectangle_area(a,b):
    return a * b

print(f'Area of a rectangle of height {height} * length {length} = {calculate_rectangle_area(length,height)}')