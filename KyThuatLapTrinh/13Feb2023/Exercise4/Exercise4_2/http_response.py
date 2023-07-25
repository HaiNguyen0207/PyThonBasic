#!/usr/bin/python

# mô đun urllib.request cung cấp các công cụ để mở các URL (địa chỉ web)
# và truy xuất dữ liệu từ chúng...
import urllib.request

# Mô đun urllib.request này bao gồm nhiều lớp và hàm để tạo và gửi các yêu cầu HTTP và HTTPS đến máy
# chủ web và xử lý các phản hồi được trả về từ máy chủ đó
# Lớp Request là một trong số đó, được sử dụng để tạo yêu cầu HTTP hoặc HTTPS đến máy chủ web.
# Lớp này cung cấp một cách để tùy chỉnh các yêu cầu bằng cách thêm các tiêu đề HTTP,
# phương thức yêu cầu và thân yêu cầu.
from urllib.request import Request

if __name__ == '__main__':
    # input() là 1 hàm tich hợp trong python ,dùng để nhập dữ liệu từ bàn phím ,
    # ở đây hiển thị thông báo cho người dùng nhập tên miền để check
    domain = input('Enter domain to check : ')
    url = 'https://www.' + domain + '/'
    response = urllib.request.urlopen(url)  # gửi một yêu cầu HTTP GET tới địa chỉ URL
    print('===> Response header <===')  # hiển thị thông báo ra màn hình

    # lấy tất cả các header (phần tiêu đề) và giá trị tương ứng của nó từ một phản hồi HTTP.
    # (header, value) được trả về bởi phương thức getheaders() của đối tượng response
    for header, value in response.getheaders():  # vòng lặp for duyệt qua tất cả các cặp (header, value)
        print(f'{header}:{value}')  # in ra

    print('=================')  # hiển thị phân tách

    request = Request(url)  # tạo ra một object Request với thông tin yêu cầu (request) được gửi đến server
    request.add_header('User-agent', ' 12345')  # them 1 header

    # lấy ra tất cả các header trong request và in ra giá trị của chúng
    for header, value in request.header_items():  # header_items() trả về một đối tượng iterable
        print(f'{header} :{value}')
