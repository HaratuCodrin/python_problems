## Unit tests
from Services import *
from ComplexNumber import ComplexNumber
from collections import deque

def test_add_element(service):
    n = len(service.repo.liste)
    service.add_number(1, 2)
    assert service.repo.liste[n].real == 1
    assert service.repo.liste[n].im == 2

if __name__ == "__main__":
    test_list = [
        ComplexNumber(1,1),
        ComplexNumber(0,3)
    ]
    moves = deque()
    
    service = Services(test_list, moves)

    test_add_element(service)
    
    print("All tests passed.")
