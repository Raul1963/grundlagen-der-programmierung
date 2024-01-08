from functools import reduce
from Repository.repo import CookedDishRepo
from Repository.repo import Datarepo
from Repository.repo import CostumerRepo
from Repository.repo import DrinkRepo
from Repository.repo import OrderRepo
from Repository.repo import Datarepo
from abc import ABC
class Controller(ABC):
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

    def __str__(self):
        return f'{self.id}. Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}, Zubereitungszeit: {self.zubereitungszeit}'
class Getrank(Gericht):
    def __init__(self,getrank_id,portionsgrosse,preis,alkoholgehalt):
        Gericht.__init__(self,getrank_id,portionsgrosse,preis)
        self.alkoholgehalt=alkoholgehalt
    def __str__(self):
        return f'{self.id}. Portionsgrosse: {self.portionsgrosse}, Preis: {self.preis}, Alkoholgehalt: {self.alkoholgehalt}'
class Kunde(identifizierbar):
    def __init__(self,Kunde_id,name,adresse):
        identifizierbar.__init__(self,Kunde_id)
        self.name=name
        self.adresse=adresse
    def __repr__(self):
        return f'{self.id}. Name: {self.name}, Adresse: {self.adresse}'
    def __eq__(self, other):
        return self.id==other[0].id and self.name==other[0].name and self.adresse==other[0].adresse
class Bestellung(identifizierbar):
    def __init__(self,kunden_id: int,id_gerichte: list,id_getranke: list):
        identifizierbar.__init__(self,kunden_id)
        self.gesamtkosten=0
        self.id_gerichte=id_gerichte
        self.id_getranke=id_getranke
    # def totalcost(self, gerichte,getranke):
    #     gericht:Gericht
    #     getrank: Getrank
    #     gericht_kosten=[gericht.preis for gericht in gerichte if gericht.id in self.id_gerichte ]
    #     getranke_kosten=[getrank.preis for getrank in getranke if getrank.id in self.id_getranke]
    #     gesamtkosten=sum(gericht_kosten)+sum(getranke_kosten)
    #     return gesamtkosten
    # def rechnung(self,gerichte,getranke,kunde):
    #     gericht: Gericht
    #     getrank: Getrank
    #     bestellte_gerichte=[gericht for gericht in gerichte if gericht.id in self.id_gerichte]
    #     bestellte_getranke=[getrank for getrank in getranke if getrank.id in self.id_getranke]
    #     rechnung = f'\n===== Rechnung =====\nKunde: {kunde.name}\nAdresse: {kunde.adresse}\nBestellte Gerichte: \n'
    #     for gericht in bestellte_gerichte:
    #         rechnung += f"{gericht.id}: {gericht.portionsgrosse} Gramm - {gericht.preis} RON\n"
    #     rechnung += f"\nBestellte Getränke:\n"
    #     for getrank in bestellte_getranke:
    #         rechnung += f"{getrank.id}: {getrank.portionsgrosse} Liter - {getrank.preis} RON\n"
    #     rechnung += f'\nGesamtkosten:{self.gesamtkosten} Euro\n'
    #     rechnung += f"===================="
    #     return rechnung