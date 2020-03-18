nrIntrari = int(input())
vectorIntrare = input().split()
vectorBucket = []
for i in range(19):
    vectorBucket.append(0)
    
for x in vectorIntrare:
    if int(x) >= 0 and int(x) <= 9:
        vectorBucket[0] += 1
    elif int(x) >= 10 and int(x) <= 99:
        vectorBucket[1] += 1
    elif int(x) >= 100 and int(x) <= 999:
        vectorBucket[2] += 1
    elif int(x) >= 1000 and int(x) <= 9999:
        vectorBucket[3] += 1
    elif int(x) >= 10000 and int(x) <= 99999:
        vectorBucket[4] += 1
    elif int(x) >= 100000 and int(x) <= 999999:
        vectorBucket[5] += 1
    elif int(x) >= 1000000 and int(x) <= 9999999:
        vectorBucket[6] += 1
    elif int(x) >= 10000000 and int(x) <= 99999999:
        vectorBucket[7] += 1
    elif int(x) >= 100000000 and int(x) <= 999999999:
        vectorBucket[8] += 1
    elif int(x) >= 1000000000 and int(x) <= 9999999999:
        vectorBucket[9] += 1
    elif int(x) >= 10000000000 and int(x) <= 99999999999:
        vectorBucket[10] += 1
    elif int(x) >= 100000000000 and int(x) <= 999999999999:
        vectorBucket[11] += 1
    elif int(x) >= 1000000000000 and int(x) <= 9999999999999:
        vectorBucket[12] += 1
    elif int(x) >= 10000000000000 and int(x) <= 99999999999999:
        vectorBucket[13] += 1
    elif int(x) >= 100000000000000 and int(x) <= 999999999999999:
        vectorBucket[14] += 1
    elif int(x) >= 1000000000000000 and int(x) <= 9999999999999999:
        vectorBucket[15] += 1
    elif int(x) >= 10000000000000000 and int(x) <= 99999999999999999:
        vectorBucket[16] += 1
    elif int(x) >= 100000000000000000 and int(x) <= 999999999999999999:
        vectorBucket[17] += 1
    elif int(x) >= 1000000000000000000 and int(x) <= 999999999999999999:
        vectorBucket[18] += 1
        
for i in range(19):
    if not vectorBucket[i] == 0:
        print(str(i + 1) + ' ' + str(vectorBucket[i]))
    
    