
from LearnPython.Chapter5.Lesson5_3.Exercise1.Circle import Circle
from LearnPython.Chapter5.Lesson5_3.Exercise1.Figure2D import Figure2D
from LearnPython.Chapter5.Lesson5_3.Exercise1.Rectangle import Rectangle
from LearnPython.Chapter5.Lesson5_3.Exercise1.Triangle import Triangle

figure_2d = Figure2D(50, 100)
figure_2d.show_infor()
print("===========================")
circle = Circle(50, 100, 30)
print(f"Chu vi hình tròn là : {circle.perimeter_circle()}")
print(f"Diện tích hình tròn là : {circle.area_circle()}")
print("==========================")
rectangle = Rectangle(50, 100, 30, 40)
print(f"Chu vi hình chữ nhật là : {rectangle.perimeter_ractangle()}")
print(f"Diện tích hình chữ nhật là : {rectangle.area_ractangle()}")
print("=========================")
triangle = Triangle(50, 100, 30, 40, 50)
print(f"Chu vi hình tam giác là : {triangle.primeter_triangle()}")
print(f"Diện tích hình tam giác là : {triangle.area_triangle()}")
