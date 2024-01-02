from logik.logic import Controller
from Entities.adress import Address
from Entities.student import Student
class Console:
    def __init__(self,controller:Controller):
        self.controller=controller

    def menu(self):
        return """
        1 - add student
        2 - sort students
        3 - Exit
        4 - filter by street
        """
    def run(self):
        while True:
            print(self.menu())
            opt=int(input("Input: "))
            if opt==1:
                name=input("Name: ")
                street=input("Street: ")
                number=int(input("Number: "))

                self.controller.repo.add(Student(name,Address(street=street,number=number)))
            if opt==2:
                students=self.controller.sort_students()
                for student in students:
                    print(student)
            if opt==3:
                break
            if opt==4:
                street=input("Street: ")
                students=self.controller.filter_by_street(street)
                for student in students:
                    print(student)