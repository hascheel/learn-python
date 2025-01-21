'''
Begrüßungsprogramm - Schreiben Sie ein Begrüßungsprogramm, das den Benutzer willkommen heißt und 
nach seinem Namen fragt. Nutzen Sie hierbei die Funktionen print() und input() zur Umsetzung. 
'''

def print_username(username):
    print('Hallo', username)

username = input('Hallo lieber Nutzer. Wie ist dein Name: ')

print_username(username)

# username = input('Hallo lieber Nutzer. Wie ist dein Name:')
# print('Hallo', username)