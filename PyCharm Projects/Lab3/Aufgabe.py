import turtle
t=turtle.Pen()
t1=turtle.Pen()
t2=turtle.Pen()
def rechteck():
    t.st()
    t1.ht()
    t2.ht()
    t.up()
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.down()
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.up()
    t.forward(75)
    t.left(90)
    t.forward(37.5)
    t.down()
    for i in range(2):
        t.forward(25)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.reset()


#rechteck()

def curbura():
    for i in range(200):
        t.right(1)
        t.forward(1)
def linie():
    for i in range(200):
        t.right(0.15)
        t.forward(1)

def herz():
    t.st()
    t1.ht()
    t2.ht()
    t.left(90)
    curbura()
    linie()
    t.right(81)
    linie()
    curbura()
    t.reset()


#herz()
def haus():
    t.forward(100)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(75)
    t.up()


def hauser():
    t1.st()
    t2.st()
    t.ht()
    t1.speed(10)
    t1.speed(10)
    t1.up()
    t2.up()
    t1.goto(-200,0)
    t2.goto(125,0)
    t1.down()
    t2.down()
    for i in range(4):
        zid(125,90)
    t1.up()
    t2.up()
    for i in range(2):
        zid(125,90)
    t1.down()
    t2.down()
    t1.right(45)
    t2.right(45)
    t1.forward(88)
    t2.forward(88)
    t1.left(90)
    t2.left(90)
    t1.forward(88)
    t2.forward(88)
    t1.left(45)
    t2.left(45)
    usa()
    fereastra()
    t1.reset()
    t2.reset()

def zid(x,y):
    t1.forward(x)
    t1.left(y)
    t2.forward(x)
    t2.left(y)

def usa():
    t1.up()
    t2.up()
    t1.forward(125)
    t2.forward(125)
    t1.left(90)
    t1.forward(45)
    t2.left(90)
    t2.forward(45)
    t1.down()
    t2.down()
    t1.left(90)
    t1.forward(45)
    t2.left(90)
    t2.forward(45)
    t1.right(90)
    t1.forward(35)
    t2.right(90)
    t2.forward(35)
    t1.right(90)
    t1.forward(45)
    t2.right(90)
    t2.forward(45)

def fereastra():
    t1.up()
    t2.up()
    for i in range(2):
        t1.right(90)
        t2.right(90)
        t1.forward(80)
        t2.forward(80)
    t1.right(90)
    t1.forward(20)
    t2.right(90)
    t2.forward(20)
    t1.down()
    t2.down()
    for i in range(4):
        t1.forward(20)
        t1.left(90)
        t2.forward(20)
        t2.left(90)
    # #for i in range(8):
    #     t1.left(90)
    #     t2.left(90)
    #     t1.forward(10)
    #     t2.forward(10)
    #     t1.right(90)
    #     t2.right(90)
    #     t1.forward(10)
    #     t2.forward(10)

def menu():
    return """
    Wahlen Sie eine Zeichnung aus:
    0. Exit
    1. Rechteck
    2. Herz
    3. Hauser
    """

def main():
    while True:
        print(menu())
        try:
            n=int(input())

            if n==1:
                rechteck()
                continue
            elif n==2:
                herz()
                continue
            elif n==3:
                hauser()
                continue
            elif n==0:
                exit()
            else:
                print("Das war nicht ein Nummer von der Liste")
        except ValueError:
            print("Das war nicht ein Nummer von der Liste")
main()
turtle.done()


