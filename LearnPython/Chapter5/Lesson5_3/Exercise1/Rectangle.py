from LearnPython.Chapter5.Lesson5_3.Exercise1.Figure2D import Figure2D


class Rectangle(Figure2D):
    def __init__(self, point_x, point_y, length, width):
        super().__init__(point_x, point_y)
        self.length = length
        self.width = width

    def perimeter_ractangle(self):
        return (self.length + self.width) * 2

    def area_ractangle(self):
        return self.length * self.width
