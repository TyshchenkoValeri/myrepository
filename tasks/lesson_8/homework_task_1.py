class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# пример
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

print(c1 + c2)    # Вывод: 4 + 9i
print(c1 - c2)    # Вывод: 2 - 5i
print(c1 == c2)   # Вывод: False
print(c1 == ComplexNumber(3, 2))   # Вывод: True
