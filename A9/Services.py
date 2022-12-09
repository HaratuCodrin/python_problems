from ComplexNumber import ComplexNumber
from Repository import Repository

class Services:
    def __init__(self, liste, moves):
        self.repo = Repository(liste)
        self.moves = moves
    
    def save_text(self):
        pass

    def save_binary(self):
        pass

    def add_number(self, a, b):
        self.repo.liste.append(ComplexNumber(a,b))
    
    def display_liste(self):
        for complex_number in self.repo.liste:
            print(complex_number)