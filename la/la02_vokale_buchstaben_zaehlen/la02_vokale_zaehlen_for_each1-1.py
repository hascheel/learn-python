txt = input('Gib deinen Text ein: ')

vowels = "aAeEiIoOuU"

vowel_counter = 0

for buchstabe in txt: # Nimm jeden einzelnen Buchstaben aus dem Text
    if buchstabe in vowels:
        #vowel_counter += 1
        vowel_counter = vowel_counter + 1

"""
    for i in txt:
    if i in vowels:
        vowel_counter += 1
"""

print(vowel_counter)
print("Anzahl Vokale ", vowel_counter, "im Text.")
print(f"Der Text hat {vowel_counter} Vokale.")

# Benutzereingabe
# Überprüfen auf Vokale
# Vokale zählen
# Textausgabe