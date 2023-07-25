import LearnPython.Chapter5.Lesson5_2.Exercise3.bank_account_utils as utils

accounts = []
utils.add_account(accounts)
option = "=====================> Option <===========================\n" \
         "=> Lesson8_1. Thêm mới Lesson8_1 tài khoản                               =\n" \
         "=> 2. Hiển thị thông tin tài khoản hiện có               =\n" \
         "=> 3. Nạp tiền vào số tài khoản cho trước                =\n" \
         "=> 4. Rút tiền khỏi số tài khoản cho trước               =\n" \
         "=> 5. Chuyển tiền theo số tài khoản                      =\n" \
         "=> 6. Tìm tài khoản theo tên                             =\n" \
         "=> 7. Tìm tài khoản theo số tài khoản                    =\n" \
         "=> 8. Tìm tài khoản theo số dư                           =\n" \
         "=> 9. Xóa tài khoản theo số tài khoản                    =\n" \
         "=> 10 .Sắp xếp tài khoản theo số dư tăng dần             =\n" \
         "=> 11. Sắp xếp tài khoản theo số dư giảm dần             =\n" \
         "==========================================================\n"
while True:
    choice = int(input(option))
    match choice:
        case 1:
            acc = utils.add_new_bank_account()
            accounts.append(acc)
            print("===> Thêm mới tài khoản thành công <===")
        case 2:
            if len(accounts) > 0:
                utils.show_accounts(accounts)
            else:
                print("===> Danh sách hiện thời rỗng <===")
        case 3:
            utils.deposit(accounts)
        case 4:
            utils.withdraw(accounts)
        case 5:
            utils.transfer(accounts)
        case 6:
            utils.find_account_by_name(accounts)
        case 7:
            utils.search_account_by_number(accounts)
        case 8:
            utils.find_account_by_surplus(accounts)
        case 9:
            utils.remove_account_by_number(accounts)
        case 10:
            utils.sort_accounts_by_surplus_asc(accounts)
        case 11:
            utils.sort_accounts_by_surplus_desc(accounts)
        case __:
            print("===> Sai chức năng ! Vui lòng thử lại <===")
