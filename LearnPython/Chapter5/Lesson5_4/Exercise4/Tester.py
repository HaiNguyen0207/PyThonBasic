from LearnPython.Chapter5.Lesson5_4.Exercise4.Employee import Employee


class Tester(Employee):
    def __init__(self, emp_id, full_name, email, number_phone, salary,
                 number_of_working_day,
                 specialize, tool, number_detect_error, number_test_complete):
        super(Tester, self).__init__(emp_id, full_name, email, number_phone,
                                     salary, number_of_working_day)
        self.specialize = specialize
        self.tool = tool
        self.number_detect_error = number_detect_error
        self.number_test_complete = number_test_complete

    def give_project(self):
        print(f"Tester{self.full_name} đang nhận dự án ....")

    def calculator_salary(self):
        return self.salary + 0.2 * super().calculator_salary() * \
               self.number_test_complete / 100 + 50000 * self.number_detect_error
