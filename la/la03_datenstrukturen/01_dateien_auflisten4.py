"""
Entwickeln Sie eine Funktion, die alle Dateien in einem angegebenen 
Ordner auflistet. Nutzen Sie dafür das Modul os. Die Namen der Dateien aus dem Ordner sollen hierbei in 
einer Liste gespeichert werden.
"""
import os

# Listing files and directories
dir_list = os.listdir('./la/la03_datenstrukturen')

# Listing files without directories
file_list = []
for f in dir_list:
    if os.path.isfile(os.path.join('./la/la03_datenstrukturen', f)):
        file_list.append(f)
print(file_list)