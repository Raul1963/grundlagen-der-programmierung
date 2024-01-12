from Repository.repo import CookedDishRepo
from Repository.repo import CostumerRepo
from Repository.repo import OrderRepo
from Repository.repo import DrinkRepo
from Controller.Kontroller import gekochterGericht
from Controller.Kontroller import Getrank
from Controller.Kontroller import Kunde

class Test:

    def hinzufugen_test(self):

        repo=CookedDishRepo("gerichtmenu_test.data")
        repo.reload()
        test_dish=gekochterGericht(gericht_id=1,portionsgrosse=100,preis=20,zubereitungszeit=30)
        repo.test_add(test_dish)
        assert test_dish in repo.test_gerichte

    def suchen_test(self):
        repo=CostumerRepo("kundenliste_test.data")
        repo.reload()
        test_kunde=Kunde(Kunde_id=1,name='Raul',adresse='Avram Iancu 6')
        repo.test_add(test_kunde)
        assert test_kunde in repo.find_costumer_name('ra')
        assert test_kunde in repo.find_costumer_adress('av')
    def rechnung_test(self):
        repo=OrderRepo("bestellung_test.data")
        repo.reload()
        DrinkRepo("getrankmenu_test.data").reload()
        test_kunde = Kunde(Kunde_id=1, name='Raul', adresse='Avram Iancu 6')
        test_dish = gekochterGericht(gericht_id=1, portionsgrosse=100, preis=20, zubereitungszeit=30)
        CookedDishRepo("gerichtmenu_test.data").test_add(test_dish)
        test_drink=Getrank(getrank_id=1,portionsgrosse=200,preis=45,alkoholgehalt=36)
        DrinkRepo("getrankmenu_test.data").test_add(test_drink)
        test_dishes = CookedDishRepo("gerichtmenu_test.data").find_dish([1])
        test_drinks = DrinkRepo("getrankmenu_test.data").find_drink([1])
        repo.rechnung(gerichte=test_dishes,getranke=test_drinks,kunde=test_kunde)
        assert repo.get_totalcost(test_dishes,test_drinks)==65
