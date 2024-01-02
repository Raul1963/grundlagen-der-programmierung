class Address:
    def __init__(self,street:str,number:int):
        self.street=street
        self.number=number

    def __str__(self):
        return f'street:{self.street}, number:{self.number}'