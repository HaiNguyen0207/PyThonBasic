class Employee:
    def __init__(self, emp_id, full_name, email, number_phone, salary,
                 number_of_working_day):
        self.emp_id = emp_id
        self.full_name = full_name
        self.email = email
        self.number_phone = number_phone
        self.salary = salary
        self.number_of_working_day = number_of_working_day

    def check_in(self):
        print(f"{self.full_name} đang check in ....")

    def check_out(self):
        print(f"{self.full_name} đang check out....")

    def calculator_salary(self):
        return self.number_of_working_day * self.salary / 22

    def do_work(self, job):
        print(f"{self.full_name} đang làm việc {job}")
