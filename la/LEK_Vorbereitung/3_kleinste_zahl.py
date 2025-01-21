'''
Aufgabe 3: Kleinste Zahl - Entwickeln Sie eine Funktion, die das kleinste Element in einer gegebenen Liste
von ganzen Zahlen findet und zurückgibt. Hinweis: Hinter zahlen verbirgt sich eine Liste mit mehreren Werten,
z.B. [3, 5, 2, 9]
'''

def finde_minimum(zahlen):
    if not zahlen:          # Wenn die Liste leer ist, gebe None zurück
        return None
    minimum = zahlen[0]     # Setze das erste Element der Liste als Minimum / Nimm erste Zahl
    for zahl in zahlen:     
        if zahl < minimum:  # Wenn die aktuelle Zahl kleiner als das bisherige Minimum ist, setze die aktuelle Zahl als neues Minimum
            minimum = zahl
    return minimum

# Test
print(finde_minimum([3, 5, 2, 9])) # 2
print(finde_minimum([15, 0, -10, 1])) # -10
print(finde_minimum([])) # None