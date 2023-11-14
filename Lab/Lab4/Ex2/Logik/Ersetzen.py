def Count(filename, wort_zu_ersetzen, ersatzwort):
    f=open(filename, 'r')
    count=0
    for line in f:
        words=line.split(' ')
        for word in words:
            word=word.strip()
            if wort_zu_ersetzen==word:
                count+=1
                word.replace(wort_zu_ersetzen, ersatzwort)
                word=word
                # f=open(filename,'w')
                # f.write(' '.join(words))
    return count
