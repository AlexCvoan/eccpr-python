inputString = input()
cifruSubstitutie = input().split()
outputString = ''
for i in range(0, len(inputString)):
    for j in range(0, 62):
        if inputString[i] == cifruSubstitutie[j][0]:
            outputString += cifruSubstitutie[j][2]
    if len(outputString) == i:
        outputString += inputString[i]
print(outputString)