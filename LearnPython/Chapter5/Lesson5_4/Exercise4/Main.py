from LearnPython.Chapter5.Lesson5_4.Exercise4.Employee import Employee
from LearnPython.Chapter5.Lesson5_4.Exercise4.Manager import Manager
from LearnPython.Chapter5.Lesson5_4.Exercise4.Programmer import Programmer
from LearnPython.Chapter5.Lesson5_4.Exercise4.Tester import Tester

emp_hai = Employee("EMP1001", "Nguyễn văn hải", "hai@xmail.com"
                   , "0983638524", 9000000, 27)
emp_hai.check_in()
emp_hai.check_out()
emp_hai.do_work("Code")
print(f"Lương nhận là {emp_hai.calculator_salary()}")
print("==================================")
programmer_quan = Programmer("EMP1011", "Trần Minh Quân", "quan@xmail.com"
                             , "0876982145", 9000000, 27, "Lập trình", 5, 10, 19)
programmer_quan.do_work("Lập trình...")
programmer_quan.give_task("Android..")
programmer_quan.fix_bug()
programmer_quan.report_job()
print(f"Lương Nhận : {programmer_quan.calculator_salary()}")
print("================================")
manager_quang = Manager("EMP1099", "Trình Đình Quang", "quang@xmail.com",
                        "0982156137", 12000000, 23, "Giám đốc", "2022-2027",
                        9000000)
manager_quang.meeting()
manager_quang.signing()
manager_quang.check_out()
print(f"Lương nhận : {manager_quang.calculator_salary()}")
print("================================")
tester_thuy = Tester("EMP1998", "Bùi Thị Thuy Thủy", "thuy@xmail.com",
                     "032457812", 90000000, 23, "tester", "laptop", 12, 15)
tester_thuy.do_work("dò lỗi ...")
tester_thuy.check_out()
tester_thuy.give_project()
print(f"Lương nhận : {tester_thuy.calculator_salary()}")
