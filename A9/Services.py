from ComplexNumber import ComplexNumber
from Repositories import *
from copy import deepcopy
class NotPossible(Exception):
    pass

class Services:
    def __init__(self, liste, moves):
        self.repo = TextFileRepository(liste) # here you change the repository type
        self.moves = moves

    def add_number(self, a, b):
        self.moves.append(deepcopy(self.repo.liste))
        self.repo.add_element(ComplexNumber(a,b))
    
    def display_liste(self):
        for complex_number in self.repo.liste:
            print(complex_number)
    
    def filter_liste(self, start, end):
        self.moves.append(deepcopy(self.repo.liste))
        temp_liste = []
        if start < 0 or start > len(self.repo.liste) or end < 0 or end > len(self.repo.liste):
            raise NotPossible
        
        if start > end:
            temp = start
            start = end
            end = start

        for i in range(0, len(self.repo.liste)):
            if i >= start and i <= end:
                temp_liste.append(self.repo.liste[i])
        self.change_list(temp_liste)
    
    def change_list(self, new_list):
        self.repo.liste.clear()
        for element in new_list:
            self.repo.add_element(element)
        
    def undo(self):
        if len(self.moves) == 0:
            print("No moves to undo.")
        else:
            self.change_list(self.moves.pop())

    def save(self):
        self.repo.save_numbers()