import pickle
import os

class Studentrepo:
    def __init__(self):
        self.students=[]
    def add(self,student):
        self.students.append(student)
    def find(self,name):
        for student in self.students:
            if student.name==name:
                return student
        return None

class Filestudentrepo(Studentrepo):
    def __init__(self,filename):
        Studentrepo.__init__(self)
        self.filename=filename
        if os.path.exists(self.filename):
            self.load()
    def save(self):
        f=open(self.filename,'ab')
        pickle.dump(self.students,f)
        f.close()
    def add(self,student):
        super().add(student)
        self.save()

    def load(self):
        f=open(self.filename,'rb')
        self.students=pickle.load(f)
        f.close()


