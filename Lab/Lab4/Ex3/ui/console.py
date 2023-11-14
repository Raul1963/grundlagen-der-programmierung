import random
from Logik.schere_stein_papier import spiel
def console(x,y):
    scor_total=(0,0)
    ok=True
    while True:
        scor_total=spiel(x,y)
        if scor_total[0]==3:
            print("Du hast gewonnen")
            return ok==False
        elif scor_total[1]==3:
            print("Der PC hat gewonnen")
            return ok==False
        if ok==False:
            break



