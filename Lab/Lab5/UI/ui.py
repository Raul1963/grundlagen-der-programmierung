from Controller.Kontroller import gekochterGericht
from Controller.Kontroller import Getrank
from Controller.Kontroller import Controller
from Controller.Kontroller import *
from Controller.Kontroller import Bestellung
from Repository.repo import OrderRepo
class UI:
    def __init__(self, c: Controller):
        self.repo = None
        self.c=c
    def menu(self):
        return """
        1 - Hinzufugen eines Gerichts/Getranks
        2 - Anzeigen des Menus
        3 - Suche nach einem Kunden anhand seiner Teiladresse 
        4 - Aktualisieren eines Kundennamens
        5 - Generierung der Rechnung
        6 - Speicherung einer Bestellung
        7 - Einlesen einer Bestellung
        8 - Exit
        """
    def run1(self):
        while True:
            print(self.menu())
            opt=int(input("Input: "))
            if opt==1:
                id=int(input('Id: '))
                portionsgrosse=(input('Portionsgrosse: '))
                preis=int(input('Preis: '))
                zubereitungszeit=int(input('Zubereitungszeit: '))
                self.c.repo.add(gekochterGericht(gericht_id=id, portionsgrosse=portionsgrosse, preis=preis, zubereitungszeit=zubereitungszeit))


            if opt==2:
                gerichtmenu=self.c.repo.gerichte
                for gericht in gerichtmenu:
                    print(gericht)
            if opt==3:
                self.c.repo.delete()
            if opt==8:
                break
    def run2(self):
        while True:
            print(self.menu())
            opt=int(input("Input: "))
            if opt==1:
                id=int(input('Id: '))
                portionsgrosse=(input('Portionsgrosse: '))
                preis=int(input('Preis: '))
                alkoholgehalt=int(input('Alkoholgehalt: '))
                self.c.repo.add(Getrank(getrank_id=id, portionsgrosse=portionsgrosse, preis=preis, alkoholgehalt=alkoholgehalt))


            if opt==2:
                getrankmenu=self.c.repo.getranke
                for getrank in getrankmenu:
                    print(getrank)
            if opt==3:
                self.c.repo.delete()
            if opt==8:
                break
    def run3(self):
        while True:
            print(self.menu())
            opt=int(input("Input: "))
            if opt==1:
                id=int(input('Id: '))
                name=(input('Name: '))
                adresse=input('Adresse: ')
                self.c.repo.add(Kunde(Kunde_id=id, name=name, adresse=adresse))
            if opt==2:
                find=int(input("Suche den Kunde anhand\n 1. seiner Teilnamen\n 2.seiner Teiladresse\n"))
                if find==1:
                    f_name=input("Teilname: ")
                    # self.repo=CostumerRepo("kundenliste.data")

                    f_cost_name=self.c.repo.find_costumer_name(f_name)
                    for fcn in f_cost_name:
                        print(f"Id: {fcn.id}, Name: {fcn.name}, Adresse: {fcn.adresse}")
                        besttellte_gerichte = []
                        besttellte_getranke = []
                    while True:
                        #wahl=int(input("1. Mochten sie die Rechnung \n2. Mochten sie bestellen "))

                        ger1 = int(input("ID-Gericht: "))

                        get1 = int(input("ID-Getrank: "))

                        self.repo = OrderRepo("bestellung.data")
                        self.c=Controller(self.repo)
                        if ger1 == 0 and get1 == 0:
                            Bestellung(kunden_id=fcn.id,id_gerichte=besttellte_gerichte, id_getranke=besttellte_getranke)
                            dish=CookedDishRepo("gerichtmenu.data").find_dish(besttellte_gerichte)
                            drinks=DrinkRepo("getrankmenu.data").find_drink(besttellte_getranke)
                            rechnung=self.c.repo.rechnung(gericht=gekochterGericht,gerichte=dish, getrank=Getrank,getranke=drinks,kunde=fcn)
                            print(rechnung)
                        else:
                            besttellte_getranke.append(get1)
                            besttellte_gerichte.append(ger1)
                            self.c.repo.add(Bestellung(kunden_id=fcn.id,id_gerichte=besttellte_gerichte, id_getranke=besttellte_getranke))
                elif find==2:
                    f_adresse=input("Teiladresse: ")
                    f_cost_adress=self.c.repo.find_costumer_adress(f_adresse)
                    for fca in f_cost_adress:
                        print(fca)
            if opt==3:
                self.c.repo.delete()
            if opt==8:
                break