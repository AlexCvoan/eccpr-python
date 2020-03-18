import math

nrPuncte = int(input())
vectorPuncte = []
vectorDistante = []
vectorDistanteRounded = []
for i in range (nrPuncte):
    vectorPuncte.append(input().split())

for i in range (nrPuncte - 1):
    distanta = math.sqrt(pow((float(vectorPuncte[i+1][0]) - float(vectorPuncte[i][0])),2) + pow((float(vectorPuncte[i+1][1]) - float(vectorPuncte[i][1])),2))
    vectorDistante.append(distanta)
    
vectorDistante.append(math.sqrt(pow((float(vectorPuncte[0][0]) - float(vectorPuncte[-1][0])),2) + pow((float(vectorPuncte[0][1]) - float(vectorPuncte[-1][1])),2)))

for distanta in vectorDistante:
    vectorDistanteRounded.append(round(distanta,3))
    
for distanta in vectorDistanteRounded:
    print(distanta)

testFinal = True

if not vectorDistanteRounded.count(vectorDistanteRounded[0]) == len(vectorDistanteRounded):
    testFinal = False
    
if testFinal == True:
    print('da')
else:
    print('nu')