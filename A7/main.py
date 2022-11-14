from numpy import Infinity
from math import sqrt as racine
import copy

def read_number():
    print("Enter a complex number:")
    real = int(input("Real part = "))
    im = int(input("Imaginary part = "))
    return real, im

def print_list(list):
    for i in range(0, len(list[0])):
        print(str(list[0][i]) + " + (" + str(list[1][i]) + ")i")

def print_dict(dict):
    for im in dict.keys():
        print(str(im) + " + (" + str(dict[im]) + ")i")
        

def increasing_modulus_list(list):
    sequences = [] # tous les sequences 
    sequence = [[], []] # temporaire
    lowest_modulus = -1
    for i in range(0, len(list[0])):
        a = list[0][i]
        b = list[1][i]
        current_modulus = racine(a**2 + b**2)
        if current_modulus > lowest_modulus:
            sequence[0].append(a)
            sequence[1].append(b)
        else:
            sequences.append(copy.deepcopy(sequence))
            sequence[0].clear()
            sequence[1].clear()
            sequence[0].append(a)
            sequence[1].append(b)
        lowest_modulus = current_modulus
    
    longueur = 0
    sequence = [[], []]
    for seq in sequences:
        if len(seq[0]) > longueur:
            longueur = len(seq[0])
            sequence = seq
    
    return longueur, sequence

def increasing_modulus_dict(dict):
    sequences = [] # tous les sequences 
    sequence = {} # temporaire
    lowest_modulus = -1
    for im in dict.keys():
        a = im
        b = dict[im]
        current_modulus = racine(a**2 + b**2)
        if current_modulus > lowest_modulus:
            sequence.update({a:b})
        else:
            sequences.append(copy.deepcopy(sequence))
            sequence.clear()
            sequence.update({a:b})
        lowest_modulus = current_modulus
    
    longueur = 0
    sequence = {}
    for seq in sequences:
        if len(seq) > longueur:
            longueur = len(seq)
            sequence = seq
    
    return longueur, sequence

def alternating_real_sequence(complex_numbers):
    if len(complex_numbers) == 0:
        return
    sequences = [] # tous les sequences 
    sequence = [] # temporaire
    last_real = -1
    up = False
    for complex_number in complex_numbers:
        current_real = complex_number.real
        if len(sequence) == 0:
            sequence.append(complex_number)
        elif len(sequence) == 1:
            if last_real != current_real:
                sequence.append(complex_number)
                if current_real > last_real:
                    up = True
                else:
                    up = False
        else:
            if up:
                if (len(sequence) + 1) % 2 == 1:
                    if current_real < last_real:
                        sequence.append(complex_number)
                    else:
                        sequences.append(sequence)
                        sequence = []
                        sequence.append(complex_number)
                else:
                      if current_real > last_real:
                        sequence.append(complex_number)
                      else:
                        sequences.append(sequence)
                        sequence = []
                        sequence.append(complex_number)
            else:
                if (len(sequence) + 1) % 2 == 1:
                    if current_real > last_real:
                        sequence.append(complex_number)
                    else:
                        sequences.append(sequence)
                        sequence = []
                        sequence.append(complex_number)
                else:
                      if current_real < last_real:
                        sequence.append(complex_number)
                      else:
                        sequences.append(sequence)
                        sequence = []
                        sequence.append(complex_number)

            last_real = current_real
        
    longueur = 0
    sequence = []
    for seq in sequences:
        if len(seq) > longueur:
            longueur = len(seq)
            sequence = seq

    return longueur, sequence

            
if __name__ == "__main__":

    choix = input("What data type are we using?\n 1) List\n 2) Dictionary\n")
    choix = choix.strip()
    complex_data = None
    if choix == "1":
        complex_data = [[1, 2, -3, 4, -5, -6, 0, 11, 23, 10],
                        [1, 2, -3, 4, 5, 6, 60, 7, 9, 10]]  
    else:
        complex_data = {
            3:-3, 1:1, -2:-1, 3:12, 4:2, -5:-2, 0:60, 11:7, 23:9, 10:10
        }

    while True:
        print("##### Complex Numbers ####")
        print("1) Add a new complex number to the list.")
        print("2) Display the complex numbers list")
        print("3) Clear the list.")
        print("4) Task A")
        print("5) Task B")
        print("6) Quit")

        choice = input("Enter Choice: ")
        choice = choice.strip() # pour ignorer les espaces

        if choice == "1":
            real, im = read_number()
            if choix == "1":
                complex_data[0].append(real)
                complex_data[1].append(im)
            else:
                complex_data.update({real:im})
        elif choice == "2":
            if len(complex_data) == 0:
                print("The structure is empty!")
            else:
                if choix == "1":
                    print_list(complex_data)
                else:
                    print_dict(complex_data)
        elif choice == "3":
            complex_data.clear()
        elif choice == "4":
            if len(complex_data) == 0:
                print("The structure is empty!")
            else:
                if choix == "1":
                    longueur, sequence = increasing_modulus_list(complex_data)
                    print(longueur)
                    print_list(sequence)
                else:
                    longueur, sequence = increasing_modulus_dict(complex_data)
                    print(longueur)
                    print_dict(sequence)
        elif choice == "5":
            pass
        elif choice == "6":
            print("Have a nice day!")
            exit(1)
        
        input("Press any key to continue...")
