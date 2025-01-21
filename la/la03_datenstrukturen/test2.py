import os

ordnerPfad = "C:\\Users\\scheelh\\OneDrive - Berufsförderungswerk Köln gGmbH\\IT2406-2\\Systementwicklung\\Python_Programme"
dateiListe = []

def dateienAuflisten(ordnerPfad):
    for datei in os.listdir(ordnerPfad):
        if os.path.isfile(os.path.join(ordnerPfad, datei)):
            print(os.path.join(ordnerPfad, datei))
            #dateiListe.append(datei)
        
            
#def dateienSortieren(dateiListe):

dateiListe = dateienAuflisten(ordnerPfad)
print(dateiListe)

#print(sorted(dateiListe, key=len))
