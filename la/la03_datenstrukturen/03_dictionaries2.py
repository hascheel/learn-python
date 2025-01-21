"""
Dictionaries - Speichern Sie die Dateien und ihre Größen (in Bytes) in einem „Dictionary“.
Das Format soll dann wie folgt aussehen: {"datei1.txt": 20000, "datei2.doc": 50000}. 
"""

import os, os.path

ordner = os.getcwd() # aktueller Ordner

dateien = {}

for i in os.listdir(ordner):
		print(os.path.join(path, i))

		dateien[i] = os.path.getsize(i)
print(dateien)

"""
# Prüfen: Ist Ordner vorhanden?
if not os.path.isdir(ordner):
	print("Ordner ist nicht vorhanden!")
	exit(0)     # EXIT CODES 0=ok, -1=Fehler

# Dateiennamen mit Dateilänge in Dictionary speichern
for i in os.listdir('.'):
    if os.path.isfile(i):
        dateien[i] = os.path.getsize(i)

print(dateien)
"""