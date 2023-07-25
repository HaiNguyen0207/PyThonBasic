from LearnPython.Chapter5.Lesson5_3. \
    Exercise2.Student import Student


class StudentUnGraduate(Student):
    def __init__(self, full_name, address, email, dob, id,
                 student_id, gpa, major, year_learn_again,
                 number_subject_failed):
        super().__init__(full_name, address, email, dob, id,
                         student_id, gpa, major)
        self.year_learn_again = year_learn_again
        self.number_subject_failed = number_subject_failed

    def learn_again(self, subject):
        print(f"{self.full_name}  học lại {subject}")

    def register_subject(self, subject):
        print(f"{self.full_name} đăng kí học lại môn {subject}")

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


