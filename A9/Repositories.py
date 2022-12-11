import os
import numpy as np
from ComplexNumber import ComplexNumber as complex
import pickle

class Repository:
    def __init__(self, liste):
        self.liste = liste
    
    def add_element(self, element):
        self.liste.append(element)
    
    def save_numbers(self):
        pass

class TextFileRepository(Repository):
    file_name = "numbers.txt"
    def __init__(self, liste):
        super().__init__(liste)
        if os.path.isfile(self.file_name):
            if os.path.getsize(self.file_name) > 0:
                self.load_numbers()
        self.save_numbers()

    def load_numbers(self):
        text = np.loadtxt(self.file_name)
        temp_list = text.tolist()
        self.liste.clear()
        for element in temp_list:
            self.liste.append(complex(element[0], element[1]))
        
    def save_numbers(self):
        temp_liste = []
        for complex_number in self.liste:
            temp_liste.append([complex_number.real, complex_number.im])
        np.savetxt(self.file_name, temp_liste)

class BinaryFileRepository(Repository):
    file_name = "pickle_numbers"
    def __init__(self, liste):
        super().__init__(liste)
        if os.path.isfile(self.file_name):
            if os.path.getsize(self.file_name) > 0:
                self.load_numbers()
        self.save_numbers()
        
    def load_numbers(self):
        file = open(self.file_name, "rb")
        self.liste = pickle.load(file)
        file.close()
    
    def save_numbers(self):
        file = open(self.file_name, "wb")
        pickle.dump(self.liste, file)
        file.close()
        

        

        





    
    
