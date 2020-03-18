import math

dateIntrare = []
dateIntrare = input().split()

n = int(dateIntrare[0])
dateIntrare.pop(0)
M = int(dateIntrare[0])
dateIntrare.pop(0)

testCombinari = 0

for index in range (0, n):
    testCombinari = math.factorial(n)/(math.factorial(index)*math.factorial(n-index))
    if testCombinari >= M:
        break
if testCombinari < M:
    index = 0
print(index)
    