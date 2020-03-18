import math

nrInputs = int(input())
inputVector = []
arieMaxima = 0
initArieMax = ''

for i in range(nrInputs):
    inputVector.append(input().split())
    
for forma in inputVector:
    if forma[0] == 'patrat':
        arie = float(forma[1]) * float(forma[1])
    elif forma[0] == 'dreptunghi':
        arie = float(forma[1]) * float(forma[2])
    elif forma[0] == 'cerc':
        arie = math.pi * float(forma[1]) * float(forma[1])
    
    if arie > arieMaxima:
        arieMaxima = arie
        if not forma[0] == 'dreptunghi':
            initArieMax = forma[0] + ' ' + forma[1]
        else:
            initArieMax = forma[0] + ' ' + forma[1] + ' ' + forma[2]
      
print(initArieMax)

    
    