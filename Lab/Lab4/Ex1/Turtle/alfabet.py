import string
import turtle


import Alfabet.a
from Alfabet.a import *
def dict_lit():

    litere={}
    alfabet=string.ascii_lowercase
    for litera in alfabet:
        functie=f'{litera.upper()}'
        litere[litera]=functie
    return litere

def desen():
    litere=dict_lit()
    word = input("Schreibe ein Wort: ")
    try:
        if word==read_dict(word).values():
            t.ht()
            turtle.st()
            read_dict(word)
            #read_file(word)
    except word==litere[word]:
        t.penup()
        t.goto(-200, 0)
        for litera in word:
            t.pendown()
            if litera=='.':
                dot()
            elif litera=='?':
                intrebare()
            elif litera=='!':
                exclamare()
            elif litera==' ':
                space()
            else:
                functie = litere.get(litera)
                litere[litera] = functie
                functie_nume = getattr(Alfabet.a, functie)

                functie_nume()
            t.penup()
            t.forward(30)

def read_dict(nume):
    dict = {}
    f = open('desene', 'r')
    for line in f:
         line.strip()
         if line.startswith(nume):

             dict[nume]=line[3:-1]
         print(dict)
    for value in dict.values():
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
    return dict
def read_file(nume):
    #f=open('desene', 'r')
    #for line in f:
        #line.strip()
    for value in read_dict(nume).values():
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

#read_dict()

# print(dict_lit())
#desen()
#turtle.done()


