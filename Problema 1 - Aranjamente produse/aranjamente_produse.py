import math

dateIntrare = []
dateIntrare = input().split()

k = int(dateIntrare[0])
M = int(dateIntrare[1])
testFactorial = 0
n = k

if math.factorial(n)/math.factorial(n-k) > M:
    print('0')
    testFactorial = M + 1
while testFactorial <= M:
    testFactorial = math.factorial(n)/math.factorial(n-k)
    if testFactorial > M:
        n -= 1
        print(n)
        break
    n+=1


