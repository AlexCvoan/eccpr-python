import sys
from copy import deepcopy

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n//2 + 1):
        if i == n:
            break
        if n % i == 0:
            return False
    return True

problemInput = []

while True:
    line = sys.stdin.readline()
    if not line: break
    problemInput.append(line.rstrip())

numarColoane = int(problemInput[0])
problemInput.pop(0)
numarLinii = int(problemInput[0])
problemInput.pop(0)

matrix = []

for coloana in range(0, numarColoane):
    linieNoua = []
    for linie in range(0, numarLinii):
        linieNoua.append(int(problemInput[0]))
        problemInput.pop(0)
    matrix.append(linieNoua)

newMatrix = deepcopy(matrix)
countOnes = 0

for coloana in range(0, numarColoane):
    for linie in range(0, numarLinii):
        if isPrime(newMatrix[coloana][linie]):
            newMatrix[coloana][linie] = 0
        else:
            newMatrix[coloana][linie] = 1
        if newMatrix[coloana][linie] == 1:
            countOnes += 1

print(countOnes)