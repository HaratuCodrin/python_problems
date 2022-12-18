
class UserInterface:

    options = [
        "############# STUDENT AND DISCIPLINE REGISTER ############",
        "Pick an option:",
        "1. Add a student.",
        "2. Display all students.",
        "3. Add a discipline.",
        "4. Display all disciplines.",
        "5. Remove a student by ID.",
        "6. Remove a discipline by ID.",
        "7. Search for a student by ID/name.",
        "8. Search for a discipline by ID/name",
        "9. Exit."
    ]

    def __init__(self, register):
        self.register = register

    def loop(self):
        while True:
            self.display()
            choice = input("Your choice:")
            choice = choice.strip()

            if choice == "1":
                name = input("Enter the new student's name:")
                self.register.add_student(name)
            elif choice == "2":
                self.register.display_students()
            elif choice == "3":
                name = input("Enter the new discipline's name:")
                self.register.add_discipline(name)
            elif choice == "4":
                self.register.display_disciplines()
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                pass
            elif choice == "8":
                pass
            elif choice == "9":
                print("Bisous!")
                exit(1)

            input("Press anything to continue...")


    def display(self):
        for option in self.options:
            print(option)

        
