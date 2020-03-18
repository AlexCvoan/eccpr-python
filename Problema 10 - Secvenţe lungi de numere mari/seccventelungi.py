numarValori = int(input())
vectorValori = []
for i in range(0, numarValori):
    vectorValori.append(float(input()))
prag = float(input())

vectorProcesat = []
for i in range(0, numarValori):
    if vectorValori[i] > prag:
        vectorProcesat.append(1)
    else:
        vectorProcesat.append(0)
        
vectorProcesat.append(0)
        
numarSecvente = 0

#print(vectorProcesat)

for i in range(1, numarValori + 1):
    if vectorProcesat[i] == 0 and vectorProcesat[i-1] == 1:
        numarSecvente += 1

print(numarSecvente)
        

