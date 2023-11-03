l=[11,34,56,23,98,10]
def criptare_lista(l):
    l4=[]
    l4.append(l[0])
    for i in range(1,len(l)):
        nr=int(l[i])+int(l[0])
        l4.append(nr)
    return l4

print(criptare_lista(l))

