from CreatedExceptions import IDInexistant

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self):
        return "ID: " + str(self.id) +" Name: " + self.name

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
        s = None
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                s = student
                break
        
        if s == None:
            raise IDInexistant
            
        for grade in self.grades:
            if grade.student.id == id:
                self.grades.remove(grade)

    def remove_discipline(self, id):
        d = None
        for discipline in self.disciplines:
            if discipline.id == id:
                self.disciplines.remove(discipline)
                d = discipline
                break
        
        if d == None:
            raise IDInexistant
            
        for grade in self.grades:
            if grade.discipline.id == id:
                self.grades.remove(grade)

        
    
    def update_student(self, student_id, name):
        s = None
        for student in self.students:
            if student.id == student_id:
                student.name = name
                s = student
                break
        
        if s == None:
            raise IDInexistant

    def update_discipline(self, discipline_id, name):
        d = None
        for discipline in self.disciplines:
            if discipline.id == discipline_id:
                discipline.name = name
                d = discipline
                break
        
        if d == None:
            raise IDInexistant

        

    
    def add_discipline(self, name):
        self.discipline_counter += 1
        self.disciplines.append(Discipline(self.discipline_counter, name))

    def add_grade(self, student_id, discipline_id, value):
        s = None
        d = None
        for student in self.students:
            if student.id == student_id:
                s = student
        
        for discipline in self.disciplines:
            if discipline.id == discipline_id:
                d = discipline
        
        if d == None or s == None:
            raise IDInexistant
        else:
            self.grades.append(Grade(s, d, value))
    
    def find_student_by_id(self, id):
        s = None
        for student in self.students:
            if student.id == id:
                s = student
                break
        if s == None:
            raise IDInexistant

        return s
    
    def find_discipline_by_id(self, id):
        d = None
        for discipline in self.disciplines:
            if discipline.id == id:
                d = discipline
                break
        if d == None:
            raise IDInexistant
        return d

    def find_student_by_name(self, text):
        longueur = len(text)
        liste = []
        for student in self.students:
            if len(student.name) >= longueur:
                if text in student.name:
                    liste.append(student)
            else:
                if student.name in text:
                    liste.append(student)
        
        return liste

    def find_discipline_by_name(self, text):
        longueur = len(text)
        liste = []
        for discipline in self.disciplines:
            if len(discipline.name) >= longueur:
                if text in discipline.name:
                    liste.append(discipline)
            else:
                if discipline.name in text:
                    liste.append(discipline)
        
        return liste
    
    def average(self, student, discipline):
        av = 0
        counter = 0
        for grade in self.grades:
                if grade.student.id == student.id and grade.discipline.id == discipline.id:
                    av = av + grade.value
                    counter = counter + 1
        
        return av / counter

        

    def find_failing_students(self):
        failing_liste = []
        for student in self.students:
            for discipline in self.disciplines:
                if self.average(student, discipline) < 5 and student not in failing_liste:
                    failing_liste.append(student)
        return failing_liste
    
   









    
    

    

    