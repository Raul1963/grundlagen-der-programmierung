import random

def spiel(x,y):
    l=['Schere', 'Papier', 'Stein']


    scor=0
    scor_pc=0
    while True:
        if scor<3 and scor_pc<3:

            x = random.choice(l)
            y = str(input("Dein Wahl:"))
            if y not in l:
                print("Das war nicht ein Wahl aus der Liste")
                continue
            print(f"PC Wahl: {x}")
            if x==y:
                continue
            if x=='Schere' and y=='Papier':
                scor_pc+=1
            if x=='Schere' and y=='Stein':
                scor+=1
            if x=='Papier' and y=='Schere':
                scor+=1
            if x=='Papier' and y=='Stein':
                scor_pc+=1
            if x=='Stein' and y=='Schere':
                scor_pc+=1
            if x=='Stein' and y=='Papier':
                scor+=1
            print(scor)
            print(scor_pc)
        else:
            break


    return scor, scor_pc






