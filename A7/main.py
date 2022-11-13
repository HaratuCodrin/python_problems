from numpy import Infinity
from ComplexNumber import *

def read_number():
    print("Enter a complex number:")
    real = int(input("Real part = "))
    im = int(input("Imaginary part = "))
    return ComplexNumber(real, im)

def increasing_modulus_sequence(complex_numbers):
    sequences = [] # tous les sequences 
    sequence = [] # temporaire
    lowest_modulus = -1
    for complex_number in complex_numbers:
        current_modulus = complex_number.modulus()
        if current_modulus > lowest_modulus:
            sequence.append(complex_number)
        else:
            sequences.append(sequence)
            sequence.clear()
            sequence.append(complex_number)
        lowest_modulus = current_modulus
    
    longueur = 0
    sequence = []
    for seq in sequences:
        if len(seq) > longueur:
            longueur = len(seq)
            sequence = seq
    
    return longueur, sequence

def alternating_real_sequence(complex_numbers):
    sequences = [] # tous les sequences 
    sequence = [] # temporaire
    
    for complex_number in complex_numbers:
        current_real = complex_number.real
        if current_real > last_real:
            sequence.append(complex_number)
        else:
            sequences.append(sequence)
            sequence.clear()
            sequence.append(complex_number)
        lowest_modulus = current_modulus
            
if __name__ == "__main__":
    
    complex_numbers = []
    complex_numbers.append(ComplexNumber(2, -1))
    complex_numbers.append(ComplexNumber(-5, 3))
    complex_numbers.append(ComplexNumber(1, 1))
    complex_numbers.append(ComplexNumber(-7, 2))
    complex_numbers.append(ComplexNumber(-3, 13))
    complex_numbers.append(ComplexNumber(4, 4))
    complex_numbers.append(ComplexNumber(-1, -1))
    complex_numbers.append(ComplexNumber(6, -5))
    complex_numbers.append(ComplexNumber(-3, -10))
    complex_numbers.append(ComplexNumber(10, -10))

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
            new_number = read_number()
            complex_numbers.append(new_number)
        elif choice == "2":
            if len(complex_numbers) == 0:
                print("The list is empty!")
            else:
                for complex_number in complex_numbers:
                    print(complex_number)
        elif choice == "3":
            complex_numbers.clear()
        elif choice == "4":
            longueur, sequence = increasing_modulus_sequence(complex_numbers)
            print(longueur)
            for complex_number in sequence:
                print(complex_number)
        elif choice == "5":
            pass
        elif choice == "6":
            print("Have a nice day!")
            exit(1)
        
        input("Press any key to continue...")
