'''
https://www.w3schools.com/python/ref_func_input.asp
'''

# Funktion input() - Eingabe vom Benutzer entgegennehmen
name = input("How is your name? ")
print("Hello, " + name + "!")


txt = input('Gib deinen Text ein: ')
if txt == '':
    print('Sie haben keinen Text eingegeben! ')
    exit(0)