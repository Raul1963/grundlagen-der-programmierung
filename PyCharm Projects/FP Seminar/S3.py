def swap(word):
    vok='aeiou'
    voks=[]
    for ch in word:
        if ch in vok:
            voks.append(ch)
    s=''
    i=1
    for ch in word:
        if ch not in vok:
            s+=ch
        else:
            s+=voks[-i]
            i+=1
    return s

def test_swap():
    assert swap('terminator')=='tormaniter'

def main():
    pass

test_swap()
