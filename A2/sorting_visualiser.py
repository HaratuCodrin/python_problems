# Menu-driven console application to help 
# visualize the way sorting algorithms work.

import random
from time import sleep as dormir
from strand_sort import *

# function to check if an array is sorted
def is_sorted(array):
    n = len(array)
    for i in range(0, n-1):
        if (array[i] > array[i+1] ):
            return False
    return True

# function tu shuffle the array for the permutation sort 
def shuffle(array):
    n = len(array)
    for i in range(0,n):
        r = random.randint(0,n-1)
        array[i], array[r] = array[r], array[i]

def permutation_sort(array, step):
    n = len(array)
    i = 0
    phase = 0
    while not is_sorted(array):
        shuffle(array)
        i += 1
        if i == step:
            i = 0
            phase += 1
            print("State ", phase)
            print(array)
            dormir(2)
    
    print("Array is sorted!")
    print(array)

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
        print("3) Visualize Permutation Sort")
        print("4) Visualize Strand Sort")
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
            step = int(input("Enter a viewing frequence (step):"))
            permutation_sort(array, step)
        elif choice == "4":
            step = int(input("Enter a viewing frequence (step): "))
            array = strand_sort(array, step)
        elif choice == "5":
            print("Have a nice day!")
            exit(1)
        
        input("Press any key to continue...")
        
        
            
