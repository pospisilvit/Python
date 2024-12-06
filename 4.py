class VanocniStrom:
   
    def __init__(self, typ_stromu):
        self.strom = typ_stromu
        self.ozdoby = []
 
    def getTypStromu(self):
        return self.strom
 
    class Ozdoby:
        def __init__(self, typ, barva, pocet):
 
            self.__typ = typ
            self.__barva = barva
            self.__pocet = pocet
       
        def getTyp(self):
            return self.__typ
 
        def getBarva(self):
            return self.__barva
 
        def getPocet(self):
            return self.__pocet  
 
 
    def ozdob(self, typ, barva, pocet):
        for i in range(pocet):
            self.ozdoby.append((f"{typ}: {barva}"))
 
    def getOzdoby(self):
        return self.ozdoby
 
   
strom = VanocniStrom("borovice")
strom.ozdob("světelný řetez", "studená bílá", 1)
strom.ozdob("koule", "červená", 10)
strom.ozdob("koule", "bílá", 10)
strom.ozdob("girlanda", "bílá", 3)
strom.ozdob("girlanda", "červená", 3)
strom.ozdob("cukrovinka", "hnědá", 20)
 
print(f"{strom.getTypStromu()} \n**********")
for ozdoby in strom.getOzdoby():
    print(ozdoby)