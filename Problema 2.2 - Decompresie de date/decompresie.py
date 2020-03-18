numarIntrari = int(input())
stringIntrari = []

for i in range(0, numarIntrari):
    stringIntrari.append(input().split(sep=','))
#for intrare in stringIntrari:
#    intrare.append('0')            

for intrare in stringIntrari:
    i = 0
    stringToPrint = ''
  
    while i < len(intrare):
        if not '(' in intrare[i] and not ')' in intrare[i]:
            stringToPrint += intrare[i] + ','
        elif '(' in intrare[i]:
            stringToPrint += intrare[i][1:] + ','
            for j in range(0, int(intrare[i+1][:len(intrare[i+1])-1])):
                stringToPrint += '0,'
            
        i += 1
    print(stringToPrint[:len(stringToPrint)-1])
   
  




            



        
            
                
    