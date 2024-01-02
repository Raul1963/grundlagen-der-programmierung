class identifizierbar:
    def __init__(self,id: int):
        self.id=id

class Gericht(identifizierbar):
    def __init__(self,id,portionsgrosse,preis: int):
        identifizierbar.__init__(self,id)
        self.portionsgrosse=portionsgrosse
        self.preis=preis
class gekochterGericht(Gericht):
    def __init__(self,portionsgrosse,preis,zubereitungszeit):
        Gericht.__init__(self,portionsgrosse,preis)
        self.zubereitungszeit=zubereitungszeit
class Getrank(Gericht):
    def __init__(self,portionsgrosse,preis,alkoholgehalt):
        Gericht.__init__(self,portionsgrosse,preis)
        self.alkoholgehalt=alkoholgehalt
class Kunde(identifizierbar):
    def __init__(self,id,name,adresse):
        identifizierbar.__init__(self,id)
        self.name=name
        self.adresse=adresse
class Bestellung(identifizierbar):
    def __init__(self,id: int,gesamtkosten: int,id_gerichte=[],id_getranke=[]):
        identifizierbar.__init__(self,id)
        self.id_gerichte=id_gerichte
        self.id_getranke=id_getranke
        self.gesamtkosten=gesamtkosten
    def __reduce__(self):
        pass