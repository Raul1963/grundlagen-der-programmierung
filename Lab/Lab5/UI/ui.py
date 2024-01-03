class UI:
    def menu(self):
        return """
        1 - Hinzufugen eines Gerichts 
        2 - Suche nach einem Kunden anhand seines Teilnamens 
        3 - Suche nach einem Kunden anhand seiner Teiladresse 
        4 - Aktualisieren eines Kundennamens
        5 - Generierung der Rechnung
        6 - Speicherung einer Bestellung
        7 - Einlesen einer Bestellung
        8 - Exit
        """
    def run(self):
        while True:
            print(self.menu())
            opt=int(input("Input: "))
            if opt==1:
                id=int(input('Id: '))
                portionsgrosse=(input('Portionsgrosse: '))
                preis=(input('Preis: '))
            if opt==2:
                students=self.controller.sort_students()
                for student in students:
                    print(student)

            if opt==4:
                street=input("Street: ")
                students=self.controller.filter_by_street(street)
                for student in students:
                    print(student)
            if opt==8:
                break