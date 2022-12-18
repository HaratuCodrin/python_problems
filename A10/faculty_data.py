from CreatedExceptions import IDInexistant

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Discipline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
class Grade:
    def __init__(self, student, discipline, value):
        self.student = student
        self.discipline = discipline
        self.value = value


class Register:
    students = []
    disciplines = []
    grades = []
    student_counter = 0
    discipline_counter = 0

    def __init__(self, students = [], disciplines = [], grades = []):
        self.students = students
        for student in self.students:
            self.student_counter += 1
        self.grades = grades
        self.disciplines = disciplines
        for discipline in self.disciplines:
            self.discipline_counter += 1
    
    def display_students(self):
        for student in self.students:
            print("ID: " + str(student.id) + ", name: " + str(student.name))

    def display_disciplines(self):
        for discipline in self.disciplines:
            print("ID: " + str(discipline.id) + ", name: " + str(discipline.name))
    

    def add_student(self, name):
        self.student_counter += 1
        self.students.append(Student(self.student_counter, name))
    
    def remove_student(self, id):
        for grade in self.grades:
            if grade.student.id == id:
                self.grades.remove(grade)
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                break
        
    
    def add_discipline(self, name):
        self.discipline_counter += 1
        self.disciplines.append(Discipline(self.discipline_counter, name))

    def add_grade(self, student_id, discipline_id, value):
        stud = None
        disc = None
        for student in self.students:
            if student.id == student_id:
                stud = student
        
        for discipline in self.disciplines:
            if discipline.id == discipline_id:
                disc = discipline
        
        if disc == None or stud == None:
            raise IDInexistant
        else:
            self.grades.append(Grade(stud, disc, value))


    
    

    

    