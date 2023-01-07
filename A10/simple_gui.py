from sys import exit
from CreatedExceptions import IDInexistant

class UserInterface:

    options = [
        "############# STUDENT AND DISCIPLINE REGISTER ############",
        "Pick an option:",
        "1. Add a student.",
        "2. Add a grade",
        "3. Add a discipline.",
        "4. Update a student",
        "5. Update a discipline",
        "6. Display all students.",
        "7. Display all disciplines.",
        "8. Remove a student by ID.",
        "9. Remove a discipline by ID.",
        "10. Search for a student by ID.",
        "11. Search for a discipline by ID",
        "12. Search for a student by name.",
        "13. Search for a discipline by name",
        "14. Find all failing students.",
        "15. Exit."
    ]

    def __init__(self, register):
        self.register = register

    def loop(self):
        while True:
            for option in self.options:
                print(option)
            choice = input("Your choice:")
            choice = choice.strip()

            if choice == "1":
                name = input("Enter the new student's name:")
                self.register.add_student(name)
            elif choice == "2":
                id = int(input("Enter the student's id:"))
                discipline = int(input("Enter the discipline id:"))
                valeur = float(input("Enter the grade:"))
                try:
                    self.register.add_grade(id, discipline, valeur)
                except(IDInexistant):
                    print("The id is not there.")
            elif choice == "3":
                name = input("Enter the new discipline's name:")
                self.register.add_discipline(name)
            elif choice == "4":
                id = int(input("Enter the student's id:"))
                name = input("Enter the new name for the student:")
                try:
                    self.register.update_student(id, name)
                except(IDInexistant):
                    print("The id is not there.")
            elif choice == "5":
                id = int(input("Enter the discipline's id:"))
                name = input("Enter the new name for the discipline:")
                try:
                    self.register.update_discipline(id, name)
                except(IDInexistant):
                    print("The id is not there.")
            elif choice == "6":
                self.register.display_students()
            elif choice == "7":
                self.register.display_disciplines()
            elif choice == "8":
                id = int(input("Enter the student's id:"))
                try:
                    self.register.remove_student(id)
                except(IDInexistant):
                    print("The id is not there.")
            elif choice == "9":
                id = int(input("Enter the discipline's id:"))
                try:
                    self.register.remove_discipline(id)
                except(IDInexistant):
                    print("The id is not there.")
            elif choice == "10":
                id = int(input("Enter the student's id:"))
                try:
                    s = self.register.find_student_by_id(id)
                    print("ID: " + str(s.id) +" Name: " + s.name)
                except(IDInexistant):
                    print("There is no such student.")
            elif choice == "11":
                id = int(input("Enter the discipline's id:"))
                try:
                    d = self.register.find_discipline_by_id(id)
                    print("ID: " + str(d.id) +" Name: " + d.name)
                except(IDInexistant):
                    print("There is no such discipline.")
            elif choice == "12":
                text = input("Enter the search word:")
                liste = self.register.find_student_by_name(text)
                if len(liste) == 0:
                    print("No such student.")
                else:
                    for student in liste:
                        print("ID: " + str(student.id) +" Name: " + student.name)
            elif choice == "13":
                text = input("Enter the search word:")
                liste = self.register.find_discipline_by_name(text)
                if len(liste) == 0:
                    print("No such discipline.")
                else:
                    for discipline in liste:
                        print("ID: " + str(discipline.id) +" Name: " + discipline.name)
            elif choice == "14":
                liste = self.register.find_failing_students()
                if len(liste) == 0:
                    print("No student has failed.")
                else:
                    for student in liste:
                        print(student)
            elif choice == "15":
                print("Bye Bye!")
                exit(1)

            input("Press anything to continue...")

        
