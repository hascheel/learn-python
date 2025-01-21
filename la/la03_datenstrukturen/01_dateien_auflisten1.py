"""
Entwickeln Sie eine Funktion, die alle Dateien in einem angegebenen 
Ordner auflistet. Nutzen Sie dafür das Modul os. Die Namen der Dateien aus dem Ordner sollen hierbei in 
einer Liste gespeichert werden.
"""

import os

files = []

# Dateien und Ordner als Liste speichern
# files = os.listdir("la\la03_datenstrukturen")
files = os.listdir("./la/la03_datenstrukturen")

print(files)