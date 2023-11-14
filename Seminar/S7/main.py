from auto import Auto
from die import Die, f
from frac import Frac
from statistics import Statistics
from test import test_count_color

from konto import Konto

def main():
    # d = Die(6)
    # roll = d.roll()
    # while roll != 6:
    #     print(f'rolled: {roll}')
    #     roll = d.roll()
    #
    # print(f'rolled: {roll}')
    #
    # f()

    f1 = Frac(4,12)
    f1.reduce()
    print(f'{f1.n}/{f1.m}')

    s = Statistics()
    autos = [Auto('m1', 'm2', 1000, 'red'),
             Auto('m1', 'm2', 1000, 'blue'),
             Auto('m1', 'm2', 1000, 'red')
             ]
    color = 'red'
    print(f'#red autos= {s.count_color(autos, color)}')

    print(f'avg year= {s.avg_year(autos, "m1")}')

    k1 = Konto('101A', 'Peter', 100)
    print(k1.betrag)

    k2 = Konto('101B', 'Peter')
    print(k2.betrag)


test_count_color()
main()