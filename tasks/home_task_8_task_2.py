import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, apex_1, apex_2, apex_3):
        self.apex_1 = apex_1
        self.apex_2 = apex_2
        self.apex_3 = apex_3

    def area(self):
        if (self.apex_1.x == self.apex_2.x and self.apex_2.x == self.apex_3.x) or \
                (self.apex_1.y == self.apex_2.y and self.apex_2.y == self.apex_3.y):
            print("Error: a triangle cannot be degenerate")
            return 0

        # Вычисление площади по формуле Герона
        side_1 = ((self.apex_1.x - self.apex_2.x) ** 2 + (self.apex_1.y - self.apex_2.y) ** 2) ** 0.5
        side_2 = ((self.apex_2.x - self.apex_3.x) ** 2 + (self.apex_2.y - self.apex_3.y) ** 2) ** 0.5
        side_3 = ((self.apex_3.x - self.apex_1.x) ** 2 + (self.apex_3.y - self.apex_1.y) ** 2) ** 0.5
        semipermeter = (side_1 + side_2 + side_3) / 2
        return (semipermeter * (semipermeter - side_1) * (semipermeter - side_2) * (semipermeter - side_3)) ** 0.5


class Square:
    def __init__(self, apex_1, apex_2, apex_3, apex_4):
        self.apex_1 = apex_1
        self.apex_2 = apex_2
        self.apex_3 = apex_3
        self.apex_4 = apex_4

    def area(self):
        if (self.apex_1.x == self.apex_2.x and self.apex_2.x == self.apex_3.x and self.apex_3.x == self.apex_4.x) or \
                (self.apex_1.y == self.apex_2.y and self.apex_2.y == self.apex_3.y and self.apex_3.y == self.apex_4.y):
            print("Error: a square cannot be degenerate")
            return 0

        # Вычисление площади по формуле S = a^2
        # Вычисляем длину стороны квадрата с помощью теоремы Пифагора: корень из (x2 - x1)^2 + (y2 - y1)^2
        side_1 = ((self.apex_1.x - self.apex_2.x) ** 2 + (self.apex_1.y - self.apex_2.y) ** 2) ** 0.5
        side_2 = ((self.apex_2.x - self.apex_3.x) ** 2 + (self.apex_2.y - self.apex_3.y) ** 2) ** 0.5
        side_3 = ((self.apex_3.x - self.apex_4.x) ** 2 + (self.apex_3.y - self.apex_4.y) ** 2) ** 0.5
        side_4 = ((self.apex_4.x - self.apex_1.x) ** 2 + (self.apex_4.y - self.apex_1.y) ** 2) ** 0.5
        if side_1 == side_2 == side_3 == side_4:
            return side_1 ** 2
        else:
            print("Error: it's not a square")
            return 0
