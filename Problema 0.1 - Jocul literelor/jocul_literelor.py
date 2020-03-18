testInput = input().lower().split()
testWords = input().lower().split()
firstTest = 0
secondTest = 0
thirdTest = 0

for word in testWords:
    currentWord = list(word)
    if currentWord[0] == testInput[0] and currentWord[-1] == testInput[1]:
        if len(word) < int(testInput[2]):
            firstTest += 1
        elif len(word) >= int(testInput[2]) and len(word) < int(testInput[3]):
            secondTest += 1
        else:
            thirdTest += 1

result = str(firstTest) + " " + str(secondTest) + " " + str(thirdTest)

print(result)
       
