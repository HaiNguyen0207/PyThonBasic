from LearnPython.Chapter5.Lesson5_3.Exercise2.Person import Person


class Instruction(Person):
    def __init__(self, full_name, address, email, dob, id,
                 instruction_id, exp, salary, specialize):
        super().__init__(full_name, address, email, dob, id)
        self.instruction_id = instruction_id
        self.exp = exp
        self.salary = salary
        self.specialize = specialize

    def receive_salary(self):
        print(f"Giảng viên {self.full_name} "
              f"nhận lương là {self.salary} ")

    def marking(self):
        print(f"Giảng viên {self.full_name} đang chấm bài ....")

    def eat(self, food):
        super().eat(food)

    def sleep(self):
        super().sleep()

    def relax(self):
        super().relax()

    def do_work(self):
        super().do_work()
