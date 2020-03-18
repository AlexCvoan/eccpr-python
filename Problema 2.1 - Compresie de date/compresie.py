numarIntrari = int(input())
stringIntrari = []

for i in range(0, numarIntrari):
    stringIntrari.append(input().split(sep=','))
for intrare in stringIntrari:
    intrare.append('0')            

for intrare in stringIntrari:
    i = 1
    countZeros = 0
    startZeros = 0
    stringToPrint = ''

    while i < len(intrare):
        if intrare[i - 1] != '0' and intrare[i] == '0' and i != len(intrare)-1:
            countZeros = 0
            startZeros = i
        elif intrare[i - 1] != '0' and intrare[i] != '0' and i != len(intrare)-1:
            stringToPrint += intrare[i-1] + ','
        elif intrare[i -1] == '0' and intrare[i] == '0' and i != len(intrare)-1:
            countZeros += 1
        elif intrare[i-1] == '0' and intrare[i] != '0' and i != len(intrare)-1:
            countZeros += 1
            intrare [startZeros] = countZeros
            stringToPrint += '(' + intrare[startZeros - 1] + ',' + str(intrare[startZeros]) + ')' + ','
            while countZeros - 1:
                intrare.remove('0')
                countZeros += -1
            i = startZeros + 1
        elif intrare[i] == '0' and i == len(intrare) - 1:
            if intrare[i - 1] != '0':
                stringToPrint += intrare[i-1]
            else:
                countZeros += 1
                intrare [startZeros] = countZeros
                stringToPrint += '(' + intrare[startZeros - 1] + ',' + str(intrare[startZeros]) + ')'
            break
        i += 1

    print(stringToPrint)
            




            



        
            
                
    