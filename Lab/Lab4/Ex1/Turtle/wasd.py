import sys
import turtle
import pickle
turtle.pen()
turtle.st()
screen=turtle.Screen()
def w():
    turtle.forward(10)
    write_to_file('w')
def s():
    turtle.forward(-10)
    write_to_file('s')
def d():
    turtle.right(45)
    write_to_file('d')

def a():
    turtle.left(45)
    write_to_file('a')
def F():
    turtle.penup()
    write_to_file('f')

def g():
    turtle.pendown()
    write_to_file('g')

def exit():
    write_to_file('\n')
    turtle.bye()



def wasd():

    #while running:
    nume = input("Name fur den neuen code: ")
    screen.onkeypress(w, 'w')
    screen.onkeypress(s, 's')
    screen.onkeypress(a, 'a')
    screen.onkeypress(d, 'd')
    screen.onkeypress(F, 'f')
    screen.onkeypress(g, 'g')
    screen.onkeypress(exit,' ')
    screen.onkeypress(exit, '\n')
    f=open('desene', 'a')
    f.write(f'{nume}: ')
    screen.listen()

    # read_dict()
    #read_file()



def write_to_file(key):
    f=open('desene','a')
    f.write(key)
# read_dict()
# wasd()
#
# #read_file()
#turtle.done()

# read_file()