'''
Aufgabe 2: Vokalezählen - Schreiben Sie eine Funktion, welche die Anzahl der Vokale in einem gegebenen Wort 
ermittelt und zurückgibt. Hinweis: Vokale sind die Buchstaben A, I, 0, U (sowohl groß als auch klein).
'''
def zaehle_vokale(wort):
    vokal_zaehler = 0
    for buchstabe in wort:
        if buchstabe in "AaEeIiOoUu":
            vokal_zaehler += 1
    return vokal_zaehler

# Test
print(zaehle_vokale("Hallo")) # 2
print(zaehle_vokale("HAllo")) # 2