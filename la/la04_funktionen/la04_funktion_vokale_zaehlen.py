def count_vowels(text):
    vowels = "aAeEiIoOuU"
    vowel_counter = 0
    
    for letter in text: # Nimm jeden einzelnen Buchstaben aus dem Text
        if letter in vowels:
            vowel_counter += 1
    
    return vowel_counter

user_text = input('Type in your text here: ')
print(f"Your text has {count_vowels(user_text)} vowels.")