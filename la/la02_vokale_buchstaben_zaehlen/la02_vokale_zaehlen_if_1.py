txt = input('Gib deinen Text ein: ')
#txt = "aeeiiioooouuuuu"
#txt = "hallo"
vowel_counter = 0

if txt.count("a") > 0:
    print("a =", txt.count("a"))
    vowel_counter = txt.count("a")
if txt.count("e") > 0:
    print("e =", txt.count("e"))
    vowel_counter = vowel_counter + txt.count("a")
if txt.count("i") > 0:
    print("i =", txt.count("i"))
    vowel_counter = vowel_counter + txt.count("i")
if txt.count("o") > 0:
    print("o =", txt.count("o"))
    vowel_counter = vowel_counter + txt.count("o")
if txt.count("u") > 0:
    print("u =", txt.count("u"))
    vowel_counter = vowel_counter + txt.count("u")

print("Anzahl Vokale: ", vowel_counter)

""" Vorlage
print("a =", txt.count("a"))
print("e =", txt.count("e"))
print("i =", txt.count("i"))
print("o =", txt.count("o"))
print("u =", txt.count("u"))
"""