from Logik.Ersetzen import Count
def ui(filename, wort_zu_ersetzen, ersatzwort):

    return (f'Filename:\t {filename}\nWort zu ersetzen:\t{wort_zu_ersetzen} \nErsatzwort:\t\
{ersatzwort} ')
def run(filename, wort_zu_ersetzen, ersatzwort):
    #count = Count(filename, wort_zu_ersetzen, ersatzwort)
    print(ui(filename, wort_zu_ersetzen, ersatzwort))
    while True:
        filename=input("Filename: ")
        wort_zu_ersetzen=input("Wort zu erstezen: ")
        ersatzwort=input("Ersatzwort: ")
        count = Count(filename, wort_zu_ersetzen, ersatzwort)
        if count==0:
            print("Kein Ersetzen ist stattgefunden, bitte wahle ein anderes Wort zu ersetzen")
            continue
        else:
            print(f'Ersetzt {wort_zu_ersetzen} durch {ersatzwort} an {count} Stellen ')

