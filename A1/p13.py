# Determine the n-th element of the sequence 
# 1, 2, 3, 2, 5, 2, 3, 7, 2, 3, 2, 5, ...
# obtained from the sequence of natural numbers by replacing composed
# numbers with their prime divisors. 

from p3 import bubbleSort

def get_prime_divisors(number):
    i = 2
    divisors = []
    while i <= number:
        if (number % i != 0):
            i += 1
        else:
            number //= i
            if i not in divisors:
                divisors.append(i)

    if number > 1:
        divisors.append(number)
    return divisors

def compute_nth_element(n):
    # computing the sequence until we get to the n-th element
    sequence = [1]
    i = 1
    while len(sequence) <= n:
        i += 1
        divisors = get_prime_divisors(i)
        for divisor in divisors:
            sequence.append(divisor)
    
    return sequence, sequence[n-1]
        
    

if __name__ == "__main__":
    print(compute_nth_element(23)) 

    
    


