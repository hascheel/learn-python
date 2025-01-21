import os, os.path

def list_files(file_path):
    file_list = []
    # Dateien & Ordner in Liste speichern
    for i in os.listdir(file_path):
        file_list.append(i)
    return file_list

def print_files(file_list):
    # Dateinamen untereinander aufgelistet ausgeben
    for i in file_list:
        # if os.path.isfile(i):
            print(i)

file_path = "la\la03_datenstrukturen"
print_files(list_files(file_path))