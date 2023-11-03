l=[12,10,50,99,60]
def nr_mare(l):
    sum=''
    l.sort(reverse=True)
    for i in l:
        string1=str(i)
        sum= sum + string1
    return sum
print(nr_mare(l))