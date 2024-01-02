from repo.student_repo import Studentrepo
class Controller:
    def __init__(self,repo:Studentrepo):
        self.repo=repo

    def sort_students(self):
        return sorted(self.repo.students)

    def filter_by_street(self, street):
        return [student for student in self.repo.students if student.address.street==street]