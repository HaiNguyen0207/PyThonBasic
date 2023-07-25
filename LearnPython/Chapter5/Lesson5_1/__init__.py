class Student:
    """lớp mô ta sinh viên"""

    def __init__(self, student_id, name, address, age):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.age = age

    def do_exam(self, subject):
        print(f"{self.name} đang làm bài {subject}")

    def relax(self):
        print(f"{self.name} đang giải trí ")

    def do_home_work(self, subject):
        print(f"{self.name} đang lam bài tập về nhà môn {subject} ")


hai = Student("AT170415", "Nguyễn Văn Hải", "Hà Nội", 20)
hai.relax()
hai.do_exam("Toán")
print(hai)
