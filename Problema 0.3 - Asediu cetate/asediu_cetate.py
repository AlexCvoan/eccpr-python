dateIntrare = []
dateIntrare = input().split()
dateIntrare = [int(i) for i in dateIntrare]

dateIntrare[0] -= 1
dateIntrare[2] -= 1

soldati = []
for x in range(1, dateIntrare[1] + 1):
    soldati.append(x)

indexSoldatOut = dateIntrare[2] 
while len(soldati) != 1:
    indexSoldatOut += dateIntrare[0]
    while indexSoldatOut >= len(soldati):
        indexSoldatOut -= len(soldati)
    del soldati[indexSoldatOut]

print(soldati[0])