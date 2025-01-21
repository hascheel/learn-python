import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(password_length))

'''
Dieser Code definiert ein Python-Programm, das ein zufälliges Passwort generiert. Dabei kommen die Konstrukte __name__ und __main__ zum Einsatz, um den Code gezielt auszuführen, wenn das Skript direkt gestartet wird.

Codeanalyse
1. Importe
	• random: Wird verwendet, um zufällige Elemente auszuwählen.
	• string: Bietet Zugriff auf vordefinierte Zeichen wie Buchstaben, Ziffern und Sonderzeichen.

2. generate_password-Funktion
Die Funktion generate_password generiert ein zufälliges Passwort mit einer bestimmten Länge:
	• Parameter: length=12 – Die Standardlänge des Passworts ist 12 Zeichen.
	• Zeichenpool: Enthält Buchstaben (ascii_letters), Ziffern (digits) und Sonderzeichen (punctuation).
	• Passwortgenerierung: 
		○ Die Funktion wählt length zufällige Zeichen aus dem Zeichenpool mit random.choice(characters).
		○ Die Methode ''.join(...) verbindet diese Zeichen zu einem String.

3. Der if __name__ == "__main__"-Block
Dieser Block sorgt dafür, dass der Code nur dann ausgeführt wird, wenn das Skript direkt gestartet wird (nicht, wenn es als Modul importiert wird).
	• __name__:
		○ Ist eine spezielle Variable, die den Namen des aktuellen Moduls enthält.
		○ Wenn das Skript direkt ausgeführt wird, hat __name__ den Wert "__main__".
		○ Wird das Skript jedoch als Modul importiert, enthält __name__ den Modulnamen.
	• if __name__ == "__main__"::
		○ Dieser Block wird nur ausgeführt, wenn das Skript direkt ausgeführt wird.
		○ Dadurch kann der Programmablauf von Funktionen oder Modulen getrennt werden.

4. Interaktiver Teil
Wenn das Skript direkt ausgeführt wird:
	1. Fragt es den Benutzer nach der gewünschten Passwortlänge (input()).
	2. Wandelt die Eingabe in eine Ganzzahl (int()) um.
	3. Ruft die Funktion generate_password() auf und gibt das generierte Passwort aus.

Zusammengefasst
	• __name__: Gibt den Namen des Moduls an. 
		○ "__main__" bedeutet, dass das Skript direkt ausgeführt wird.
	• if __name__ == "__main__":: Trennt ausführbaren Code von importierbaren Funktionen/Definitionen.

Beispielausführung
    
    Wenn das Skript gestartet wird:
        Enter the desired password length: 16
        Generated password: k&7Fj#s!D3mPl9Q@
    
    Falls das Skript importiert wird:
        import my_password_generator  # Name des Skripts
        
        # Hier passiert nichts, weil der "__main__"-Block nicht ausgeführt wird.

Dies ermöglicht es, das Modul für wiederverwendbare Funktionen (generate_password) zu nutzen, ohne dass der interaktive Teil stört.

'''