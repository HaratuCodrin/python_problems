from Functions import *

options = [
    "######## Programming Contest ########",
    "1) Display all contestants.", 
    "2) Delete scores at position x.", 
    "3) Add result of a new participant.",
    "4) Insert results at a position.",
    "5) Delete scores from position a to position b.",
    "6) Replace a certain score of a participant.",
    "7) Display all contestants with a certain condition.",
    "8) Exit program."
]

secondary_options = [
    "######## Pick another option ########",
    "1) Display all contestants in decreasing order of average score.",
    "2) Display all contestants with an average below n."
    "3) Display all contestants with an average over n."
    "4) Display all contestants with an average equal to n."
]

def menu_instance(list):
    print()
    for option in options:
        print(option)

    choice = input("Choose an option:")
    choice = choice.strip()

    if choice == "1":
        display(list)
    elif choice == "2":
        pos = int(input("Enter position of the contestant x = ").strip())
        try:
            remove(list, pos)
        except IndexError:
            print("Participant doesn't exist, try again...")
    elif choice == "3":
        grade1 = int(input("Enter grade 1 of the new contestant:").strip())
        grade2 = int(input("Enter grade 2 of the new contestant:").strip())
        grade3 = int(input("Enter grade 3 of the new contestant:").strip())
        add_new_result(list, grade1, grade2, grade3)
    elif choice == "4":
        pos = int(input("Enter position of the contestant x =").strip())
        grade1 = int(input("Enter grade 1 of the new contestant:").strip())
        grade2 = int(input("Enter grade 2 of the new contestant:").strip())
        grade3 = int(input("Enter grade 3 of the new contestant:").strip())
        try:
            insert_result(list, pos, grade1, grade2, grade3)
        except IndexError:
            print("Participant doesn't exist, try again...")
    elif choice == "5":
        pos1 = int(input("Enter first position a = ").strip())
        pos2 = int(input("Enter first position b = ").strip())
        try:
            remove_from_a_to_b(list, pos1, pos2)
        except IndexError:
            print("Some participants don't exist, try again...")
    elif choice == "6":
        pos = int(input("Enter position of the contestant x =").strip())
        problem = int(input("Enter the number of the problem = ").strip())
        grade = int(input("Enter the grade = "))
        try:
            replace_score(list, pos, problem, grade)
        except IndexError:
            print("Participant doesn't exist, try again...")
        except NoSuchProblem:
            print("Wrong problem number, try again...")
    elif choice == "7":
        for option in secondary_options:
            print(option)
        secondary_choice = input("Your choice:").strip()
        if secondary_choice == "1":
            display_sorted(list)
        elif secondary_choice == "2":
            n = int(input("Enter a value n = "))
            print("The contestants with average below", n, ":")
            try:
                display_below_n(list, n)
            except NoSuchProblem:
                print("No such participants...")
        elif secondary_choice == "3":
            n = int(input("Enter a value n = "))
            print("The contestants with average over", n, ":")
            try:
                display_over_n(list, n)
            except NoSuchProblem:
                print("No such participants...")
        elif secondary_choice == "4":
            n = int(input("Enter a value n = "))
            print("The contestants with average equal to", n, ":")
            try:
                display_equal_n(list, n)
            except NoSuchProblem:
                print("No such participants...")
    elif choice == "8":
        print("Bisous!")
        exit(1)
    
    input("Press anything to continue...")

