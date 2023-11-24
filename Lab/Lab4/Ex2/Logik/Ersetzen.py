def Count(filename, wort_zu_ersetzen, ersatzwort):
    f=open(filename, 'r')
    count=0
    l=[]
    for line in f:
        words=line.split(' ')

        for word in words:

            if word.endswith('\n'):
                word=word.strip()
                l.append(word)
                l.append('\n')
            else:
                l.append(word)
            if wort_zu_ersetzen==word:
                count+=1
                word.replace(wort_zu_ersetzen, ersatzwort)
                word=word
                for i in range(len(l)):
                    if l[i]==wort_zu_ersetzen:
                        l[i]=ersatzwort
    open(filename, 'w')
    # for new_word in l:
    f=open(filename, 'a')
    f.write(' '.join(l))

    return count
