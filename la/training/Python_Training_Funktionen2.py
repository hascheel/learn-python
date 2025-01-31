# Diese Funktion begrüßt den Nutzer, basierend auf dem übergebenen Namen.
def begruessung_nutzer(name):
    print(f'hello {name}')

# Diese Funktion addiert zwei Zahlen und gibt das Ergebnis zurück.
def zwei_zahlen_addieren(a, b):
    return a + b

# Diese Funktion kehrt die Reihenfolge der Elemente in einer Liste um und gibt sie zurück.
def liste_umkehren(liste):
    length = len(liste)
    reversed_liste = []
    print(liste)
    for x in liste:
        length -= 1
        # print(liste[length])
        reversed_liste.append(liste[length])
    print(reversed_liste)

liste = [1,2]
liste_umkehren(liste)

# Diese Funktion findet das längste Wort in einer Liste von Wörtern.
def laengstes_wort_finden(wörter):
    # TODO
    return None

# Diese Funktion generiert eine zufällige Zahl im angegebenen Bereich.
def zufaellige_zahl_generieren(min, max):
    # TODO
    return None

# Diese Funktion gibt die aktuelle Uhrzeit im Format "HH:MM:SS" aus.
def aktuelle_uhrzeit_ausgeben():
    # TODO
    return None

# Diese Funktion generiert ein zufälliges Passwort mit der angegebenen Länge.
def passwort_generieren(länge):
    # TODO
    return None

# Diese Funktion berechnet die Anzahl der Tage bis zu einem bestimmten zukünftigen Datum.
def tage_bis_zukuenftiges_datum(datum):
    # TODO
    return None

# Diese Funktion findet die gemeinsamen Elemente zwischen zwei Listen und gibt diese zurück.
def gemeinsame_elemente_finden(liste1, liste2):
    # TODO
    return None

# Diese Funktion prüft, ob ein Wort ein Palindrom ist (d.h., vorwärts und rückwärts gleich).
def palindrom_pruefen(wort):
    # TODO
    return None