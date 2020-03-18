nrIntrari = int(input())
deCodat = []
for i in range(nrIntrari):
    deCodat.append(input().split())

primaCodare = []
for x in deCodat:
    intCodat = []
    while x:
        if len(x) >= 2:
            intCodat.append(x[1])
            intCodat.append(x[0])
            x.pop(0)
            x.pop(0)
        else:
            intCodat.append(x[0])
            x.pop(0)
    primaCodare.append(intCodat)

aDouaCodare = []
for x in primaCodare:
    nrUnu = 0
    while len(x) > 1:
        if not int(x[1]) % 2 == 0:
            nrUnu += 1
        x.pop(1)
    nrUnu += int(x[0])
    aDouaCodare.append(nrUnu)
    
print(max(aDouaCodare))