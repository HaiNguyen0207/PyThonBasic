#!/usr/bin/python
# Mô đun optparse : phân tích cú pháp và xử lý các đối số dòng lệnh
# xác định các tùy chọn và đối số được truyền vào chương trình từ dòng lệnh,
# giúp cho việc viết các ứng dụng dòng lệnh trở nên dễ dàng hơn
# ở đây đối số là domain
import optparse

# Mô đun requests :được sử dụng để gửi các yêu cầu HTTP  và nhận các phản hồi HTTP từ máy chủ web.
# gửi các yêu cầu GET, POST, PUT, DELETE và các loại yêu cầu HTTP khác
# hữu ích khi muốn tương tác với các API hoặc trang web từ trong ứng dụng Python của mình
import requests


# read_file_http_userpass :Đọc file chứa danh sách username và password

def read_file_http_userpass():
    # sử dụng with statement thay vì mở đóng file thủ công
    # nhận vào 2 tham số "tên file " ,"r"
    with open('http_default_userpass.txt', 'r') as f:  # file sẽ được đóng tự động ngay sau khi đọc xong
        data = [line.strip() for line in f.readlines()]  # tách /n
    return data  # trả về nôi dung file


# read_file():  Đọc file chứa danh sách các mục (predictable URL) cần kiểm tra
def read_file():
    # sử dụng with statement thay vì mở đóng file thủ công
    with open('Logins.txt', 'r') as f:
        content = [line.strip() for line in f.readlines()]  # tách /n
    return content  # trả về nội dung


#  Kiểm tra đăng nhập với mỗi cặp username và password trong danh sách mặc định
def try_login(url):
    data = read_file_http_userpass()
    # duyệt từng cặp userpass
    for e in data:
        username = e.split(" ")[0]  # username
        password = e.split(" ")[1]  # passowrd
        payload = {'username': username, 'password': password}
        # requests  thực hiện một yêu cầu HTTP POST đến một URL cụ thể qua post
        # payload chứa thông tin đăng nhập bao gồm tên đăng nhập và mật khẩu
        response = requests.post(url, data=payload)
        # nếu chuỗi "Login successful " có xuất hiện trong response trả về
        if 'Login successful' in response.text:
            # login thành công
            print(f'{payload} login to {url} success!')
        else:  # ngược  lại
            # login thất bại
            print(f'{payload} login to {url} failed!')
    print("====================")  # phân tách mỗi url


# phương thức get-arguments()   sử dụng để lấy các đối số từ dòng lệnh
# lấy đối số host để kiểm tra dịch vụ
def get_arguments():
    # -d hoặc --domain được sử dụng để truyền cổng vào chương trình.
    # Nếu địa chỉ host không được cung cấp, hàm sẽ in ra thông báo lỗi tương ứng
    parser = optparse.OptionParser()  # khởi tạo 1 đối tượng
    parser.add_option('-d', '--domain', dest='domain',
                      help='Enter domain address to check ')

    options, arguments = parser.parse_args()

    if not options.domain:  # lỗi
        parser.error('[-] Please enter a valid domain address! Example: testphp.vulnweb.com ')  # thông báo lỗi
    return options.domain  # trả về domain


# Tìm kiếm trang login
# nhận vào một URL (domain) đang phân tích
# và 1 list predictable URL trong fuzzdb
def check_login(logins, domain):
    # sử dụng with statement để tạo ra một session session
    with requests.Session() as session:
        # duyệt qua danh sách logins để kiểm tra từng URL.
        for login in logins:
            url = domain + login
            try:  # ngoại lệ
                # gửi một yêu cầu GET đến đó và kiểm tra xem nó trả về mã trạng thái HTTP
                response = session.get(url)
                print(f'Checking ... {url}')
                if response.status_code == 200:  # nếu trạng thái = 200
                    print(f'Login resource detected: {url}')  # tìm thấy
                    try_login(url)  # thử đăng nhập vài tài khoản
            except requests.exceptions.RequestException as e:  # xảy ra ngoại lệ
                print(f'Error connecting to {url}: {e}')  # in báo lỗi


if __name__ == '__main__':
    domain = 'http://testphp.vulnweb.com'
    logins = read_file()
    check_login(logins, domain)
