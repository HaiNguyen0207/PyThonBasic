from LearnPython.Chapter5.Lesson5_2.Exercise2.employee import Employee


def add_new_emp() -> Employee:
    id = input("Nhập mã nhân viên : ")
    full_name = input("Nhập họ tên : ")
    address = input("Nhập địa chỉ : ")
    age = int(input("Nhập tuổi : "))
    phone_number = input("Nhập số điện thoại : ")
    salary = int(input("Nhâp mức lương :  "))
    exp = int(input("Nhập năm kinh nghiệm : "))
    return Employee(id, full_name, address, age, phone_number,
                    salary, exp)


def show_title():
    print(f'{"Mã NV":10}{"Họ Tên":20}'
          f'{"Địa chỉ":12}{"Tuổi":<6}{"SĐT":15}{"K.N":<10}{"Lương":<12}')


def show_emp_infor(e):
    print(f"{e.id:10}{e.full_name:20}{e.address:12} "
          f"{e.age:<6}{e.phone_number:15}{e.exp:<10}{e.salary:<12}")


def show_emp(employees):
    show_title()
    for e in employees:
        show_emp_infor(e)


def find_emp(employees, id):
    for i in range(len(employees)):
        if employees[i].id.lower() == id.lower():
            return i
    return -1


def find_emp_by_id(employees):
    id = input("Nhập mã nhân viên cần tìm kiếm : ")
    index = find_emp(employees, id)
    if index != -1:
        print("===> Thông tin tìm kiếm trả về <===")
        show_title()
        show_emp_infor(employees[index])
    else:
        print("===> Thông tin tìm kiếm không hợp lệ <===")


def remove_emp_by_id(employees):
    id = input("Nhập mã nhân viên cần xóa : ")
    index = find_emp(employees, id)
    if index != -1:
        employees.pop(index)
        print("===> Xóa thành công <====")
    else:
        print("===> Thông tin xóa không hợp lệ <===")


def sort_emp_by_salary_desc(employees):
    employees.sort(key=lambda x: (-x.salary, x.first_name, x.last_name), reverse=True)
    show_emp(employees)


def sort_emp_by_name_asc(employees):
    employees.sort(key=lambda x: x.first_name)
    show_emp(employees)


def add_emp(employees: []):
    employees.append(Employee("emp1001", "Nguyễn văn hải", "hà nội", 20, "0986789212", 10000, 2))
    employees.append(Employee("emp1002", "Nguyễn văn an", "hà nội", 22, "0325729123", 10000, 1))
    employees.append(Employee("emp1003", "Trần văn thủy", "hà nội", 23, "0376129212", 9500, 2))
    employees.append(Employee("emp1004", "Nguyễn huy hùng", "hà nội", 19, "0876589212", 8000, 6))
    employees.append(Employee("emp1005", "Mai văn thiện", "hà nội", 25, "0321989212", 3000, 4))
    employees.append(Employee("emp1006", "Trần văn ánh", "hà nội", 30, "0921459212", 2000, 3))
    employees.append(Employee("emp1007", "Nguyễn Minh Ánh", "hà nội", 20, "0989876123", 10000, 2))
    employees.append(Employee("emp1008", "Đỗ Thu Thủy", "hà nội", 20, "0326781123", 10000, 1))


def fin_max_salary(employees):
    max = 0
    for e in employees:
        if e.salary > max:
            max = e.salary
    return max


def show_list_emp_max_salary(employees):
    max_salary = fin_max_salary(employees)
    emp_max_salary = []
    for e in employees:
        if e.salary == max_salary:
            emp_max_salary.append(e)
    show_emp(emp_max_salary)


def find_emp_by_age(employees):
    age = int(input("Nhập tuổi cần tìm : "))
    emp_age = []
    for e in employees:
        if e.age == age:
            emp_age.append(e)
    show_emp(emp_age)


def show_emp_together_salary(employees):
    salary_list = []
    show_title()
    for e in employees:
        if e.salary not in salary_list:
            salary_list.append(e.salary)
    for salary in salary_list:
        list_together_salary = []
        for e in employees:
            if e.salary == salary:
                list_together_salary.append(e)
        for e_salary in list_together_salary:
            show_emp_infor(e_salary)


def find_emp_by_exp(employees):
    exp = int(input("Nhập năm kinh nghiệm cần tìm kiếm : "))
    emp_exp = []
    for e in employees:
        if e.exp == exp:
            emp_exp.append(e)
    show_emp(emp_exp)


def find_emp_by_three_last_number_phone(employees):
    number_phone = (input("Nhập 3 số cuối cần tìm kiếm :  "))
    emp_by_number = []
    for e in employees:
        if e.phone_number.find(number_phone, len(e.phone_number) - 3) != -1:
            emp_by_number.append(e)
    show_emp(emp_by_number)
