from LearnPython.Chapter5.Lesson5_3.Exercise2.Person import Person
from LearnPython.Chapter5.Lesson5_3.Exercise2.Student import Student
from LearnPython.Chapter5.Lesson5_3.Exercise2.StudentGraduate import StudentGraduate

person = Person("Nguyễn văn hải", "hà nội", "hai@xmail.com",
                "02/07/2002", "90812561271")
person.sleep()
person.relax()
person.eat("cơm")
person.do_work()
print("================================")
student_huy = Student("Đỗ văn huy", "Bình định", "huy@xmail.com",
                      "30/05/2001", "098126781289", "AT170454",
                      3.42, "ATTT")
student_huy.eat("mì tôm")
student_huy.relax()
student_huy.do_exam("Python")
student_huy.do_exercise("Java")
student_huy.sleep()
student_huy.do_work()
print("================================")
student_graduate_anh = StudentGraduate("Nguyễn Minh Ánh", "Hà Nội",
                                       "anh@xmail.com", "30/08/2002",
                                       "09812890121", "AT170403", 3.26,
                                       "ATTT", "2022", "Giỏi", 9000)
student_graduate_anh.go_to_work()
student_graduate_anh.reveive_certificate()
student_graduate_anh.sleep()
student_graduate_anh.do_work()
student_graduate_anh.relax()
