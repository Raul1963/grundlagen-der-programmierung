from datetime import datetime
import pickle
import os
import functools
from abc import ABC


class Datarepo(ABC):
    def __init__(self, filename):
        self.filename = filename
        # self.objects=[]

    def save(self, objects):
        with open(self.filename, 'ab') as f:
            pickle.dump(objects,f)


    def load(self, objects):
        with open(self.filename, 'rb') as f:
            self.objects = objects
            while True:
                try:
                    if os.path.exists(self.filename):
                        obj = pickle.load(f)
                        self.objects.append(obj)
                except EOFError:
                    break

    def reload(self):
        with open(self.filename, 'wb') as f:
            f.truncate()
    def convert_to_string(self,list):
        result=map(lambda x: str(x), list)
        joined_elements=','.join(result)
        with open(self.filename,'w') as f:
            f.write(joined_elements)
    def convert_from_string(self):
        objects=[]
        with open(self.filename,'r') as f:
            lines=f.readlines()
            for line in lines:
                obj=line.strip()
                objects.append(obj)
        return objects


class CookedDishRepo(Datarepo):
    def __init__(self, filename):
        Datarepo.__init__(self, filename)
        self.gerichte = []
        self.test_gerichte=[]
        if os.path.exists(self.filename):
            self.load(self.gerichte)

        # self.gerichte=[]

    def add(self, gericht):
        self.gerichte.append(gericht)
        self.save(self.gerichte)
    def test_add(self,test_gericht):
        self.test_gerichte.append(test_gericht)
        self.save(self.test_gerichte)
    def find_dish(self, search_dish):
        self.load(self.gerichte)
        for sd in search_dish:
            for dishes in self.gerichte:
                found_dish = list(filter(lambda Gericht: sd in (int(x) for x in str(Gericht.id)), dishes))
                if found_dish:
                    return found_dish

    def delete(self, id):
        self.gerichte.pop(id)
        self.save(self.gerichte)
        self.load(self.gerichte)
    def aktualisieren(self, new_id, new_preis,new_portionsgrosse, new_zubereitungszeit,gericht_actualizat):
        g = []
        with open(self.filename, 'rb') as f:
            gerichte = pickle.load(f)
            g.append(gerichte)
        if gericht_actualizat-1 in range(len(gerichte)):
            gerichte[gericht_actualizat-1].id=new_id
            gerichte[gericht_actualizat-1].preis=new_preis
            gerichte[gericht_actualizat-1].portionsgrosse=new_portionsgrosse
            gerichte[gericht_actualizat-1].zubereitungszeit=new_zubereitungszeit
            self.reload()
            self.save(gerichte)
            self.load(gerichte)


class DrinkRepo(Datarepo):
    def __init__(self, filename):
        Datarepo.__init__(self, filename)
        self.test_getranke=[]
        self.getranke = []
        if os.path.exists(self.filename):
            self.load(self.getranke)

    def add(self, getrank):
        self.getranke.append(getrank)
        self.save(self.getranke)
    def test_add(self,test_getrank):
        self.test_getranke.append(test_getrank)
        self.save(self.test_getranke)
    def delete(self, id):
        self.getranke.pop(id)
        self.save(self.getranke)
        self.load(self.getranke)

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
        self.test_kunden=[]
        self.kunden = []
        if os.path.exists(self.filename):
            self.load(self.kunden)

    def add(self, kunde):
        self.kunden.append(kunde)
        self.save(self.kunden)
    def test_add(self, test_kunde):
        self.test_kunden.append(test_kunde)
        self.save(self.test_kunden)

    def find_costumer_name(self, search_name):
        self.load(self.kunden)
        for costumers in self.kunden:
            found_cost_name = list(filter(lambda Kunde: search_name.lower() in Kunde.name.lower() or search_name.upper() in Kunde.name.upper(),costumers))
            if found_cost_name:
                return found_cost_name

    def find_costumer_adress(self, search_adress):
        self.load(self.kunden)
        for costumers in self.kunden:
            found_cost_adress = list(filter(lambda
                                                Kunde: search_adress.upper() in Kunde.adresse.upper() or search_adress.lower() in Kunde.adresse.lower(),
                                            costumers))
            if found_cost_adress:
                return found_cost_adress

    def aktualisieren(self, nume_actualizat, new_id, new_adress, kunde_actualizat):
        k = []
        with open(self.filename, 'rb') as f:
            kunde = pickle.load(f)
            k.append(kunde)
        if kunde_actualizat-1 in range(len(kunde)):
            kunde[kunde_actualizat-1].id=new_id
            kunde[kunde_actualizat-1].name=nume_actualizat
            kunde[kunde_actualizat-1].adresse=new_adress
            self.reload()
            self.save(kunde)
            self.load(kunde)
    def delete(self, id):
        kunden=self.kunden
        kunden.pop(id)
        self.reload()
        self.save(kunden)
        self.load(kunden)


class OrderRepo(Datarepo):
    def __init__(self, filename):
        Datarepo.__init__(self, filename)
        self.orders = []
        if os.path.exists(self.filename):
            self.load(self.orders)

    def add(self, order):
        self.orders.append(order)
        self.save(self.orders)

    def __totalcost(self, gerichte, getranke):
        gericht_kosten = [gericht.preis for gericht in gerichte]
        getranke_kosten = [getrank.preis for getrank in getranke]
        gesamtkosten =functools.reduce(lambda a,b: a+b,(getranke_kosten+gericht_kosten))
        return gesamtkosten
    def get_totalcost(self,gerichte,getranke):
        return self.__totalcost(gerichte=gerichte,getranke=getranke)

    def rechnung(self,  gerichte, getranke, kunde):
        zeit=datetime.now()
        bestellte_gerichte = [gericht for gericht in gerichte]
        bestellte_getranke = [getrank for getrank in getranke]
        rechnung = f'\n===== Rechnung =====\nKunde: {kunde.name}\nAdresse: {kunde.adresse}\nZeit der Bestellung: {zeit}\nBestellte Gerichte: \n'
        for gericht in bestellte_gerichte:
            rechnung += f"{gericht.id}: {gericht.portionsgrosse} Gramm - {gericht.preis} RON\n"
        rechnung += f"\nBestellte Getränke:\n"
        for getrank in bestellte_getranke:
            rechnung += f"{getrank.id}: {getrank.portionsgrosse} Liter - {getrank.preis} RON\n"
        rechnung += f'\nGesamtkosten:{self.__totalcost(bestellte_gerichte, bestellte_getranke)} RON\n'
        rechnung += f"===================="
        return rechnung
