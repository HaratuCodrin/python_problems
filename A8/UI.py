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
    "8) Establish the podium options.",
    "9) Undo last move.",
    "10) Exit program."
]

secondary_options = [
    "######## Pick another option ########",
    "1) Display all contestants in decreasing order of average score.",
    "2) Display all contestants with an average below n.",
    "3) Display all contestants with an average over n.",
    "4) Display all contestants with an average equal to n."
]

podium_options = [
    "######## Pick another option ########",
    "1) Display top n contestants.",
    "2) Display top n contestants for a certain problem score.",
    "3) Remove all contestants with an average over n.",
    "4) Remove all contestants with an average below n.",
    "5) Display all contestants with an average equal to n."
]

def menu_instance(list, queue):
    print()
    for option in options:
        print(option)

    choice = input("Choose an option:")
    choice = choice.strip()

    if choice == "1":
        display(list)
    elif choice == "2":
        pos = int(input("Enter position of the contestant x = ").strip())
        queue.append(copy.deepcopy(list))
        try:
            remove(list, pos)
        except IndexError:
            print("Participant doesn't exist, try again...")
    elif choice == "3":
        grade1 = int(input("Enter grade 1 of the new contestant:").strip())
        grade2 = int(input("Enter grade 2 of the new contestant:").strip())
        grade3 = int(input("Enter grade 3 of the new contestant:").strip())
        queue.append(copy.deepcopy(list))
        try:
            add_new_result(list, grade1, grade2, grade3)
        except NoSuch:
            print("Some of the grades are incorrect... Try again.")
    elif choice == "4":
        pos = int(input("Enter position of the contestant x =").strip())
        grade1 = int(input("Enter grade 1 of the new contestant:").strip())
        grade2 = int(input("Enter grade 2 of the new contestant:").strip())
        grade3 = int(input("Enter grade 3 of the new contestant:").strip())
        queue.append(copy.deepcopy(list))
        try:
            insert_result(list, pos, grade1, grade2, grade3)
        except IndexError:
            print("Participant doesn't exist, try again...")
        except NoSuch:
            print("Some of the grades are incorrect... Try again.")
    elif choice == "5":
        pos1 = int(input("Enter first position a = ").strip())
        pos2 = int(input("Enter first position b = ").strip())
        queue.append(copy.deepcopy(list))
        try:
            remove_from_a_to_b(list, pos1, pos2)
        except IndexError:
            print("Some participants don't exist, try again...")
    elif choice == "6":
        pos = int(input("Enter position of the contestant x = ").strip())
        problem = int(input("Enter the number of the problem = ").strip())
        grade = int(input("Enter the grade = "))
        queue.append(copy.deepcopy(list))
        try:
            replace_score(list, pos, problem, grade)
        except IndexError:
            print("Participant doesn't exist, try again...")
        except NoSuch:
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
            except NoSuch:
                print("No such participants...")
        elif secondary_choice == "3":
            n = int(input("Enter a value n = "))
            print("The contestants with average over", n, ":")
            try:
                display_over_n(list, n)
            except NoSuch:
                print("No such participants...")
        elif secondary_choice == "4":
            n = int(input("Enter a value n = "))
            print("The contestants with average equal to", n, ":")
            try:
                display_equal_n(list, n)
            except NoSuch:
                print("No such participants...")
    elif choice == "8":
        for option in podium_options:
            print(option)
        podium_choice = input("Your choice:").strip()

        if podium_choice == "1":
            n = int(input("Enter a value n = "))
            try:
                to_display = top_n(list, n)
                display(to_display)
            except(NoSuch):
                print("No such contestants.")
        elif podium_choice == "2":
            n = int(input("Enter a value n = "))
            problem = int(input("Enter a problem number p = "))
            try:
                to_display = top_n_for_problem(list, n, problem)
                display(to_display)
            except NoSuch:
                print("No such participants...")
        elif podium_choice == "3":
            n = int(input("Enter a value average = "))
            queue.append(copy.deepcopy(list))
            try:
                remove_more_than(list, n)
            except NoSuch:
                print("No such participants...")
        elif podium_choice == "4":
            n = int(input("Enter a value average = "))
            queue.append(copy.deepcopy(list))
            try:
                remove_less_than(list, n)
            except NoSuch:
                print("No such participants...")
        elif podium_choice == "5":
            n = int(input("Enter a value average = "))
            queue.append(copy.deepcopy(list))
            try:
                remove_equal_to(list, n)
            except NoSuch:
                print("No such participants...")
    elif choice == "9":
        if len(queue) != 0:
            undo(list, queue)
            queue.pop()
        else:
            print("No jobs to undo.") 
    elif choice == "10":
        print("Bisous!")
        exit(1)
    
    input("Press anything to continue...")

