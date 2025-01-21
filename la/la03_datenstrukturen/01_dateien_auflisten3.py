"""
Entwickeln Sie eine Funktion, die alle Dateien in einem angegebenen 
Ordner auflistet. Nutzen Sie dafür das Modul os. Die Namen der Dateien aus dem Ordner sollen hierbei in 
einer Liste gespeichert werden.
"""

import os, os.path

#ordner = "C:\\Users\\scheelh\\OneDrive - Berufsförderungswerk Köln gGmbH\\IT2406-2\\Systementwicklung\\Python_Programme"
# ordner = os.getcwd() # aktueller Ordner
ordner = "./la/la03_datenstrukturen"
#ordner = "./"

dateien = []

# Prüfen: Ist Ordner vorhanden?
if not os.path.isdir(ordner):
	print("Ordner ist nicht vorhanden!")
	exit(0)     # EXIT CODES 0=ok, -1=Fehler

# Dateien und Ordner als Liste speichern
dateien = os.listdir(ordner)

# Dateien untereinander gelistet ausgeben
for i in dateien:
    if os.path.isfile(i):
        print(i)