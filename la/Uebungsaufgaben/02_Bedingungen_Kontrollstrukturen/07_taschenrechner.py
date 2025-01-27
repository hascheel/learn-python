'''
Simple calculator: Implement a simple if-elif-else structure for basic arithmetic operations. 
Einfacher Taschenrechner: Implementiere eine einfache if-elif-else Struktur für Grundrechenarten. 
'''

try:
    num_a = int(input("First number: "))
    calc_type = input("Which calculation type? (e.g.: + - * /): ")
    num_b = int(input("Second number: "))
except ValueError:
    print("Wrong type! Enter integers only!")

try:
    if calc_type == "+":
        print(f'Sum of {num_a} + {num_b} is {num_a + num_b}')
    elif calc_type == "-":
        print(f'Difference of {num_a} - {num_b} is {num_a - num_b}')
    elif calc_type == "*":
        print(f'Product of {num_a} * {num_b} is {num_a * num_b}')
    elif calc_type == "/":
        try:
            print(f'Quotient of {num_a} / {num_b} is {num_a / num_b}')
        except ZeroDivisionError:
            print("Division by zero not possible!")
    else:
        print("Incorrect calculation operator! Only use: + - * /")
except NameError:
    print("Wrong type! Enter integers only!")