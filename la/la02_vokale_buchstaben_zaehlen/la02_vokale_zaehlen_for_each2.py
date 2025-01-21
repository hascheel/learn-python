'''
Vokalzähler - Entwickeln Sie ein Programm, das einen Text vom Benutzer abfragt und die Anzahl der 
Vokale zählt. Nutzen Sie entsprechende Programmkonstrukte wie Schleifen und Bedingungen.

Groß- und Kleinschreibung berücksichtigen - Erweitern Sie das Programm so, dass es Groß- und 
Kleinschreibung berücksichtigt.

Sonderzeichen berücksichtigen - Ergänzen Sie die Funktionalität, sodass das Programm zusätzlich 
Sonderzeichen wie !, ?, und . zählt und separat ausgibt.
'''

txt = input('Gib deinen Text ein: ')

vowels = "aAeEiIoOuU"
special_characters = '°!"§$%&/()=?`^²³{[]}\|@€+*~#\'_:;,.>< '

vowel_counter = 0
special_character_counter = 0

for i in txt:
    if i in vowels:
        vowel_counter += 1
    if i in special_characters:
        special_character_counter += 1

print(f'Der Text "{txt}" enthält {vowel_counter} Vokale und {special_character_counter} Sonderzeichen.')