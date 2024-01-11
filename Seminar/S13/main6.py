def find1(l,i=0):
    if len(l)==0:
        return 0
    if i==len(l)-1:
        if l[i]==1:
            return 1
        else:
            return 0
    if l[i]==1:
        return 1 + find1(l[i+1:],i)
    else:
        return find1(l[i+1:],i)

print(find1([1,2,3,1,2,3,3,5,1,34]))