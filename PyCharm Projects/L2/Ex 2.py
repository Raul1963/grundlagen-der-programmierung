l=[10, 11, 12, 21, 13, 40, 56,  22, 65,65]
l2=[]
def ist_symmetrisch(a,b):
    return str(a)==str(b)[::-1]

print(ist_symmetrisch(12,21))
def perechi_simetrice(l):
    nr_perechi_sim=0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if ist_symmetrisch(l[i],l[j]):
                nr_perechi_sim+=1
    return nr_perechi_sim



print(perechi_simetrice(l))