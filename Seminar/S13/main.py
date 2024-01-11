def sorted_merge(l1,l2):
    l=[]
    i,j=0,0
    while i<len(l1) and j < len(l2):
        if l1[i]>l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    return l + l1[i:] + l2[j:]
print(sorted_merge([1,3,7],[0,2,4]))