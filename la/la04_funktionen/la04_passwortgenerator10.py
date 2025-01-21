'''
Funktion Passwort-Generator - Entwickeln Sie eine Funktion für einen Passwort-Generator, der ein 
zufälliges Passwort erstellt. Das Passwort soll Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen 
enthalten. Die Länge soll als Parameter festgelegt werden können. Machen Sie sich diesbezüglich mit dem 
Modul random vertraut.

- Kleinbuchstaben
- Großbuchstaben
- Zahlen
- Sonderzeichen
'''

import random
import string

password_length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(password_length):
    password += random.choice(characters)

print(password)