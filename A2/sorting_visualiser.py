# Menu-driven console application to help 
# visualize the way sorting algorithms work.

import random
from turtle import clear

def permutation_sort(array):
    pass

def strand_sort(array):
    pass

def generate_random_numbers(n):
    list = []
    for i in range(0, n):
        n = random.randint(0,100)
        list.append(n)
    return list

if __name__ == "__main__":
    ## console menu
    array = []
    while True:
        print("##### Sorting Visualizer ####")
        print("1) Generate a new list of random numbers from 0 to 100")
        print("2) Display the list")
        print("3) Visualize Strand Sort")
        print("4) Visualize Permutation Sort")
        print("5) Quit")

        choice = input("Enter Choice: ")
        choice = choice.strip()

        if choice == "1":
            n = int(input("Enter a number of elements: "))
            array = generate_random_numbers(n)
        elif choice == "2":
            if len(array) > 0:
                print("The list: ")
                print(array)
            else:
                print("The array is not generated yet.")
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            exit(1)
        
        
            
