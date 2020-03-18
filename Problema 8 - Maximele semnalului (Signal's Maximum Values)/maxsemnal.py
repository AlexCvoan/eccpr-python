vectorLength = input()
vectorSignal = []
vectorMaxPoints = []
counter = 0
sum = 0

for i in range(0, int(vectorLength)):
    x = input()
    vectorSignal.append(float(x))

for i in range(0, int(vectorLength)):
    if i == 0:
        if vectorSignal[i] > vectorSignal[i+1]:
            vectorMaxPoints.append(vectorSignal[i])
    elif i == (int(vectorLength) - 1):
        if vectorSignal[i] > vectorSignal[i-1]:
            vectorMaxPoints.append(vectorSignal[i])
    elif vectorSignal[i] > vectorSignal[i-1] and vectorSignal[i] > vectorSignal[i+1]:
        vectorMaxPoints.append(vectorSignal[i])

for point in vectorMaxPoints:
    sum += float(point)

average = sum / len(vectorMaxPoints)

for point in vectorSignal:
    if float(point) > average:
        counter += 1

print(counter)
    
    

    