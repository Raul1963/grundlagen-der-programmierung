def exmeplu(a,b):
    for i in range(0,5):
        a=a+b
    return a+b, a-b

suma,diff= exmeplu(10,15)


l=[10,11, 12,21, 11,21]
#1
l1=[]
def nr_repetate(l):
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    return l1

print(nr_repetate(l))




