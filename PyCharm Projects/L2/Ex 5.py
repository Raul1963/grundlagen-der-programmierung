l=[31,24,67,57,63,90,42,10,84]
def filtrare(l):
    l5=[]
    for i in range(len(l)):
        x= l[i]//10
        y=l[i]%10
        expression= 'x/y==2'
        if y == 0:
            continue
        if eval(expression)==True:
                l5.append(l[i])
    return l5

print(filtrare(l))