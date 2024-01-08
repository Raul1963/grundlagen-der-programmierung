from UI.ui import UI
from Controller.Kontroller import gekochterGericht
from Controller.Kontroller import Controller
from Repository.repo import CookedDishRepo
from Repository.repo import DrinkRepo
from Repository.repo import CostumerRepo

def main():
    print("""
    1. Gerichte
    2. Getranke
    3. Kunde
    """)
    inp=int(input("Wahl: "))
    if inp==1:
        repo=CookedDishRepo("gerichtmenu.data")
        ui=UI(Controller(repo))
        ui.run1()
    elif inp==2:
        repo=DrinkRepo("getrankmenu.data")
        ui = UI(Controller(repo))
        ui.run2()
    elif inp==3:
        repo=CostumerRepo("kundenliste.data")
        ui = UI(Controller(repo))
        ui.run3()

main()