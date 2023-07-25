from LearnPython.Chapter5.Lesson5_3.Exercise2.Student import Student


class StudentGraduate(Student):
    def __init__(self, full_name, address, email, dob, id,
                 student_id, gpa, major, year_graduate,
                 capacity, salary_current):
        super().__init__(full_name, address, email, dob, id,
                         student_id, gpa, major)
        self.year_graduate = year_graduate
        self.capacity = capacity
        self.salary_current = salary_current

    def go_to_work(self):
        print(f"{self.full_name} hiện đang làm IT...")

    def reveive_certificate(self):
        print(f"{self.full_name} đã nhận bằng tốt nghiệp ...")

    def do_exercise(self, subject):
        super().do_exercise(subject)

    def do_exam(self, subject):
        super().do_exam(subject)

    def pay_tuition(self):
        super().pay_tuition()

    def eat(self, food):
        super().eat(food)

    def sleep(self):
        super().sleep()

    def relax(self):
        super().relax()

    def do_work(self):
        super().do_work()
