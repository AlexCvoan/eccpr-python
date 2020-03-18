nrMaxim = int(input())
inputAutobuze = input().split()
sumaAbsenti = 0
totalAutobuze = []

for i in range(nrMaxim):
    totalAutobuze.append(str(i + 1))

for autobuz in totalAutobuze:
    if not autobuz in inputAutobuze:
        sumaAbsenti += int(autobuz)

print(sumaAbsenti)



