import math

from LearnPython.Chapter5.Lesson5_3.Exercise1.Figure2D import Figure2D


class Triangle(Figure2D):
    def __init__(self, point_x, point_y, len_a, len_b, len_c):
        super().__init__(point_x, point_y)
        self.len_a = len_a
        self.len_b = len_b
        self.len_c = len_c

    def check_is_triangle(self):
        if self.len_a + self.len_b > self.len_c and \
                self.len_a + self.len_c > self.len_b and \
                self.len_b + self.len_c > self.len_a:
            return True
        return False

    def primeter_triangle(self):
        if (self.check_is_triangle()):
            return self.len_c + self.len_b + self.len_a
        else:
            return None

    def area_triangle(self):
        if (self.check_is_triangle()):
            p = (self.len_a + self.len_b + self.len_c) / 2
            value = math.pow((p - self.len_c), 2) + \
                    math.pow((p - self.len_b), 2) + \
                    math.pow((p - self.len_a), 2)
            return math.sqrt(value)
