import pickle
import os
import Controller.Kontroller
from Controller.Kontroller import *
from abc import ABC
class Datarepo(ABC):
    def __init__(self,filename):
        self.filename=filename
        # self.objects=[]
    def save(self,objects):
        f=open(self.filename,'ab')
        pickle.dump(objects,f)
        f.close()
    def load(self,objects: list):
        f=open(self.filename,'rb')
        self.objects=objects
        while True:
           try:
                if os.path.exists(self.filename):
                    obj=pickle.load(f)
                    self.objects.append(obj)
           except EOFError:
               break
        f.close()
    def delete(self):
        f=open(self.filename,'wb')
        #self.objects=pickle.load(f)
        f.close()

class CookedDishRepo(Datarepo):
    def __init__(self,filename):
        Datarepo.__init__(self,filename)
        self.gerichte=[]
        if os.path.exists(self.filename):
            self.load(self.gerichte)
        #self.gerichte=[]
    def add(self, gericht):
        self.gerichte.append(gericht)
        self.save(self.gerichte)

    def find_dish(self, search_dish):
        self.load(self.gerichte)
        for sd in search_dish:
            for dishes in self.gerichte:
                found_dish = list(filter(lambda Gericht: sd in (int(x) for x in str(Gericht.id)), dishes))
                if found_dish:
                    return found_dish

class DrinkRepo(Datarepo):
    def __init__(self, filename):
        Datarepo.__init__(self, filename)
        self.getranke=[]
        if os.path.exists(self.filename):
            self.load(self.getranke)
    def add(self, getrank):
        self.getranke.append(getrank)
        self.save(self.getranke)
    def find_drink(self, search_drink):
        self.load(self.getranke)
        for d in search_drink:
            for drinks in self.getranke:
                found_drink = list(filter(lambda Getrank: d in (int(x) for x in str(Getrank.id)), drinks))
                if found_drink:
                    return found_drink

class CostumerRepo(Datarepo):
    def __init__(self, filename):
        Datarepo.__init__(self, filename)
        self.kunden=[]
        if os.path.exists(self.filename):
            self.load(self.kunden)

    def add(self, kunde):
        self.kunden.append(kunde)
        self.save(self.kunden)
    def find_costumer_name(self, search_name):
        self.load(self.kunden)
        for costumers in self.kunden:
            found_cost_name=list(filter(lambda Kunde: search_name.lower() in Kunde.name.lower() or search_name.upper() in Kunde.name.upper(), costumers))
            # if not IndexError:
            #     continue
            if found_cost_name:
                return found_cost_name
    def find_costumer_adress(self, search_adress):
        self.load(self.kunden)
        for costumers in self.kunden:
            found_cost_adress=list(filter(lambda Kunde:  search_adress.upper() in Kunde.adresse.upper()or search_adress.lower() in Kunde.adresse.lower(), costumers))
            if found_cost_adress:
                return found_cost_adress
class OrderRepo(Datarepo):
    def __init__(self, filename):
        Datarepo.__init__(self, filename)
        self.orders=[]
        if os.path.exists(self.filename):
            self.load(self.orders)
    def add(self, order):
        self.orders.append(order)
        self.save(self.orders)

    def totalcost(self, gerichte, getranke):
        gericht_kosten = [gericht.preis for gericht in gerichte]
        getranke_kosten = [getrank.preis for getrank in getranke]
        gesamtkosten = sum(gericht_kosten) + sum(getranke_kosten)
        return gesamtkosten

    def rechnung(self, gericht,gerichte, getrank,getranke, kunde):
        bestellte_gerichte = [gericht for gericht.id in gerichte]
        bestellte_getranke = [getrank for getrank.id in getranke]
        rechnung = f'\n===== Rechnung =====\nKunde: {kunde.name}\nAdresse: {kunde.adresse}\nBestellte Gerichte: \n'
        for gericht in bestellte_gerichte:
            rechnung += f"{gericht.id}: {gericht.portionsgrosse} Gramm - {gericht.preis} RON\n"
        rechnung += f"\nBestellte Getränke:\n"
        for getrank in bestellte_getranke:
            rechnung += f"{getrank.id}: {getrank.portionsgrosse} Liter - {getrank.preis} RON\n"
        rechnung += f'\nGesamtkosten:{self.totalcost(bestellte_gerichte, bestellte_getranke)} Euro\n'
        rechnung += f"===================="
        return rechnung