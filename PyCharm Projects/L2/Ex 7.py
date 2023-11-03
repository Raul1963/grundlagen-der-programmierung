l=[10,24,12,48,11, 13, 67]
def ggt(a,b):
    if a==0:
        return b
    return ggt(b%a,a)
def kgv(a,b):
    return (a*b)//ggt(a,b)


def kgv_lista(l, f_id, t_id):
    kgv_rezultat=l[f_id]

    for i in range(f_id, t_id):
        kgv_rezultat=kgv(kgv_rezultat, l[i+1])

    return kgv_rezultat

From=int(input())
To=int(input())
print('From: ',From)
print('To: ',To)
f_id=From
t_id=To


print(kgv_lista(l,f_id,t_id))