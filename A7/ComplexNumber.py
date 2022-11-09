from math import sqrt as racine

class ComplexNumber:

    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __str__(self):
        return f"{self.real} + {self.im}i"

    def module(self):
        return racine(self.real**2 + self.im**2) 

    def add(n1, n2):
        real = n1.real + n2.real
        im = n1.im + n2.im
        return ComplexNumber(real, im)

    def substract(n1, n2):
        real = n1.real - n2.real
        im = n1.im - n2.im
        return ComplexNumber(real, im)
    
    def multiply(n1, n2):
        real = n1.real * n2.real  - n1.im * n2.im
        im = n1.real * n2.im + n1.im * n2.real
        return ComplexNumber(real, im)

    

    



