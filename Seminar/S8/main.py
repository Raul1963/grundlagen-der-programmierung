def Aufgabe2(lista_liste):
    dic_count={}
    for l in lista_liste:
        for el in l:
            if el in dic_count:
                dic_count[el] += 1
            else:
                dic_count[el] = 1
    for i in dic_count:
        for l in lista_liste:
            c = l.count(i) - 1
            if c > 0: dic_count[i] -= c
    l = []
    nr = len(lista_liste)
    for k,v in dic_count.items():
        if v == nr:
            l.append(k)
    return l
print(Aufgabe2([[1,2,3,4],[4,5,1],[1, 7, 8, 5, 1, 4, 6, 1]]))