# The numbers n1 and n2 have the property P 
# if their writing in base 10 uses the same digits

# Determine whether two given natural numbers have property P

from p3 import bubbleSort

def get_different_digits(number):
    n = number 
    digits = []
    while n != 0:
        current_digit = n % 10 # on prend la derniere chiffre

        if current_digit not in digits:
            digits.append(current_digit)

        n = int(n / 10)
        
    bubbleSort(digits)
    return digits

def property_P(n1, n2):

    digits_1 = get_different_digits(n1)
    digits_2 = get_different_digits(n2)

    if len(digits_1) == len(digits_2):
        for i in range(0, len(digits_1) - 1):
            if digits_1[i] != digits_2[i]:
                return False
    else:
        return False
    
    return True
            
if __name__ == "__main__":
    n1 = 33214
    n2 = 31223
    print(property_P(n1, n2))

    pass

