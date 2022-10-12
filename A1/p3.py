#  For a given natural number n find the minimal
#  natural number m formed with the same digits.

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

def get_sorted_digits(number):
    n = number 
    digits = []
    while n != 0:
        digits.append(n % 10)
        n = int(n / 10)
    bubbleSort(digits)
    return digits

def find_minimal_configuration(number):
    n = number
    # we create an array to store the digits of the number,
    # and then we sort them with a sorting alg
    array = get_sorted_digits(n)
    # we compute the final number with the sorted digits 
    # example: 147 = 1 * 100 + 4 * 10 + 7 * 1
    n = 0
    power = len(array) - 1
    for element in array:
        n = n + element * (10 ** power)
        power = power - 1
    return n
        
    
if __name__ == "__main__":

    numbers = [3658, 4167, 1895, 87, 193453]
    for number in numbers:
        print(number, find_minimal_configuration(number))
    



    
    