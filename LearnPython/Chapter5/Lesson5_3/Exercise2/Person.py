class Person:
    def __init__(self, full_name, address, email, dob, id):
        self.full_name = full_name
        self.address = address
        self.email = email
        self.dob = dob
        self.id = id

    def eat(self, food):
        print(f"{self.full_name} đang ăn món {food}....")

    def sleep(self):
        print(f"{self.full_name} đang ngủ trưa ....")

    def relax(self):
        print(f"{self.full_name} đang giải trí ....")

    def do_work(self):
        print(f"{self.full_name} đang làm việc ....")
