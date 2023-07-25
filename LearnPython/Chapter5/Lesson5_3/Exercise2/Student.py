from LearnPython.Chapter5.Lesson5_3.Exercise2.Person import Person


class Student(Person):
    def __init__(self, full_name, address, email, dob, id,
                 student_id, gpa, major):
        super().__init__(full_name, address, email, dob, id)
        self.student_id = student_id
        self.gpa = gpa
        self.major = major

    def do_exercise(self, subject):
        print(f"{self.full_name} đang làm bài môn {subject}s")

    def do_exam(self, subject):
        print(f"{self.full_name} đang làm kiểm tra môn {subject}")

    def pay_tuition(self):
        print(f"{self.full_name} đã nộp học phí ....")

    def eat(self, food):
        super().eat(food)

    def sleep(self):
        super().sleep()

    def relax(self):
        super().relax()

    def do_work(self):
        super().do_work()
