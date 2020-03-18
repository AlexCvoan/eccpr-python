class Campionat:
    numeEchipa = 'echipaStandard'
    punctajEchipa = 0
    goluriMarcate = 0
    goluriIncasate = 0

    def denumireEchipa(self, string):
        self.numeEchipa = string
    def castigaMeci(self):
        self.punctajEchipa += 3
    def goluriMarcateMeci(self, integer):
        self.goluriMarcate += integer
    def goluriIncasateMeci(self, integer):
        self.goluriIncasate += integer
    def remizaMeci(self):
        self.punctajEchipa += 1
    def __init__(self, string):
        self.numeEchipa = string

echipeCampionat = []
meciuriRaw = []
numeEchipe = []
numarEchipe = int(input())
numarMeciuri = int(input())



for i in range(0, numarMeciuri):
    meciuriRaw.append(input())

for i in range(0, numarMeciuri):
    meciFormat = meciuriRaw[i].split()
    if not meciFormat[0] in numeEchipe:
        numeEchipe.append(meciFormat[0])
    if not meciFormat[4] in numeEchipe:
        numeEchipe.append(meciFormat[4])
    

for i in range(0, numarEchipe):
        echipeCampionat.append(Campionat(numeEchipe[i]))

while meciuriRaw:
    meciFormat = meciuriRaw[0].split()
    del(meciFormat[2])
    for echipa in echipeCampionat:
        if meciFormat[0] == echipa.numeEchipa:
            if meciFormat[1] > meciFormat[2]:
                echipa.castigaMeci()
                echipa.goluriMarcateMeci(int(meciFormat[1]))
                echipa.goluriIncasateMeci(int(meciFormat[2]))
            elif meciFormat[1] == meciFormat[2]:
                echipa.remizaMeci()
                echipa.goluriMarcateMeci(int(meciFormat[1]))
                echipa.goluriIncasateMeci(int(meciFormat[2]))
            else:
                echipa.goluriMarcateMeci(int(meciFormat[1]))
                echipa.goluriIncasateMeci(int(meciFormat[2]))              
                
        if meciFormat[3] == echipa.numeEchipa:
            if meciFormat[2] > meciFormat[1]:
                echipa.castigaMeci()
                echipa.goluriMarcateMeci(int(meciFormat[2]))
                echipa.goluriIncasateMeci(int(meciFormat[1]))
            elif meciFormat[1] == meciFormat[2]:
                echipa.remizaMeci()
                echipa.goluriMarcateMeci(int(meciFormat[2]))
                echipa.goluriIncasateMeci(int(meciFormat[1]))
            else:
                echipa.goluriMarcateMeci(int(meciFormat[2]))
                echipa.goluriIncasateMeci(int(meciFormat[1]))
    meciuriRaw.pop(0)

echipeCampionat.sort(key=lambda x: x.punctajEchipa, reverse=True)

for echipa in echipeCampionat:
    toPrint = echipa.numeEchipa + ' ' + str(echipa.punctajEchipa) + ' ' + str(echipa.goluriMarcate) + ' ' + str(echipa.goluriIncasate)
    print(toPrint)










