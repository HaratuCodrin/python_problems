from ComplexNumber import ComplexNumber
from Repositories import *
from copy import deepcopy
import json
class NotPossible(Exception):
    pass

class Services:
    def __init__(self, liste, moves):
        f = open('settings_properties.json')
        data = json.load(f)
        if data["repo"] == "Memory":
            self.repo = Repository(liste)
        elif data["repo"] == "Text":
            self.repo = TextFileRepository(liste)
        elif data["repo"] == "Binary":
            self.repo = BinaryFileRepository(liste)

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