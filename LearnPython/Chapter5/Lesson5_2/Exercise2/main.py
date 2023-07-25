import LearnPython.Chapter5.Lesson5_2.Exercise2.employee_utils as utils

employees = []
size = 1
utils.add_emp(employees)
option = "=======================> Option <===================\n" \
         " ===> Lesson8_1. Thêm mới một nhân viên                  <===\n" \
         " ===> 2. Hiển thị danh sách sinh viên            <===\n" \
         " ===> 3. Tìm nhân viên theo mã nhân viên         <===\n" \
         " ===> 4. Xóa nhân viên theo mã cho trước         <===\n" \
         " ===> 5. Sắp xếp nhân viên theo lương giảm dần   <===\n" \
         " ===> 6. Sắp xếp nhân viên theo tên a - z        <===\n" \
         " ===> 7. Liệt kê nhân viên có mức lương cao nhất <===\n" \
         " ===> 8. Liệt kê các nhân viên có cùng mức lương <===\n" \
         " ===> 9. Tìm nhân viên có tuổi là x              <===\n" \
         " ====> 10. Tìm nhân viên có n năm kinh nghiệm    <===\n" \
         " ====> 11. Tìm nhân viên theo 3 số cuối của SDT  <===\n" \
         " ====> 0. Kết thúc chương trình                  <===\n" \
         " ====================================================\n"

while True:
    x = int(input(option))
    match x:
        case 0:
            print("===> Chương trình kết thúc <====")
            break
        case 1:
            emp = utils.add_new_emp()
            employees.append(emp)
            size = size + 1
            print("===> Thêm mới nhân viên thành công <===")
        case 2:
            utils.show_emp(employees)
        case 3:
            if size > 0:
                utils.find_emp_by_id(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 4:
            if size > 0:
                utils.remove_emp_by_id(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 5:
            if size > 0:
                utils.sort_emp_by_salary_desc(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 6:
            if size > 0:
                utils.sort_emp_by_name_asc(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 7:
            if size > 0:
                utils.show_list_emp_max_salary(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 8:
            if size > 0:
                utils.show_emp_together_salary(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 9:
            if size > 0:
                utils.find_emp_by_age(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 10:
            if size > 0:
                utils.find_emp_by_exp(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case 11:
            if size > 0:
                utils.find_emp_by_three_last_number_phone(employees)
            else:
                print("===> Danh sách nhân viên hiện thời rỗng <===")
        case _:
            print("===> Sai tùy chọn ! Vui lòng kiểm tra lại <===")
