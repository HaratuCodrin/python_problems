# python_problems
Assignment 1 is done, if you have any questions I could comment the code more or I can explain it to you. 
Problem 13, I am not sure if it is the greatest answer but it works fine. 

Explanation:

############ A1 ############

p3: # For a given natural number n find the minimal natural number m formed with the same digits.
    We first put all the number's n digits into an array, 
    then we sort the array with an algorithm of choice, 
    then we recompute the number with the new array of digits.
    That will be the minimal configuration.

p11: # The numbers n1 and n2 have the property P if their writing in base 10 uses the same digits
       Determine whether two given natural numbers have property P
     We first take the numbers different digits and put them in 2 arrays, digits1 and digits2,
     then the arrays are sorted with the algorithm of choice.
     Now, to check if the numbers contain the same digits, the two resulting arrays have to be identical.
     So we compare the arrays digits1 and digits2:
        if they are identical, n1 and n2 have the property P,
        else, n1 and n2 don't have the property P

p13: # Determine the n-th element of the sequence 1, 2, 3, 2, 5, 2, 3, 7, 2, 3, 2, 5, ...
     obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors.
     We compute the sequence until we get to the n-th element.

########### A2 #############

Menu implemented, with different options. Used "random" package for generating the list.
 
    
