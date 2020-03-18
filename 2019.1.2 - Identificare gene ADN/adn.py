toTest = input()
toFind = input()
indiceFound = []
toFindReverse = []
for i in range(len(toFind)):
    if toFind[i] == 'A':
        toFindReverse.append('T')
    elif toFind[i] == 'T':
        toFindReverse.append('A')
    elif toFind[i] == 'C':
        toFindReverse.append('G')
    elif toFind[i] == 'G':
        toFindReverse.append('C')
toFindReverse.reverse()
toFindR = ''
for letter in toFindReverse:
    toFindR += letter


i = 0
while True:
    indice = toTest.find(toFind,i)
    if indice == -1:
        break
    else:
        i += 1
        if indice not in indiceFound:
            indiceFound.append(indice)
i = 0
while True:
    indice = toTest.find(str(toFindR),i)
    if indice == -1:
        break
    else:
        i += 1
        if indice not in indiceFound:
            indiceFound.append(indice)
            
        
print(len(indiceFound))
indiceFound.sort()
for indice in indiceFound:
    print(indice,end= ' ')