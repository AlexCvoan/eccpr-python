nrCategorii = int(input())
inputCategorii = input().split()
for i in range(nrCategorii):
    inputCategorii[i] = int(inputCategorii[i])
nrOperatiuni = int(input())
inputOperatiuni = []
for i in range(nrOperatiuni):
    inputOperatiuni.append(input().split())

operatiuniNerealizate = 0 
nrAprovizionari = 0
    
for operatiune in inputOperatiuni:
    if operatiune.count('0') == len(operatiune):
        for i in range(nrCategorii):
            inputCategorii[i] += 10
        nrAprovizionari += 1
    else:
        eRealizabil = True
        for i in range(nrCategorii):
            if (inputCategorii[i] - int(operatiune[i])) < 0:
                eRealizabil = False
        if eRealizabil:
            for i in range(nrCategorii):
                inputCategorii[i] -= int(operatiune[i])
        else:
            operatiuniNerealizate += 1

print(operatiuniNerealizate)
print(nrAprovizionari)
    

    
