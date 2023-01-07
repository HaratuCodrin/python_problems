from faculty_data import Register, Discipline, Student
from simple_gui import UserInterface as UI

if __name__ == "__main__":
    d = [Discipline(1, "Math"), Discipline(2, "Physique"), Discipline(3, "Roumain")]
    s = [Student(1, "Mihnea"), Student(2, "Cosmin")]

    register = Register(students = s, disciplines = d)
    register.add_student("Codrin")
    register.add_student("Matei")
    register.add_student("Alex")
    

    register.add_grade(1, 1, 10)
    register.add_grade(1, 1, 8)

    register.add_grade(1, 2, 7)
    register.add_grade(1, 2, 8)

    register.add_grade(1, 3, 9)
    register.add_grade(1, 3, 8)

    register.add_grade(2, 1, 5)
    register.add_grade(2, 1, 2)

    register.add_grade(2, 2, 6)
    register.add_grade(2, 2, 6)

    register.add_grade(2, 3, 8)
    register.add_grade(2, 3, 7)

    register.add_grade(3, 1, 4)
    register.add_grade(3, 1, 4)

    register.add_grade(3, 2, 2)
    register.add_grade(3, 2, 7)

    register.add_grade(3, 3, 10)
    register.add_grade(3, 3, 10)

    register.add_grade(4, 1, 7)
    register.add_grade(4, 1, 5)

    register.add_grade(4, 2, 2)
    register.add_grade(4, 2, 2)

    register.add_grade(4, 3, 10)
    register.add_grade(4, 3, 1)

    register.add_grade(5, 1, 4)
    register.add_grade(5, 1, 3)

    register.add_grade(5, 2, 2)
    register.add_grade(5, 2, 10)

    register.add_grade(5, 3, 5)
    register.add_grade(5, 3, 5)

    user_interface = UI(register)
    user_interface.loop()
    


