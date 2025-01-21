"""
Entwickeln Sie eine Funktion, die alle Dateien in einem angegebenen 
Ordner auflistet. Nutzen Sie dafür das Modul os. Die Namen der Dateien aus dem Ordner sollen hierbei in 
einer Liste gespeichert werden.
"""
import os

def generate_file_list(directory):
    # Listing files and directories
    dir_list = os.listdir(directory)
    
    # Listing files without directories
    file_list = []
    for f in dir_list:
        if os.path.isfile(os.path.join(directory, f)):
            file_list.append(f)
    return file_list

directory = './la/la03_datenstrukturen'

print(generate_file_list(directory))