import turtle

from Turtle.alfabet import dict_lit
from Turtle.alfabet import desen
from Turtle.alfabet import t
# from Turtle.alfabet import read_dict
# from Turtle.alfabet import read_file
from Turtle.wasd import *
#from Turtle.wasd import exit

def ui():
    running=True
    #while True:
    print("""
    Bitte wahlen:
    0 - exit
    1- worter aus einen worterbuch zu zeichen
    2- eigene zeichnung zu machen""")
    alegere=input('Dein Wahl: ')
    if alegere=='1':
        turtle.ht()
        print(dict_lit())
        desen()
    elif alegere=='0':
        exit()

    elif alegere=='2':
        t.ht()
        wasd()

        # read_dict()
        # read_file()

def read_dict():
    f = open('desene', 'r')
    dict = {}
    nume = input("Name fur den neuen code: ")
    for line in f:
        dict[nume] = line
        open('desene','w')
        print(dict)
    return dict
def read_file():
    #f=open('desene', 'r')
    #for line in f:
        #line.strip()
    for value in read_dict().values() :
        for key in value:
            if key=='w':
                turtle.forward(10)
            if key=='s':
                turtle.forward(-10)
            if key=='a':
                turtle.left(45)
            if key=='d':
                turtle.right(45)
            if key=='f':
                turtle.penup()
            if key=='g':
                turtle.pendown()

#ui()
#turtle.done()