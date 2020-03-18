import sys
from copy import copy, deepcopy
import math

inputNumbers = []
matrix = []
while True:
    line = sys.stdin.readline()
    if not line: break
    inputNumbers.append(line[0:len(line)-1])   

numarLinii = int(inputNumbers[0])
inputNumbers.pop(0)
numarColoane = int(inputNumbers[0])
inputNumbers.pop(0)

for coloana in range(0, numarColoane):
    linieNoua = []
    for linie in range(0, numarLinii):
        linieNoua.append(int(inputNumbers[0]))
        inputNumbers.pop(0)
    matrix.append(linieNoua)

newMatrix = deepcopy(matrix)
sumaElemente = 0

for coloana in range(0, numarColoane):
    for linie in range(0, numarLinii):
        newMatrix[coloana][linie] = math.floor(newMatrix[coloana][linie] * 0.9 + 2)
        sumaElemente = sumaElemente + newMatrix[coloana][linie] - matrix[coloana][linie]

print(round(sumaElemente/((coloana+1)*(linie+1)), 2))