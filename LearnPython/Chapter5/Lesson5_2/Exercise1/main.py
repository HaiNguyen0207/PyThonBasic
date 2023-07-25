from LearnPython.Chapter5.Lesson5_2.Exercise1.Exercise1 import Fraction

fractions = []


def calculator_add():
    data_one = [int(x) for x in input("Nhập một phân số (a1/b1) : ")
    .split("/")]
    f_a = Fraction(int(data_one[0]), int(data_one[1]))
    data_two = [int(x) for x in input("Nhập một phân số (a2/b2) : ")
    .split("/")]
    f_b = Fraction(int(data_two[0]), int(data_two[1]))
    f_add = Fraction(None, None)
    f_add.addition(f_a.numerator, f_a.denominator, f_b.numerator,
                   f_b.denominator)
    f_add.show_fraction()
    print()


def calculator_sub():
    data_one = [int(x) for x in input("Nhập một phân số (a1/b1) : ")
    .split("/")]
    f_a = Fraction(int(data_one[0]), int(data_one[1]))
    data_two = [int(x) for x in input("Nhập một phân số (a2/b2) : ")
    .split("/")]
    f_b = Fraction(int(data_two[0]), int(data_two[1]))
    f_sub = Fraction(None, None)
    f_sub.subtraction(f_a.numerator, f_a.denominator, f_b.numerator,
                      f_b.denominator)
    f_sub.show_fraction()
    print()


def calculator_mul():
    data_one = [int(x) for x in input("Nhập một phân số (a1/b1) : ")
    .split("/")]
    f_a = Fraction(int(data_one[0]), int(data_one[1]))
    data_two = [int(x) for x in input("Nhập một phân số (a2/b2) : ")
    .split("/")]
    f_b = Fraction(int(data_two[0]), int(data_two[1]))
    f_mul = Fraction(None, None)
    f_mul.multiplication(f_a.numerator, f_a.denominator, f_b.numerator,
                         f_b.denominator)
    f_mul.show_fraction()
    print()


def calculator_div():
    data_one = [int(x) for x in input("Nhập một phân số (a1/b1) : ")
    .split("/")]
    f_a = Fraction(int(data_one[0]), int(data_one[1]))
    data_two = [int(x) for x in input("Nhập một phân số (a2/b2) : ")
    .split("/")]
    f_b = Fraction(int(data_two[0]), int(data_two[1]))
    f_div = Fraction(None, None)
    f_div.division(f_a.numerator, f_a.denominator, f_b.numerator,
                   f_b.denominator)
    f_div.show_fraction()
    print()


def create_new_fraction():
    data = [int(x) for x in input("Nhập một phân số (a/b) : ")
    .split("/")]
    numerator = int(data[0])
    denominator = int(data[1])
    return Fraction(numerator, denominator)


def compact():
    data = [int(x) for x in input("Nhập phân số (a/b) = ")
    .split("/")]
    f = Fraction(int(data[0]), int(data[1]))
    f.compact()
    f.show_fraction()
    print()


def calculator_sum_current_list():
    sum = 0
    for e in fractions:
        sum += float(e.numerator / e.denominator)
    print(sum)


def mul_list():
    mul = 1
    for e in fractions:
        mul *= float(e.numerator / e.denominator)
    print(mul)


option = "======================> Option <=====================\n" \
         "=> Lesson8_1.  Nhập vào một phân số mới                      =\n" \
         "=> 2. Hiển thị danh sách các phân số                 =\n" \
         "=> 3. Rút gọn phân số nhập vào từ bàn phím           =\n" \
         "=> 4. Tính tổng hai phân số                          =\n" \
         "=> 5. Tính tổng các phân số hiện có trong danh sách  =\n" \
         "=> 6. Tính hiệu hai phân số                          = \n" \
         "=> 7. Tính tích hai phân số                          =\n" \
         "=> 8. Tính thương hai phân số                        =\n" \
         "=> 9. Tính tích các phân số hiện có trong danh sách  =\n" \
         "=> 10. Kết thúc chương trình                         =\n" \
         "======================================================\n"

while True:
    chocie = int(input(option))
    match chocie:
        case 1:
            fraction = create_new_fraction()
            fractions.append(fraction)
            print("==> Thêm mới phân số thành công <===")
        case 2:
            for e in fractions:
                e.show_fraction()
            print()
        case 3:
            compact();
        case 4:
            calculator_add()
        case 5:
            calculator_sum_current_list()
        case 6:
            calculator_sub()
        case 7:
            calculator_mul()
        case 8:
            calculator_div()
        case 9:
            mul_list()
        case 10:
            print("===> Kết thúc chương trình <===")
            break
