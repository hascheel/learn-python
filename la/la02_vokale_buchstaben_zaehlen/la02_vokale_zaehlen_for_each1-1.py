text = input('Gib deinen Text ein: ')
vowels = "aAeEiIoOuU"
vowel_counter = 0

for letter in text: # Nimm jeden einzelnen lettern aus dem Text
    if letter in vowels:
        #vowel_counter += 1
        vowel_counter = vowel_counter + 1
       
#print(vowel_counter)
#print("Anzahl Vokale ", vowel_counter, "im Text.")
print(f"Der Text hat {vowel_counter} Vokale.")

# Benutzereingabe
# Überprüfen auf Vokale
# Vokale zählen
# Textausgabe