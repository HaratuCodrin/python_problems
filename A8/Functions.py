# all functions take a list of dictionaries as parameters
import copy

class NoSuch(Exception):
    pass


def average(participant):
    average = 0
    for grade in participant:
        average += participant[grade]
    
    average = average / 3
    return average

def add_new_result(list, P1, P2, P3):
    if P1 > 10 or P2 > 10 or P3 > 10:
        raise NoSuch
    if P1 < 0 or P2 < 0 or P3 < 0:
        raise NoSuch
    list.append({"P1" : P1, "P2" : P2, "P3" : P3})

def insert_result(list, position, P1, P2, P3):
    n = len(list)
    if position > n - 1:
        raise IndexError
    if P1 > 10 or P2 > 10 or P3 > 10:
        raise NoSuch
    if P1 < 0 or P2 < 0 or P3 < 0:
        raise NoSuch
    list[position] = {"P1" : P1, "P2" : P2, "P3" : P3}

def remove(list, position):
    n = len(list)
    if position > n - 1:
        raise IndexError
    for grade in list[position]:
        list[position][grade] = 0

def remove_from_a_to_b(list, a, b):
    n = len(list)
    if a > n - 1 or b > n-1:
        raise IndexError
    if a >= b:
        temp = a
        a = b
        b = temp

    for i in range(a,b+1):
        for grade in list[i]:
            list[i][grade] = 0

def replace_score(list, position, problem, grade):
    n = len(list)
    if position > n - 1:
        raise IndexError
    if problem > 3 or problem < 1:
        raise NoSuch
    
    if grade > 10:
        raise NoSuch
    if grade < 0:
        raise NoSuch

    prob = "P"+str(problem)   # creer un string "P1", "P2" ou "P3"
    list[position][prob] = grade
    

def display(list):
    i = 0
    for element in list:
        print(i, element)
        i += 1

def display_below_n(list, n):
    new_list = []

    for participant in list:
        avg = average(participant)
        if avg < n:
            new_list.append(participant)
    
    if len(new_list) == 0:
        raise NoSuch

    display(new_list)


def display_over_n(list, n):
    new_list = []
    for participant in list:
        avg = average(participant)
        if avg > n:
            new_list.append(participant)
    
    if len(new_list) == 0:
        raise NoSuch

    display(new_list)

def display_equal_n(list, n):
    new_list = []
    for participant in list:
        avg = average(participant)
        if avg == n:
            new_list.append(participant)
    
    if len(new_list) == 0:
        raise NoSuch

    display(new_list)


def display_sorted(list):
    # bubble sort with averages 
    n = len(list)
    new_list = copy.deepcopy(list)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if average(new_list[j]) < average(new_list[j+1]):
                swapped = True
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
        if not swapped:
            break
    
    display(new_list)


            
    





