from math import gcd

def simplify(frac):
    g=gcd(frac[0], frac[1])

    return frac[0]//g, frac[1]//g

def test_simplify():
    assert simplify((20,12))==(5,3)
def add(a,b):
    return simplify((a[0]*b[1] + b[0]*a[1], a[1]*b[1]))

def sub(a,b):
    return simplify((a[0]*b[1] - b[0]*a[1], a[1]*b[1]))

def mul(a,b):
    return simplify((a[0] * b[0], a[1] * b[1]))
def div(a,b):
    return simplify((a[0] * b[1], a[1] * b[0]))

def add_frac(fracs, frac):
    fracs.append(frac)

def remove_frac(fracs, frac):
    fracs.remove(frac)

def sum_fracs(fracs):
    sum=0,1

    for frac in fracs:
        sum=add(sum,frac)
    return sum

def test_sum():
    assert sum_fracs([(1,2),(2,3),(1,2)])==(5,3)
def test_add():
    assert add((1,2),(2,3))==(7,6)
    assert add((1,2),(1,2))==(1,1)

def test_sub():
    assert sub((3,2), (2,3))==(5,6)
    assert sub((1,2),(5,6))==(-1,3)

def test_mul():
    assert mul((1,2),(1,2))==(1,4)
    assert mul((3,4),(2,3))==(1,2)

def test_div():
    assert div((2,3),(2,3))==(1,1)
    assert div((5,6), (2,3))==(5,4)
def menu():
    return """
    1 - add frac
    2 - calculate sum
    3 - delete previous frac
    0 - exit
    """

def main():
    fracs=[]
    while True:
        print(menu())
        opt=int(input('opt='))
        if opt==1:
            n=int(input('n='))
            m=int(input('m='))

            add_frac(fracs, (n,m))

        if opt == 2:
            n,m=sum_fracs(fracs)
            print('sum=', (n,m))
        if opt == 3:
            remove_frac(fracs, (n,m))

        if opt== 0:
            break
test_add()
test_sub()
test_mul()
test_sum()
test_simplify()
main()
