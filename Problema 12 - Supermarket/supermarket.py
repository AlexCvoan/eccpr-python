class Supermarket:
    codBare = ''
    tip = ''
    valoare = 0
    
    def __init__(self, stringCod, charTip, intValoare):
        self.codBare = stringCod
        self.tip = charTip
        self.valoare = intValoare
        
dateIntrare = input().split()
intrariSupermarket = []
reducereBool = False
valoareReducere = 0
valoareCos = 0

for i in range(0, int(dateIntrare[0])):
    intrare = input().split()
    intrariSupermarket.append(Supermarket(intrare[0],intrare[1],float(intrare[2])))
    
produseCos = input().split()

for produs in produseCos:
    for item in intrariSupermarket:
        if item.codBare == produs:
            if item.tip == 'p':
                valoareCos += item.valoare
            elif item.tip == 'c':
                valoareReducere += item.valoare
            
if not valoareReducere == 0:
    print(float(valoareCos - valoareCos * valoareReducere / 100))
else:
    print(valoareCos)
        
    
    