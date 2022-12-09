from Services import Services
from collections import deque
from ComplexNumber import ComplexNumber as CN

class UserInterface:

    options = [
        "############# COMPLEX NUMBERS ############",
        "Pick an option:",
        "1. Add a number to the list.",
        "2. Display the numbers.",
        "3. Filter between 'start' and 'end'.",
        "4. Undo last move.",
        "5. Exit."
    ]

    liste = [
        CN(1, 2),
        CN(-3, -1),
        CN(1, 1),
        CN(6, 7),
        CN(-4, 8),
        CN(4, -8),
        CN(-2, -2),
        CN(5, -5),
        CN(0, 1),
        CN(1, 0),
    ]
    moves = deque()

    def __init__(self):
        self.services = Services(self.liste, self.moves)

    def loop(self):
        while True:
            self.display()
            choice = input("Your choice:")
            choice = choice.strip()

            if choice == "1":
                real = int(input("Real part:"))
                img = int(input("Imaginary part:"))
                
                self.services.add_number(real, img)
            elif choice == "2":
                self.services.display_liste()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print("Bisous!")
                exit(1)

            input("Press anything to continue...")


    def display(self):
        for option in self.options:
            print(option)

        