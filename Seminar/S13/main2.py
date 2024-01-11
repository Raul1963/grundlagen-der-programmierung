def recursive_sort(l):
    if len(l)==0:
        return []
    if l[0]==0:
        return [0]+ recursive_sort(l[1:])
    else:
        return recursive_sort(l[1:])+ [1]

l=[1,0,0,1,0,1,1,0]
print(recursive_sort(l))