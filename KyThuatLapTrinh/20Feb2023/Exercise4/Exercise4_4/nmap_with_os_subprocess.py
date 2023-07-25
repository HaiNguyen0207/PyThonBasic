# !/usr/bin/python3
# mô-đun argparse để xử lý các tham số đầu vào
import argparse
# mô đun subprocess() :thực thi các lệnh hệ thống hoặc
# các chương trình bên ngoài từ trong chương trình Python
# ung cấp các phương thức để chạy các tiến trình,
# quản lý các luồng tiến trình,
# truyền tham số và nhận kết quả trả về từ các chương trình khác.
import subprocess


# get_arguments() được định nghĩa để lấy các đối số đầu vào từ dòng lệnh


def get_arguments():
    # khởi tạo 1 đối tượng ArgumentParser
    parser = argparse.ArgumentParser(description='Scan for open ports on a given domain.')
    # thêm đối số
    parser.add_argument('-i', '--ip', dest='ip',
                        required=True, help='Ip address to scan...Example 183.81.34.136')

    return parser.parse_args()  # trả về ip


if __name__ == '__main__':
    # subprocess.run() được sử dụng để thực thi lệnh nmap với tùy chọn
    # capture_output=True được sử dụng để bắt đầu đầu ra của lệnh được thực thi.
    # text=True được sử dụng để chuyển đổi đầu ra của lệnh thành chuỗi văn bản.
    #-A để lấy chi tiết thông tin
    result = subprocess.run(["nmap", "-A", get_arguments().ip], capture_output=True, text=True)
    # result.stdout được sử dụng để hiển thị đầu ra của lệnh trên terminal.
    print(result.stdout)
