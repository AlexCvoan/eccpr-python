import sys
import string


problemInput = []

while True:
    line = sys.stdin.readline()
    if not line: break
    problemInput.append(line.rstrip())

stringToFilter = problemInput[0]
wordNumber = int(problemInput[1])
wordsToTest = problemInput[2].split()


for i in range (0, wordNumber):
    replacedWord = "*" * len(wordsToTest[i])
    stringToFilter = stringToFilter.replace(wordsToTest[i], replacedWord)

print (stringToFilter.rstrip())