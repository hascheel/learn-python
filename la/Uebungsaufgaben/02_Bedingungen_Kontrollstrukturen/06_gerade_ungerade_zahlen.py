'''
Even or odd: Check whether a number entered is even or odd. 
Gerade oder ungerade: Prüfe, ob eine eingegebene Zahl gerade oder ungerade ist. 
'''

def user_input():
    try:
        number = input("Your number: ")
        return int(number)
    except ValueError:
        print(f"Enter integers only!")
        user_input()

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(user_input()))