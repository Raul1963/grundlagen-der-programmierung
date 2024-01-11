from Controller.Kontroller import gekochterGericht
from Controller.Kontroller import Getrank
from Controller.Kontroller import Controller
from Controller.Kontroller import Kunde
from Controller.Kontroller import Bestellung
from Repository.repo import OrderRepo
from Repository.repo import CostumerRepo
from Repository.repo import CookedDishRepo
from Repository.repo import DrinkRepo
class UI:
    def __init__(self, c: Controller):
        self.repo = None
        self.c=c
    def menu(self):
        return """
        1 - Hinzufugen 
        2 - Anzeigen 
        3 - Delete 
        4 - Aktualisieren 
        5 - Exit
        """
    def menu_kunden(self):
        return """
                1 - Hinzufugen 
                2 - Anzeigen 
                3 - Delete
                4 - Suchen und Bestellung machen
                5 - Aktualisieren 
                6 - Exit
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
                for gericht in range(len(gerichtmenu)):
                    print(f"{gerichtmenu[gericht]}")
            if opt==3:
                index=int(input("Welches Gericht mochten sie loschen: "))
                self.c.repo.delete(index-1)
            if opt==4:
                f_id = int(input("Id: "))
                f_dish = self.c.repo.find_dish(f_id)
                for fd in f_dish:
                    print(f"Id: {fd.id}, : Portionsgrosse: {fd.portionsgrosse}, Preis: {fd.preis}, Zubereitungszeit: {fd.zubereitungszeit}")
                new_id = int(input("Id: "))
                new_portionsgrosse = input("Portionsgrosse: ")
                new_preis = input("Preis: ")
                new_zubereitungszeit=input("Zubereitungszeit: ")
                self.c.repo.aktualisieren(new_id=new_id, new_portionsgrosse=new_portionsgrosse,new_preis=new_preis,new_zubereitungszeit=new_zubereitungszeit,gericht_actualizat=fd.id)
            if opt==5:
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
                    print(f"{getrank}")
            if opt==3:
                index = int(input("Welches Gericht mochten sie loschen: "))
                self.c.repo.delete(index - 1)
            if opt==5:
                break
    def run3(self):
        while True:
            print(self.menu_kunden())
            opt=int(input("Input: "))
            if opt==1:
                id=int(input('Id: '))
                name=(input('Name: '))
                adresse=input('Adresse: ')
                self.c.repo.add(Kunde(Kunde_id=id, name=name, adresse=adresse))
            if opt==2:
                kundenliste = self.c.repo.kunden
                for kunde in kundenliste:
                    print(kunde)
            if opt==3:
                index = int(input("Welches Kunde mochten sie loschen: "))
                self.c.repo.delete(index - 1)
            if opt==4:
                find=int(input("Suche den Kunde anhand\n1. seiner Teilnamen\n2. seiner Teiladresse\n"))
                if find==1:
                    f_name=input("Teilname: ")
                    self.repo=CostumerRepo("kundenliste.data")

                    f_cost_name=self.c.repo.find_costumer_name(f_name)
                    for fcn in f_cost_name:
                        print(f"Id: {fcn.id}, Name: {fcn.name}, Adresse: {fcn.adresse}")
                    besttellte_gerichte = []
                    besttellte_getranke = []
                    while True:
                        ger1 = int(input("ID-Gericht: "))
                        get1 = int(input("ID-Getrank: "))
                        self.repo = OrderRepo("bestellung.data")
                        self.c=Controller(self.repo)
                        if ger1 == 0 and get1 == 0:
                            Bestellung(kunden_id=fcn.id,id_gerichte=besttellte_gerichte, id_getranke=besttellte_getranke)
                            dishes=CookedDishRepo("gerichtmenu.data").find_dish(besttellte_gerichte)
                            drinks=DrinkRepo("getrankmenu.data").find_drink(besttellte_getranke)
                            rechnung=self.c.repo.rechnung(dishes,drinks,fcn)
                            print(rechnung)
                            break
                        else:
                            besttellte_getranke.append(get1)
                            besttellte_gerichte.append(ger1)
                            self.c.repo.add(Bestellung(kunden_id=fcn.id,id_gerichte=besttellte_gerichte, id_getranke=besttellte_getranke))
                elif find==2:
                    f_adresse=input("Teiladresse: ")
                    self.repo = CostumerRepo("kundenliste.data")
                    f_cost_adress=self.c.repo.find_costumer_adress(f_adresse)
                    for fca in f_cost_adress:
                        print(fca)
                    besttellte_gerichte = []
                    besttellte_getranke = []
                    while True:
                        ger1 = int(input("ID-Gericht: "))
                        get1 = int(input("ID-Getrank: "))

                        self.repo = OrderRepo("bestellung.data")
                        self.c = Controller(self.repo)
                        if ger1 == 0 and get1 == 0:
                            Bestellung(kunden_id=fca.id, id_gerichte=besttellte_gerichte,
                                       id_getranke=besttellte_getranke)
                            dishes = CookedDishRepo("gerichtmenu.data").find_dish(besttellte_gerichte)
                            drinks = DrinkRepo("getrankmenu.data").find_drink(besttellte_getranke)
                            rechnung = self.c.repo.rechnung(dishes, drinks, fca)
                            print(rechnung)
                            break
                        else:
                            besttellte_getranke.append(get1)
                            besttellte_gerichte.append(ger1)
                            self.c.repo.add(Bestellung(kunden_id=fca.id,id_gerichte=besttellte_gerichte, id_getranke=besttellte_getranke))
            if opt==5:
                self.repo=CostumerRepo("kundenliste.data")
                f_name = input("Teilname: ")
                f_cost_name = self.c.repo.find_costumer_name(f_name)
                for fcn in f_cost_name:
                    print(f"Id: {fcn.id}, Name: {fcn.name}, Adresse: {fcn.adresse}")
                new_id=int(input("Id: "))
                new_name=input("Name: ")
                new_adresse=input("Adresse: ")
                self.c.repo.aktualisieren(new_id=new_id, nume_actualizat=new_name, new_adress=new_adresse,kunde_actualizat=fcn.id)
            if opt==6:
                break