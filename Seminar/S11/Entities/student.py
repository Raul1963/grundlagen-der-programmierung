from Entities.adress import Address
class Student:
    def __init__(self,name:str,address:Address):
        self.name=name
        self.address=address
    def __str__(self):
        return f'Nume:{self.name}, Address:{self.address}'

    def __eq__(self, other):
        #return self.name==other.name and aelf.address.number==other.address.number
        #and self.address.street==other.address.street
        return self.name==other.name

    def __lt__(self, other):
        return self.name<other.name






















