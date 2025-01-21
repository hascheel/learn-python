"""
Listen sortieren - Sortieren Sie die Datei-Liste nach der Länge des Dateinamens
und geben Sie das Ergebnis aus. 
"""

import os, os.path

#ordner = "C:\\Users\\scheelh\\OneDrive - Berufsförderungswerk Köln gGmbH\\IT2406-2\\Systementwicklung\\Python_Programme"
ordner = os.getcwd() # aktueller Ordner
#ordner = "./"

dateien = []

# Prüfen: Ist Ordner vorhanden?
if not os.path.isdir(ordner):
	print("Ordner ist nicht vorhanden!")
	exit(0)     # EXIT CODES 0=ok, -1=Fehler

# Dateien in Liste speichern
for i in os.listdir(ordner):
    if os.path.isfile(i):
        dateien.append(i)

for i in dateien:
    print(i)

# Dateien nach Dateillänge sortieren
dateien.sort(key=len)

# Dateien untereinander gelistet ausgeben
for i in dateien:
    print(i)