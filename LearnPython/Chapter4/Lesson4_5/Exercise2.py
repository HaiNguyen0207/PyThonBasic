"""
Bài 2. Thông tin bảng lương tháng 15 của một công ty gồm nhiều dòng, mỗi dòng có dạng: <mã
nhân viên> <tiền lương>. Hãy cho biết mã nhân viên và tiền lương của nhân viên có tiền lương
cao nhất và thấp nhất.
"""


def find_min_salary(dict_emp):
    min = [int(x) for x in dict_emp.values()]
    min.sort()
    return int(min[0])


def find_max_salary(dict_emp: dict):
    max = [int(x) for x in dict_emp.values()]
    max.sort(reverse=True)
    return int(max[0])


def show_result(dict_emp: dict, key_list):
    min_salary = find_min_salary(dict_emp)
    max_salary = find_max_salary(dict_emp)
    for e in key_list:
        if int(dict_emp.get(e)) == max_salary or int(dict_emp.get(e)) == min_salary:
            print(f"\n{e} : {dict_emp.get(e)}", end=" ")


test = int(input())
for i in range(test):
    amount_emp = int(input())
    dict_emp = dict()
    for e in range(amount_emp):
        data = [x for x in input().split()]
        dict_emp[data[0]] = data[1]
    key_list = [x for x in dict_emp.keys()]
    show_result(dict_emp, key_list)
