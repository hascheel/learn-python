zahlen = [5,3,1,100,2]

def sortieren(zahlen):
    laenge = len(zahlen)
    for i in range(laenge -1):
        for j in range(laenge -1):
            if zahlen[j] > zahlen[j+1]:
                zahlen[j], zahlen[j+1] = zahlen[j+1], zahlen[j]

    return zahlen

print(sortieren(zahlen))