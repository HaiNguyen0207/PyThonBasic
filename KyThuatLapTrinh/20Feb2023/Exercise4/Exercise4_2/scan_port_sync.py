#!/usr/bin/python3
# Mô đun nmap sử dụng để thực hiện quét mạng và kiểm tra các cổng trên
# các máy tính hoặc thiết bị khác nhau.
# Sử dụng để kiểm tra bảo mật hệ thống và phát hiện các lỗ hổng bảo mật.

import nmap
# mô-đun argparse để xử lý các tham số đầu vào.
import argparse


# lớp được tạo ra để quét cổng.
class NmapScanner:
    # Hàm khởi tạo của lớp NmapScanner nhận hai tham số đầu vào: địa chỉ IP và cổng.
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        # biến self.portScanner được khởi tạo là một đối tượng của lớp PortScanner
        self.portScanner = nmap.PortScanner()
        # scan () để quét cổng trên địa chỉ IP và cổng đã cho
        self.portScanner.scan(self.ip_address, self.port)
        print(f'[+] Executing command: {self.portScanner.command_line()}')

    # get_port_state () được sử dụng để lấy trạng thái của các cổng được quét
    def get_port_state(self):
        # all_hosts() được sử dụng để lấy tất cả các host trong kết quả quét của portScanner
        all_hosts = self.portScanner.all_hosts()

        # duyệt qua từng host và kiểm tra trạng thái của cổng đã được quét
        for host in all_hosts:
            # in trạng thái của cổng ,mở hoặc đóng
            try:
                port_state = self.portScanner[host]['tcp'][int(self.port)]['state']
                print(f"[+] {host} - {self.port}/tcp - {port_state}")
            except KeyError:
                print(f"[-] {host} - {self.port}/tcp - closed")

#get_arguments() được định nghĩa để lấy các đối số đầu vào từ dòng lệnh
#-d : domain
#-p : port
def get_arguments():
    # khởi tạo 1 đối tượng ArgumentParser
    parser = argparse.ArgumentParser(description='Scan for open ports on a given domain.')
    # thêm đối số
    parser.add_argument('-d', '--domain', dest='domain',
                        required=True, help='Domain address to scan.Example dantri.com.vn...')
    parser.add_argument('-p', '--ports', dest='ports',
                        required=True, help='Comma-separated list of ports to scan.Example 20,21,22,80..')

    return parser.parse_args() # trả về 2 giá trị domain và port


if __name__ == '__main__':
    host_scan = get_arguments().domain # domain lấy thông qua get_argument()
    port_list = get_arguments().ports.split(",") #port domain lấy thông qua get_argument()

    for port in port_list: # duyệt từng port
        # check trạng thái của mỗi port
        scanner = NmapScanner(host_scan, port)
        scanner.get_port_state()
