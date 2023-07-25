class Employee:
    def __init__(self, id, full_name, address, age,
                 phone_number, salary, exp):
        self.mid_name = None
        self.first_name = None
        self.last_name = None
        self.id = id
        self.address = address
        self.age = age
        self.phone_number = phone_number
        self.salary = salary
        self.exp = exp
        self.set_full_name(full_name)
        self.full_name = self.last_name + " " + self.mid_name + self.first_name

    def set_full_name(self, full_name: str):
        words = full_name.split(" ")
        self.last_name = words[0]
        self.first_name = words[len(words) - 1]
        self.mid_name = ""
        for i in range(1, len(words) - 1):
            self.mid_name += words[i] + " "
