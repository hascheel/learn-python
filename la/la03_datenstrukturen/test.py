import os

def dateien_auflisten(ordner_pfad):
    """Listet alle Dateien in einem angegebenen Ordner auf."""
    try:
        return [datei for datei in os.listdir(ordner_pfad) if os.path.isfile(os.path.join(ordner_pfad, datei))]
    except FileNotFoundError:
        print(f"Der Ordner '{ordner_pfad}' wurde nicht gefunden.")
        return []

def liste_sortieren(datei_liste):
    """Sortiert die Liste nach der Länge der Dateinamen."""
    return sorted(datei_liste, key=len)

def dateien_und_groessen(ordner_pfad):
    """Speichert Dateien und ihre Größen in einem Dictionary."""
    dateien_dict = {}
    for datei in dateien_auflisten(ordner_pfad):
        pfad = os.path.join(ordner_pfad, datei)
        dateien_dict[datei] = os.path.getsize(pfad)
    return dateien_dict

ordner_pfad = "C:\\Users\\scheelh\\OneDrive - Berufsförderungswerk Köln gGmbH\\IT2406-2\\Systementwicklung\\Python_Programme"  # Pfad zu deinem Ordner

# Aufgabe 1: Dateien auflisten
datei_liste = dateien_auflisten(ordner_pfad)
print("Dateien im Ordner:", datei_liste)

# Aufgabe 2: Liste sortieren
sortierte_liste = liste_sortieren(datei_liste)
print("Sortierte Datei-Liste:", sortierte_liste)

# Aufgabe 3: Dateien und Größen speichern
dateien_dict = dateien_und_groessen(ordner_pfad)
print("Dateien mit Größen:", dateien_dict)
