nrIntrari = int(input())
vectorIntrari = []
vectorConversii = []

for i in range (0, nrIntrari):
    vectorIntrari.append(int(input()))
for deConvertit in vectorIntrari:
    nrBinar = []
    nrBitiZero = 0
    x = deConvertit
    while x:
        if not x % 2 == 0:
            nrBinar.append(1)
        else:
            nrBinar.append(0)
        x = x // 2
    while len(nrBinar) != 8:
        nrBinar.append(0)
    nrBinar.reverse()
    for bit in nrBinar:
        if bit == 0:
            nrBitiZero += 1
    vectorConversii.append(nrBitiZero)
 
for i in range(0, nrIntrari):
    if vectorConversii[i] == max(vectorConversii):
        print(vectorIntrari[i])
    