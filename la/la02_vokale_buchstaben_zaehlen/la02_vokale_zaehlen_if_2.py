txt = input('Gib deinen Text ein: ')
#txt = "aeeiiioooouuuuu"
#txt = "hallo"
vowel_counter = 0

if txt.count("a") > 0:
    print("a =", txt.count("a"))
    vowel_counter = vowel_counter + txt.count("a")
elif txt.count("A") > 0:
    print("A =", txt.count("A"))
    vowel_counter = vowel_counter + txt.count("A")
if txt.count("e") > 0:
    print("e =", txt.count("e"))
    vowel_counter = vowel_counter + txt.count("a")
elif txt.count("E") > 0:
    print("E =", txt.count("E"))
    vowel_counter = vowel_counter + txt.count("E")
if txt.count("i") > 0:
    print("i =", txt.count("i"))
    vowel_counter = vowel_counter + txt.count("i")
elif txt.count("I") > 0:
    print("I =", txt.count("I"))
    vowel_counter = vowel_counter + txt.count("I")
if txt.count("o") > 0:
    print("o =", txt.count("o"))
    vowel_counter = vowel_counter + txt.count("o")
elif txt.count("O") > 0:
    print("O =", txt.count("O"))
    vowel_counter = vowel_counter + txt.count("O")
if txt.count("u") > 0:
    print("u =", txt.count("u"))
    vowel_counter = vowel_counter + txt.count("u")
elif txt.count("U") > 0:
    print("U =", txt.count("U"))
    vowel_counter = vowel_counter + txt.count("U")

print("Anzahl Vokale: ", vowel_counter)