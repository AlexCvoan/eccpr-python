import copy

def intarzie(d, semnal):
    copieSemnal = copy.deepcopy(semnal)
    semnalIntarziat=[]
    while d:
        semnalIntarziat.append('0')
        copieSemnal.pop()
        d += -1
    for val in copieSemnal:
        semnalIntarziat.append(val)
    return semnalIntarziat
    
def mediere(semnale):
    mediatRaw = [x*0 for x in range(10)]
    mediat = []
    for semnal in semnale:
        for i in range(10):
            mediatRaw[i] += float(semnal[i])
    for val in mediatRaw:
        mediat.append(format((val/len(semnale)),'.2f'))
    return(mediat)
    
nrMics = int(input())
inputSemnale = []
for n in range(nrMics):
    inputSemnale.append(input().split())
    
semnaleNeintarziate = copy.deepcopy(inputSemnale)
semnaleIntarziateUnu = []
semnaleIntarziateDoi = []

for i in range(nrMics):
    semnaleIntarziateUnu.append(intarzie(i, inputSemnale[i]))
for i in range(nrMics):
    semnaleIntarziateDoi.append(intarzie(i*2, inputSemnale[i]))
    

semnaleMediate = []
semnaleMediate.append(mediere(semnaleNeintarziate))
semnaleMediate.append(mediere(semnaleIntarziateUnu))
semnaleMediate.append(mediere(semnaleIntarziateDoi))

for semnal in semnaleMediate:
    for val in semnal:
        print(val, end = ' ')
    print('')
    

