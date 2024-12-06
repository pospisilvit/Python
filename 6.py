class Tovarna:
    def __init__(self, typ_darku):
        self.darek = typ_darku
        self.darky = []
 
    def vyrobDarek(self):
        return self.darek
   
    class Darek:
        def __init__(self, typ, pocet):
            self.typ = typ
            self.pocet = pocet
 
        def getTyp(self):
            return self.typ
 
        def getPocet(self):
            return self.pocet
       
    def vyrabej(self, typ, pocet):
        for i in range(pocet):
            self.darky.append((f"{typ}: {pocet}"))
 
    def GetDarky(self):
        return self.darky
   
darky = Tovarna("Dárky")
darky.vyrabej("Autíčko", 5)
darky.vyrabej("Panenka", 4)
darky.vyrabej("Fotbalový míč", 2)
darky.vyrabej("Mobil", 3)
darky.vyrabej("Tablet", 2)
darky.vyrabej("Sluchátka", 2)
 
print(f"{darky.vyrobDarek()} \n**********")
for i in darky.GetDarky():
    print(i)