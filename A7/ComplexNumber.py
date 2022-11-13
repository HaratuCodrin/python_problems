from math import sqrt as racine

# list implementation
# [(1,2), (2 ,-3)]

# dictionary implementation
dict = {
    1:2,
    3:5,
}


#class implementation 
class ComplexNumber:

    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __str__(self):
        if self.im < 0 and abs(self.im) != 1:
            return f"{self.real} - {abs(self.im)}i"
        elif self.im < 0 and abs(self.im) == 1:
            return f"{self.real} - i"
        elif self.im == 0:
            return f"{self.real}"
        elif self.im > 0 and abs(self.im) == 1:
            return f"{self.real} + i"
        else:
            return f"{self.real} + {self.im}i"

    def modulus(self):
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

    

    



