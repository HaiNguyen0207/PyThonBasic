from LearnPython.Chapter5.Lesson5_4.Exercise4.Employee import Employee


class Manager(Employee):
    def __init__(self, emp_id, full_name, email, number_phone, salary,
                 number_of_working_day, role, term, total_salary):
        super(Manager, self).__init__(emp_id, full_name, email,
                                      number_phone, salary,
                                      number_of_working_day)
        self.role = role
        self.term = term
        self.total_salary = total_salary

    def meeting(self):
        print(f"Giám đốc {self.full_name} đang đi gặp đối tác ...")

    def signing(self):
        print(f"Giám đốc {self.full_name} đang kí duyệt tài liệu")

    def calculator_salary(self):
        return super().calculator_salary() + 0.8 * self.total_salary
