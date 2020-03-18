import sys

judete = ['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS', 'CL', 'CJ', 'CT', 'CV', 'DB', 'DJ','GL','GR','GJ','HR','HD','IL','IS','IF','MM','MH','MS','NT','OT','PH','SM','SJ','SB','SV','TR','TM','TL','VS','VL','VN']
inputStrings = []
stringToTest = []
stringsToPrint = []
stringOK = True

while True:
    line = sys.stdin.readline()
    if not line: break
    inputStrings.append(line.strip())   



for i in range(0, len(inputStrings)-1):
    stringToTest = inputStrings[i].split()
    stringOK = True
  #  print (stringToTest)
    if stringToTest[0] in judete:
     #   print('Judet ok')
        if len(stringToTest[1]) > 1 and len(stringToTest[1]) < 4 and stringToTest[1].isdigit():
         #   print('Numar ok')
            if len(stringToTest[2]) == 3:
                for letter in list(stringToTest[2]):
                    if not (ord(letter) >= 65 and ord(letter) <= 90):
                        stringOK = False
                if stringOK:
                 #   print('String ok')
                    stringsToPrint.append(inputStrings[i])   


                        
                
for string in stringsToPrint:
    print(string)
    
    
    
    