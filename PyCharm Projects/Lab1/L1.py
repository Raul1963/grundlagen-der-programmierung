#1a)
def verificare_nr_prime(p):
    if p <2:
        return False
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
def generare_nr_prime(n):
    prim=[]
    for p in range(2, n):
        if verificare_nr_prime(p)==True:
            prim.append(p)
    return prim

nr=int(input())
n=nr-1
print(generare_nr_prime(nr))



#1b)

def func(m):
    teilfolge_max=[]
    teilfolge=[]
    contor=0
    x=-1
    max=0
    for i in range(1, m+1):
        y=int(input())
        if y<=x:
            contor=0
            teilfolge=[]
        else:
            contor=contor+1
            teilfolge.append(y)
        if contor>max:
            max=contor
            teilfolge_max=teilfolge
        x=y           #Actualizare termen anterior
    return teilfolge_max




m=int(input())
print(func(m))

#4a)
x=int(input())
def gasire_termen_apropiat(x):
    for i in range(0,int(x**(1/2))):
        if i<int(x**(1/2)):
            i+=1
        if i==int(x**(1/2)):
            x=i

    return x

print(gasire_termen_apropiat(x))

#3b)
# #def gasire_nr_prime(x):
#     prim=False
#     if x< 2:
#         return False
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#            return False
#     return True
# x=int(input())
# print(gasire_nr_prime(x))

# def func2(m):
#     teilfolge_max = []
#     teilfolge = []
#     ok = 0
#
#     max = 0
#     for i in range(1, m + 1):
#         y =int(input())
#         if gasire_nr_prime(y)==False:
#             ok = 0
#             teilfolge = []
#         else:
#             ok = ok + 1
#             teilfolge.append(y)
#         if ok > max:
#             max = ok
#             teilfolge_max = teilfolge
#
#     return teilfolge_max
# m=int(input())
# print(func2(m))


#4b)
def gasire_dif_nr_prime(a,b):
    if b-a< 2:
        return False
    for i in range(2, int((b-a)**0.5)+1):
        if (b-a)%i==0:
           return False
    return True
# a=int(input())
# b=int(input())
# print(gasire_dif_nr_prime(a,b))
def func2(lista):
    teilfolge_max = []
    teilfolge = []
    ok = 0
    max = 0
    for i in range(len(lista)-1):
        if gasire_dif_nr_prime(lista[i],lista[i+1]):
            ok = ok + 1
            teilfolge.append(lista[i])
        else:
            ok = 0
            teilfolge = []
        if ok > max:
            max = ok
            teilfolge_max = teilfolge + [lista[i+1]]
    return teilfolge_max
l=[1,2,4,6,7,1,2,5,10,12,14]
print(func2(l))

