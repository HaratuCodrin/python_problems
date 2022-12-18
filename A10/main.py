from faculty_data import Register
from simple_gui import UserInterface as UI

if __name__ == "__main__":
    register = Register()
    register.add_discipline("Math")
    register.add_student("Marta")

    ui = UI(register)
    ui.loop()
    


