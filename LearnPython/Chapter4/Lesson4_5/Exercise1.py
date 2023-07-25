"""
Bài Lesson8_1. Thông tin điểm sinh viên được mô tả dạng <mã sinh viên> <điểm trung bình>. Trong đó
mã sinh viên gồm cả chữ và số, điểm trung bình là số thực làm tròn đến 2 chữ số sau dấu phẩy.
Cho danh sách các bộ dữ liệu đầu vào và mã sinh viên nào đó, hãy cho biết điểm trung bình của
sinh viên có mã đã cho.
"""
test = int(input())


def show_gpa(ids, dict_students):
    for e in ids:
        print(f"{dict_students.get(e)}", end=" ")


for i in range(test):
    amount = int(input())
    dict_students = dict()
    for e in range(amount):
        data = [x for x in input().split()]
        dict_students[data[0]] = data[1]
    ids = [x for x in input().split()]
    show_gpa(ids, dict_students)
