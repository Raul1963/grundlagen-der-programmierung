import math


class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X = {self.x}, Y = {self.y}'

    # def __sub__(self, other):
    #     return Punct(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Cerc:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return f'Aria = {self.aria()}, Raza = {self.r}, {self.c}'

    def __sub__(self, other):
        # c = Cerc(self.r - other.r, self.c - other.c) #wrong
        c = Cerc(self.r - other.r, Punct(self.c.x - other.c.x, self.c.y - other.c.y)) #pentru ca sub din clasa punct returneaza distanta intre doua puncte
        return c

    def aria(self):
        return math.pi * self.r ** 2


def move(c1, c2):
    while not(c1.c - c2.c <= c1.r + c2.r):
        c1.c.x += 1




def main():
    p1 = Punct(14, 2)
    p2 = Punct(3, 5)
    p3 = p1 - p2
    # print(p3.x, p3.y)
    print(p3)
    c1 = Cerc(5, p1)
    c2 = Cerc(5, Punct(100, 2))
    move(c1, c2)
    print(c1)
    c3 = c1 - c2
    print(c3)


main()