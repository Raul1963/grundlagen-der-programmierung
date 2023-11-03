l=[67,76,55,58,87,79,99,10,11]
def domino(l):
    teilfolge_max = []
    teilfolge = []
    contor = 0
    max = 0
    for i in range(0,len(l)-1):
        ult_c=l[i]%10
        pr_c=l[i+1]//10
        if pr_c!=ult_c:
            contor = 0
            teilfolge = []
        else:
            contor = contor + 1
            teilfolge.append(l[i])

        if contor > max:
            max = contor
            teilfolge_max = teilfolge + [l[i+1]]

    return teilfolge_max

print(domino(l))