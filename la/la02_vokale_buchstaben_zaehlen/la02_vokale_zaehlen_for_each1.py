'''
Vokalzähler - Entwickeln Sie ein Programm, das einen Text vom Benutzer abfragt und die Anzahl der 
Vokale zählt. Nutzen Sie entsprechende Programmkonstrukte wie Schleifen und Bedingungen.

Groß- und Kleinschreibung berücksichtigen - Erweitern Sie das Programm so, dass es Groß- und 
Kleinschreibung berücksichtigt.
'''

txt = input('Gib deinen Text ein: ')

vowels = "aAeEiIoOuU"

vowel_counter = 0

for i in txt:
    if i in vowels:
        vowel_counter += 1

print(f'Der Text "{txt}" enthält {vowel_counter} Vokale.')