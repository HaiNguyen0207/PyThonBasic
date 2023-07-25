from LearnPython.Chapter5.Lesson5_4.Exercise4.Employee import Employee


class Programmer(Employee):
    def __init__(self, emp_id, full_name, email, number_phone, salary,
                 number_of_working_day, specialize, number_language,
                 number_project, kpi):
        super(Programmer, self).__init__(emp_id, full_name, email, number_phone,
                                         salary, number_of_working_day)
        self.specialize = specialize
        self.number_language = number_language
        self.number_project = number_project
        self.kpi = kpi

    def give_task(self, job):
        print(f"Lập trình viên {self.full_name} đã nhận công việc {job}")

    def code(self):
        print(f"Lập trình viên {self.full_name} đang code ....")

    def fix_bug(self):
        print(f"Lập trình viên {self.full_name} đang fix lỗi ....")

    def report_job(self):
        print(f"Lập trình viên {self.full_name} báo cáo công viêc ....")

    def calculator_salary(self):
        return self.salary + 0.3*(super().calculator_salary() * self.kpi) / 100
