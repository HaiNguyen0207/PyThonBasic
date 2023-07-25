#!/usr/bin/python
# Mô đun nmap sử dụng để thực hiện quét mạng và kiểm tra các cổng trên các máy tính hoặc thiết bị khác nhau.
# sử dụng để kiểm tra bảo mật hệ thống và phát hiện các lỗ hổng bảo mật.
import nmap

# Mô đun optparse : phân tích cú pháp và xử lý các đối số dòng lệnh
# xác định các tùy chọn và đối số được truyền vào chương trình từ dòng lệnh,
# giúp cho việc viết các ứng dụng dòng lệnh trở nên dễ dàng hơn

import optparse


# get-argument() : phương thức lấy đối số từ dòng lệnh
# -d : domain
# -p :port
def get_argument():
    parser = optparse.OptionParser()  # khởi tạo 1 đối tượng
    # thêm cú pháp dòng lệnh : -d -p
    parser.add_option('-d', '--domain', dest='domain', help='Enter address domain to check !')
    parser.add_option('-p', '--port', dest='port', action='append', help='Enter address port to check !')
    options, arguments = parser.parse_args()
    if not options.domain:  # nếu lệnh ko hợp lệ
        parser.error('[-] Please enter address domain valid ! Example dantri.com.vn')  # thông báo lỗi
    if not options.port:
        parser.error('[-] Please enter address port valid ! Example 22,20,80,443...')

    return options  # trả về 2 giá trị : -d ,-p


# check_port() :kiểm tra trạng thái của một danh sách các cổng (port) trên một hoặc nhiều máy chủ (host)

def check_port(host_scan, port_list):
    try:
        # khởi tạp 1 đối tượng
        portScanner = nmap.PortScanner()
        # quét các cổng có trong"port_list"
        # arguments='-n -p' + port_list được sử dụng để chỉ định các đối số cho quét cổng nmap,
        # với -n chỉ định rằng không sử dụng phân giải tên miền DNS
        # -p được sử dụng để chỉ định danh sách các cổng được quét.
        portScanner.scan(hosts=host_scan, arguments='-n -p' + port_list)
        print(portScanner.command_line())  # in ra dòng lệnh
        # thông tin trạng thái của các máy chủ được lưu trữ trong biến host_list
        host_list = [(x, portScanner[x]['status']['state']) for x in portScanner.all_hosts()]
        # duyệt qua các máy chủ được quét và in ra trạng thái của từng máy chủ
        for host, status in host_list:
            print(host, status)
            print(portScanner[host])
            # qua các giao thức được quét (ví dụ: TCP, UDP) cho mỗi máy chủ
            for protocol in portScanner[host].all_protocols():

                print(f'Protocol : {protocol}')
                # keys() trên portScanner[host][protocol], lấy danh sách các khóa của cổng và thông tin
                listport = portScanner[host][protocol].keys()  # 20,21,22,23,80 ...
                # in ra danh sách các cổng được quét và trạng thái của chúng.
                for port in listport:
                    print('Port : %s State : %s' % (port, portScanner[host][protocol][port]['state']))
    except nmap.PortScannerError:
        print("An error occurred while scanning the network.")


if __name__ == '__main__':
    # lấy đối số thông qua phương thức get_argument()
    host_scan = get_argument().domain
    port_list = get_argument().port
    check_port(host_scan, ",".join(port_list))  # gọi phương thức check_port()
