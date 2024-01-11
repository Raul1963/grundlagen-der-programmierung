def lastap(l: list,n):
    i=len(l)
    if len(l)==0:
        return "Nu s-au gasit elemente"
    if l[-1]==n:
        return l.index(n)
    else:
        return lastap(l[:i-1],n)

print(lastap([1,2,3,4],1))
