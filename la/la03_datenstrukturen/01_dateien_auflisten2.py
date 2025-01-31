"""
Entwickeln Sie eine Funktion, die alle Dateien in einem angegebenen 
Ordner auflistet. Nutzen Sie dafür das Modul os.
Die Namen der Dateien aus dem Ordner sollen hierbei in 
einer Liste gespeichert werden.
"""

import os, os.path

files = []

# Dateien und Ordner in Liste speichern
files = os.listdir("./la/la03_datenstrukturen")

# Dateinamen untereinander aufgelistet ausgeben
for i in files:
    print(i)