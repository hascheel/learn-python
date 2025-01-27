'''
Age check: Check the age and decide whether someone is of legal age.
Altersprüfung: Frage das Alter ab und entscheide, ob jemand volljährig ist.
'''
def legal_age(age):
    if age >= 18:
        print(f'You are {age} and of legal age.')
    else:
        print(f'Your are not of legal age!')

try:
    age = int(input("Your age: "))
    legal_age(age)
except ValueError:
    print("Use only integers!")