'''
Funktion Passwort-Generator - Entwickeln Sie eine Funktion für einen Passwort-Generator, der ein 
zufälliges Passwort erstellt. Das Passwort soll Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen 
enthalten. Die Länge soll als Parameter festgelegt werden können. Machen Sie sich diesbezüglich mit dem 
Modul random vertraut.

- Kleinbuchstaben
- Großbuchstaben
- Zahlen
- Sonderzeichen

Programmablauf:
generate_password() -> ask_for_password_details() -> build_password() -> shuffle_password()
'''

import random
import string

def build_password(password_length=12, number_of_lower_case=1, number_of_upper_case=1, number_of_digits=1, number_of_special_characters=1):
    lower_case_chars = string.ascii_letters.lower()
    upper_case_chars = string.ascii_letters.upper()
    digits = string.digits
    special_chars = string.punctuation
    password = ""

    # use the specified number of each character type
    for i in range(number_of_lower_case):
        password += random.choice(lower_case_chars)
    for i in range(number_of_upper_case):
        password += random.choice(upper_case_chars)
    for i in range(number_of_digits):
        password += random.choice(digits)
    for i in range(number_of_special_characters):
        password += random.choice(special_chars)
    
    # fill up the rest of the password with random characters
    for i in range(password_length - len(password)):
        password += random.choice(lower_case_chars + upper_case_chars + digits + special_chars)

    return password

def shuffle_password(password):
    password = list(password)   # convert string to list
    random.shuffle(password)
    password = ''.join(password)   # convert list to string
    return password

def ask_for_password_details():
    try:
        password_length = int(input("Enter the length of the password: "))
    except ValueError:
        password_length = 4
    if password_length < 4:
        print("The password length must be greater than or equal to 4.")
        return ask_for_password_details()
    
    try:
        number_of_lower_case = int(input("Enter the number of lower case characters: "))
    except ValueError:
        number_of_lower_case = 1
    if number_of_lower_case > password_length:
        print("The number of lower case characters must be less than or equal to the password length.")
        return ask_for_password_details()
    
    try:
        number_of_upper_case = int(input("Enter the number of upper case characters: "))
    except ValueError:
        number_of_upper_case = 1
    if number_of_upper_case > password_length:
        print("The number of upper case characters must be less than or equal to the password length.")
        return ask_for_password_details()
    if number_of_upper_case + number_of_lower_case > password_length:
        print("The sum of the number of upper and lower case characters must be less than or equal to the password length.")
        return ask_for_password_details()
    
    try:
        number_of_digits = int(input("Enter the number of digits: "))
    except ValueError:
        number_of_digits = 1
    if number_of_digits > password_length:
        print("The number of digits must be less than or equal to the password length.")
        return ask_for_password_details()
    if number_of_digits + number_of_upper_case + number_of_lower_case > password_length:
        print("The sum of the number of digits, upper and lower case characters must be less than or equal to the password length.")
        return ask_for_password_details()
    
    try:
        number_of_special_characters = int(input("Enter the number of special characters: "))
    except ValueError:
        number_of_special_characters = 1
    if number_of_special_characters > password_length:
        print("The number of special characters must be less than or equal to the password length.")
        return ask_for_password_details()   
    if number_of_special_characters + number_of_digits + number_of_upper_case + number_of_lower_case > password_length:
        print("The sum of the number of special characters, digits, upper and lower case characters must be less than or equal to the password length.")
        return ask_for_password_details()
    
    # check if the password length is greater than or equal to the sum of the number of characters of each type
    if password_length < number_of_lower_case + number_of_upper_case + number_of_digits + number_of_special_characters:
        print("The password length must be greater than or equal to the sum of the number of characters of each type.")
        return ask_for_password_details()
    
    # returns a tuple containing the password details
    return password_length, number_of_lower_case, number_of_upper_case, number_of_digits, number_of_special_characters

def generate_password():
    password_details = ask_for_password_details()
    
    # unpack the tuple and pass the values as arguments to the build_password function
    return shuffle_password(build_password(*password_details))

print(generate_password())
