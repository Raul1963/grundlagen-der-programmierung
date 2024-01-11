def get_culomn(i,N,m):
    if len(m)!=N*N:
        raise ValueError('Nu e patratic')
    col=[]
    for pos,ch in enumerate(m):
        if pos%N==i:
            col.append(ch)
    return col
def test_get_column():
    assert get_culomn(0,3,'012345678')==['0','3','6']
    assert get_culomn(1,3,'012345678')==['1','4','7']
    #assert get_culomn(2,3,'012345678')==['0','5','6']

print(get_culomn(0,2,'3'))
test_get_column()