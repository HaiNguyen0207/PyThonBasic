from LearnPython.Chapter5.Lesson5_2.Exercise3.bank_account \
    import bank_account


# thêm mới Lesson8_1 tài khoản
def add_new_bank_account() -> bank_account:
    number_account = input("Nhập số tài khoản : ")
    name_account = input("Nhập tên tài khoản : ")
    type_account = input("Nhập loại tài khoản : ")
    surplus = int(input("Nhập số dư : "))
    name_bank = input("Nhập tên ngân hàng : ")
    release_date = input("Nhập ngày phát hành : ")
    expired_date = input("Nhập ngày hết hạn : ")
    return bank_account(number_account, name_account,
                        type_account, surplus, name_bank,
                        release_date, expired_date)


def show_title():
    print(f'{"Số TK":15}{"Tên TK":20}{"Loại TK":15}'
          f'{"Số Dư":10}{"Tên NH":15}{"Phát Hành":15}{"Hết Hạn":10}')


def show_account_infor(e: bank_account):
    print(f'{e.number_account:15}{e.name_account:20}{e.type_account:15}'
          f'{e.surplus:<10}{e.name_bank:15}{e.release_date:15}{e.expiration_date:10}')


# hiển thị thông tin tài khoản
def show_accounts(accounts):
    show_title()
    for e in accounts:
        show_account_infor(e)


# nạp tiền :
def find_account_by_number(accounts, number_account) -> bank_account:
    for e in accounts:
        if e.number_account == number_account:
            return e
    return None


def check_money_deposit(amount):
    if (amount > 0):
        return True
    return False


def deposit(accounts):
    number_account = input("Nhập số tài khoản nạp tiền : ")
    account = find_account_by_number(accounts, number_account)
    if (account != None):
        amount = int(input("Nhập số tiền nạp : "))
        if (check_money_deposit(amount)):
            account.surplus += amount
            print("===> Đã nạp thành công <====")
        else:
            print("===> Số tiền nạp không hợp lệ <===")

    else:
        print("===> Số tài khoản nạp không hợp lệ <===")


# rút tiền
def check_money_withdraw(amount, surplus):
    if amount > 0 and amount <= surplus:
        return True
    return False


def withdraw(accounts):
    number_account = input("Nhập số tài khoản rút tiền : ")
    account = find_account_by_number(accounts, number_account)
    if (account != None):
        amount = int(input("Nhập số tiền rút : "))
        if (check_money_withdraw(amount, account.surplus)):
            account.surplus -= amount
            print("===> Đã rút thành công <====")
        else:
            print("===> Số tiền rút không hợp lệ <===")

    else:
        print("===> Số tài khoản rút không hợp lệ <===")


# chuyển tiền
def transfer(accounts):
    number_account_a = input("Nhập số tài khoản chuyển : ")
    account_a = find_account_by_number(accounts, number_account_a)
    if account_a != None:
        number_account_b = input("Nhập số tài khoản nhận : ")
        account_b = find_account_by_number(accounts, number_account_b)
        if account_b != None:
            money = int(input("Nhập số tiền chuyển : "))
            if check_money_withdraw(money, account_a.surplus):
                account_a.surplus -= money
                account_b.surplus += money
                print("===> Đã chuyển tiền thành công <===")
            else:
                print("===> Số tiền chuyển không hợp lệ <===")
        else:
            print("===> Số tài khoản nhận không hợp lệ ! <===")
    else:
        print("===> Số tài khoản chuyển không hợp lệ ! <===")


# tìm tài khoản theo tên tài khoản
def find_account_by_name(accounts):
    result = []
    name = input("Nhập tên tài khoản cần tìm kiếm : ")
    for e in accounts:
        if e.first_name.lower() == name.lower():
            result.append(e)
    print("===> Danh sách tìm kiếm trả về <===")
    show_accounts(result)


# tìm tài khoản theo số tài khoản
def search_account_by_number(accounts):
    number_account = input("Nhập số tài khoản cần tìm kiếm : ")
    result = []
    acc = find_account_by_number(accounts, number_account)
    if acc != None:
        result.append(acc)
    print("===> Danh sách tìm kiếm trả về <===")
    show_accounts(result)


# tìm tài khoản theo số dư là x
def find_account_by_surplus(accounts):
    surplus = int(input("Nhập số dư tìm kiếm : "))
    result = []
    for e in accounts:
        if e.surplus >= surplus:
            result.append(e)
    print("===> Danh sách tìm kiếm trả về <===")
    show_accounts(result)


# xóa tài khoản theo số tài khảon
def find_account(accounts, number_account):
    for i in range(len(accounts)):
        if (accounts[i].number_account == number_account):
            return i
    return -1


def remove_account_by_number(accounts):
    number_account = input("Nhập số tài khoản cần xóa : ")
    index = find_account(accounts, number_account)
    if index != -1:
        accounts.pop(index)
        print("===> Xóa tài khoản thành công <===")
    else:
        print("===> Tài khoản xóa không tồn tại <===")


# sắp xếp theo số dư tăng dần
def sort_accounts_by_surplus_asc(accounts):
    accounts_copy = accounts.copy()
    accounts_copy.sort(key=lambda x: x.surplus)
    print('===> Danh sách sắp xếp theo số dư tăng dần <===')
    show_accounts(accounts_copy)


# sắp xếp theo số dư giảm dần
def sort_accounts_by_surplus_desc(accounts):
    accounts_copy = accounts.copy()
    accounts_copy.sort(key=lambda x: (-x.surplus, x.first_name))
    print('===> Danh sách sắp xếp theo số dư tăng dần <===')
    show_accounts(accounts_copy)


def add_account(accounts):
    accounts.append(bank_account("1111", "nguyễn văn hải", "tiết kiệm",
                                 9000, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("2222", "nguyễn văn an", "tiết kiệm",
                                 8000, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("3333", "trịnh văn hải", "tiết kiệm",
                                 10000, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("4444", "bùi công an", "tiết kiệm",
                                 9500, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("5555", "trần thị thủy", "tiết kiệm",
                                 9820, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("6666", "mai xuân quyết", "tiết kiệm",
                                 7800, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("7777", "nguyễn duy anh", "tiết kiệm",
                                 8300, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("8888", "đào bá lộc", "tiết kiệm",
                                 5000, "tp bank", "01/01/2022", "01/01/2027"))
    accounts.append(bank_account("9999", "trần thủy tiên", "tiết kiệm",
                                 5200, "tp bank", "01/01/2022", "01/01/2027"))
