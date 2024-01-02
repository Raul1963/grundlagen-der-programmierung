from UI.ui import Console
from repo.student_repo import Studentrepo
from logik.logic import Controller
from repo.student_repo import Filestudentrepo
def main():
    print("Welches repo? 1 - Memory/ 2 - File")
    wahl=int(input())
    if wahl==1:
        repo=Studentrepo()
    else:
        repo=Filestudentrepo('student.data')
    c=Console(Controller(repo))
    c.run()

main()