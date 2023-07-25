# !/usr/bin/python
# Mô đunchttp.client cung cấp các lớp và hàm để tạo và gửi các yêu cầu HTTP đến các máy chủ web và
# xử lý các phản hồi HTTP trả về.

# Module này được sử dụng để tương tác với các trang web hoặc API sử dụng giao thức HTTP.
# hỗ trợ tạo các yêu cầu HTTP như GET, POST, PUT, DELETE, HEAD, OPTIONS và TRACE,
# cũng như xử lý các phản hồi HTTP và các trạng thái phản hồi như 200 OK,
# 404 Not Found, 500 Internal Server Error, vv.
import http.client


def check_status(url):
    conn = http.client.HTTPConnection(url)  # tao ra 1 ket noi vs may chu url
    # list chứa phương thức
    # có nhiều phương thức ,nhưng em đề cập đến 2 cái là GET và HEAD
    methods = ['GET', 'HEAD']
    for method in methods:  # duyệt từng phương thức một
        print(f'=======> {method} <======')  # in trang phân tách
        conn.request(method, '/')  # gửi yêu cầu
        # phương thức HTTP "GET hay HEAD" để gửi một yêu cầu tới địa chỉ URL "/"
        # "/" là một địa chỉ URL cục bộ của máy chủ,
        # chỉ cho một trang chủ hoặc trang mặc định của một trang web.
        res = conn.getresponse()
        print(type(res))  # tra ve doi tuong

        # res.status chứa mã trạng thái HTTP của phản hồi từ máy chủ web, ví dụ như 200, 404, 500,
        # res.reason chứa thông điệp trạng thái tương ứng với mã trạng thái,
        # giúp hiểu rõ hơn về trạng thái đó
        print("Status: ", res.status, res.reason)  # lấy status và reason
        # print("All headers: ", res.getheaders())
        print("Data: ", res.read())
    conn.close()  # đóng


if __name__ == '__main__':
    domain = input('Enter domain : ')
    url = 'www.' + domain  # tên miền lấy từ câu lệnh thông qua phương thức get_arguments()
    check_status(url)  # gọi phương thức
