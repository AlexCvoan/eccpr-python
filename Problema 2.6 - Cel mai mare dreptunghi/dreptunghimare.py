nrDr = int(input())
vectorDr = []
arieMax = 0
initArieMax = ''

for i in range(nrDr):
    vectorDr.append(input().split())

for dr in vectorDr:
    arie = (int(dr[3]) - int(dr[1])) * (int(dr[4]) - int(dr[2]))
    if arie > arieMax:
        arieMax = arie
        initArieMax = dr[0] + ' ' + dr[1] + ' ' + dr[2] + ' ' + dr[3] + ' ' + dr[4] + ' ' + str(round(arieMax))
        
print(initArieMax)
    