
from Functions import * 

def test_average():
    assert average({"P1":10, "P2": 10, "P3":10}) == 10, "Should be 10"

def test_add_new_result(list):
    n = len(list)
    add_new_result(list, 1, 2, 3)
    assert list[n] == {"P1" : 1, "P2" : 2, "P3" : 3}, "The added member should be at the end."

def test_insert_result(list, pos, p1, p2, p3):
    insert_result(list, pos, p1, p2, p3)
    assert list[pos] == {"P1" : p1, "P2" : p2, "P3" : p3} , "The values passed should correspond."

def test_remove(list, pos):
    remove(list, pos)
    assert list[pos] == {"P1" : 0, "P2" : 0, "P3" : 0}, "The grades at the position have to be 0."

def test_remove_a_to_b(list, a, b):
    remove_from_a_to_b(list, a, b)
    for position in range(a, b+1):
        assert list[position] == {"P1" : 0, "P2" : 0, "P3" : 0}, "All grades have to be 0."


def test_replace_score(list, pos, problem, grade):
    replace_score(list, pos, problem, grade)
    prob = "P"+str(problem)
    assert list[pos][prob] == grade, "The new grade has to be the one we gave."

if __name__ == "__main__":
    test_list = [
        {"P1":0, "P2":5, "P3":5},
        {"P1":4, "P2":6, "P3":10},
        {"P1":6, "P2":8, "P3":9},
        {"P1":4, "P2":10, "P3":5}
    ]

    test_average()
    test_add_new_result(test_list)
    test_insert_result(test_list, 0, 3, 4, 5)
    test_insert_result(test_list, 0, 1, 4, 5)
    test_remove(test_list, 2)
    test_remove_a_to_b(test_list, 0, 1)
    test_replace_score(test_list, 1, 1, 10)


    print("Everything passed.")





