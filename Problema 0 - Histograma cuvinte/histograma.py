from collections import Counter
stringInput = input()
result = Counter(stringInput.lower().split())
for key, value in sorted(result.items(), key=lambda item: (-item[1], item[0])):
    toPrint = key + ' ' + str(value)
    print(toPrint)