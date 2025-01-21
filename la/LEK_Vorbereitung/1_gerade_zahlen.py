'''
Aufgabe 1: Gerade Zahlen - Erstellen Sie eine Funktion, die überprüft,
ob eine Zahl gerade oder ungerade ist und das entsprechende Ergebnis zurückgibt.
'''
def ist_gerade(zahl):
    if zahl % 2 == 0:   # Wenn die Zahl durch 2 teilbar ist, und der Rest 0 ist (Modulo) ist sie gerade
        return True
    else:               # Ansonsten ist sie ungerade
        return False

# Test
print(ist_gerade(4)) # True
print(ist_gerade(5)) # False