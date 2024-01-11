class Controller:
    def __init__(self,repo):
        self.repo=repo
class identifizierbar:
    def __init__(self,id: int):
        self.id=id

class Gericht(identifizierbar):
    def __init__(self,gericht_id,portionsgrosse,preis: int):
        identifizierbar.__init__(self,gericht_id)
        self.portionsgrosse=portionsgrosse
        self.preis=preis
class gekochterGericht(Gericht):
    def __init__(self,gericht_id,portionsgrosse,preis,zubereitungszeit):
        Gericht.__init__(self, gericht_id, portionsgrosse, preis)
        self.zubereitungszeit=zubereitungszeit

    def __repr__(self):
        return f'{self.id}. Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}, Zubereitungszeit: {self.zubereitungszeit}'
    def __eq__(self, other):
        if isinstance(other, gekochterGericht):
            return self.id==other.id and self.portionsgrosse==other.portionsgrosse and self.preis==other.preis and self.zubereitungszeit==other.zubereitungszeit
class Getrank(Gericht):
    def __init__(self,getrank_id,portionsgrosse,preis,alkoholgehalt):
        Gericht.__init__(self,getrank_id,portionsgrosse,preis)
        self.alkoholgehalt=alkoholgehalt
    def __repr__(self):
        return f'{self.id}. Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}, Alkoholgehalt: {self.alkoholgehalt}'
class Kunde(identifizierbar):
    def __init__(self,Kunde_id,name,adresse):
        identifizierbar.__init__(self,Kunde_id)
        self.name=name
        self.adresse=adresse
    def __repr__(self):
        return f'{self.id}. Name: {self.name}, Adresse: {self.adresse}'
    def __eq__(self, other):
        # return self.id==other[0].id and self.name==other[0].name and self.adresse==other[0].adresse

        if isinstance(other, Kunde):
            return self.id == other.id and self.name==other.name and self.adresse==other.adresse
class Bestellung(identifizierbar):
    def __init__(self,kunden_id: int,id_gerichte: list,id_getranke: list):
        identifizierbar.__init__(self,kunden_id)
        self.gesamtkosten=0
        self.id_gerichte=id_gerichte
        self.id_getranke=id_getranke
