from functools import reduce
class identifizierbar:
    def __init__(self,id: int):
        self.id=id

class Gericht(identifizierbar):
    def __init__(self,gericht_id,portionsgrosse,preis: int):
        identifizierbar.__init__(self,gericht_id)
        self.portionsgrosse=portionsgrosse
        self.preis=preis
class gekochterGericht(Gericht):
    def __init__(self,gek_gericht_id,portionsgrosse,preis,zubereitungszeit):
        identifizierbar.__init__(self, gek_gericht_id)
        Gericht.__init__(self,portionsgrosse,preis)
        self.zubereitungszeit=zubereitungszeit
class Getrank(Gericht):
    def __init__(self,getrank_id,portionsgrosse,preis,alkoholgehalt):
        identifizierbar.__init__(self, getrank_id)
        Gericht.__init__(self,portionsgrosse,preis)
        self.alkoholgehalt=alkoholgehalt
class Kunde(identifizierbar):
    def __init__(self,id,name,adresse):
        identifizierbar.__init__(self,id)
        self.name=name
        self.adresse=adresse
class Bestellung(identifizierbar):
    def __init__(self,kunden_id: int,gesamtkosten: int,id_gerichte=[],id_getranke=[]):
        identifizierbar.__init__(self,kunden_id)
        self.gesamtkosten=gesamtkosten
        self.id_gerichte=id_gerichte
        self.id_getranke=id_getranke
    # def reduce(self):
    #     functools.reduce(lambda x,y: x+y, self.id_getranke, self.id_gerichte)