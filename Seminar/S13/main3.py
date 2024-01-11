def find(l,s,e):
    if s>e:
        #return len(l)
        return e+1
    if l[s]!=s:
        return s
    mid=(s+e)//2
    if mid==l[mid]:
        return find(l,mid+1,e)
    else:
        return find(l,s,mid)

l=[0,1,2,3,4,5,6,7]
print(find(l,0,7))