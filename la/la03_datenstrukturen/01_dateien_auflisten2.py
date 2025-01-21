"""
Entwickeln Sie eine Funktion, die alle Dateien in einem angegebenen 
Ordner auflistet. Nutzen Sie dafür das Modul os. Die Namen der Dateien aus dem Ordner sollen hierbei in 
einer Liste gespeichert werden.
"""

import os, os.path

files = []

# Dateien in Liste speichern
for i in os.listdir("la\la03_datenstrukturen"):
    if os.path.isfile(i):
        files.append(i)

"""
# Dateinamen untereinander aufgelistet ausgeben
for i in files:
    if os.path.isfile(i):
        print(i)

"""

print(files)