import sys

dateIntrare = []
vectorConc = []
while True:
    line = sys.stdin.readline()
    if not line: break
    dateIntrare.append(line)

while dateIntrare:
    tempVar = int(dateIntrare[0])
    dateIntrare.pop(0)
    vectorConc.extend(dateIntrare[0:tempVar])
    del dateIntrare[0:tempVar]

vectorConc = list(map(int, vectorConc))
output = 0
vectorConc = sorted(vectorConc)
if len(vectorConc) < 6:
    print (0)
else:
    numarValori = len(vectorConc) - 5
    for i in range(0, numarValori):
        output += vectorConc.pop()
        
outputResult = format(round(output/numarValori,2),'.2f')
print (outputResult)