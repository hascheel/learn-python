'''
FUNKTION finde_duplikate(ordner_pfad):
    WENN ordner_pfad nicht existiert ODER kein Verzeichnis ist:
        GIB ein leeres Wörterbuch zurück

    INITIALISIERE hash_verzeichnis als leeres Wörterbuch

    FÜR jede Datei im ordner_pfad:
        BERECHNE datei_pfad als vollständigen Pfad der Datei
        BERECHNE datei_hash mit berechne_datei_hash(datei_pfad)

        WENN datei_hash bereits in hash_verzeichnis existiert: 
            FÜGE datei_pfad zu hash_verzeichnis[datei_hash] hinzu
        SONST:
            SETZE hash_verzeichnis[datei_hash] auf eine neue Liste wit datei_pfad

    FILTERE hash_verzeichnis, um nur Einträge mit mehr als einem Pfad zu behalten 
    GIB das gefilterte hash_verzeichnis zurück

FUNKTION berechne_datei_hash(datei_pfad, blockgröße=4096):
    INITIALISIERE hash_objekt mit SHA255

    ÖFFNE datei_pfad im binären Lese-Modus:
        SOLANGE ein block = Lese blockgröße Bytes aus der Datei:
            AKTUALISIERE hash_objekt mit block-Daten

    GIB den Hexadezimalwert von hash_objekt zurück
'''