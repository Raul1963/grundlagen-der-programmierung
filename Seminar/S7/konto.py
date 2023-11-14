class Konto:
    def __init__(self, no: int, admin: str,  betrag: int = 0):
        self.no = no
        self.betrag = betrag
        self.admin = admin


    def einzahlen(self, betrag):
        self.betrag += betrag


    def auszahlen(self, betrag):
        self.betrag -= betrag