import math

from LearnPython.Chapter5.Lesson5_3.Exercise1.Figure2D import Figure2D


class Circle(Figure2D):
    def __init__(self, point_x, point_y, radium):
        super().__init__(point_x, point_y)
        self.radium = radium

    # tính chu vi
    def perimeter_circle(self):
        return 2 * self.radium * math.pi

    # tính diện tích
    def area_circle(self):
        return math.pi * self.radium * self.radium
