""""
thông tin sinh viên gồm mã sinh viên ,họ ,tên ,đệm, chuyên ngành
điểm trunh bình. hãy tạo Lesson8_1 danh sách sinh viên
sau đó sắp xếp danh sách sinh viên điểm giảm dần
"""


class Student:
    def __init__(self, id, full_name, major, gpa):

        self.id = id
        self.set_full_name(full_name)
        self.major = major
        self.gpa = gpa
        self.full_name = self.last_name + " " + self.mid_name + self.first_name

    def set_full_name(self, full_name):
        words = full_name.split()
        self.first_name = words[len(words) - 1]
        self.last_name = words[0]
        self.mid_name = ''
        for i in range(1, len(words) - 1):
            self.mid_name += words[i] + " "

    def show_student(self):
        print(f"{self.id} - {self.full_name} - {self.major} - {self.gpa}")


def create_new_student() -> Student:
    id = (input("Enter student Id : "))
    full_name = (input("Enter full name : "))
    major = (input("Enter major : "))
    gpa = float((input("Enter gpa : ")))
    return Student(id, full_name, major, gpa)


students = []
n = int(input())
for i in range(n):
    student = create_new_student()
    students.append(student)
students.sort(key=lambda x: x.gpa, reverse=True)
for i in students:
    i.show_student()
