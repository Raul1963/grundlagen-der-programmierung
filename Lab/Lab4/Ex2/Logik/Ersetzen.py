def Count(filename, wort_zu_ersetzen, ersatzwort):
    f=open(filename, 'w')
    count=0
    for line in f:
        words=line.split(' ')
        for word in words:
            word=word.strip()
            if wort_zu_ersetzen==word:
                count+=1
    return count


