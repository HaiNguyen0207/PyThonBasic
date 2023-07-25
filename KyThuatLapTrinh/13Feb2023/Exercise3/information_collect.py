#!/usr/bin/python

"""
+ Mô đun socket : tạo thành cơ sở của tất cả các mạng giao tiếp trong python
    cho phép các ứng dụng tạo các đối tượng socket, kết nối và giao tiếp
    với các thiết bị mạng khác,
    đọc và ghi dữ liệu trên mạng, lắng nghe các yêu cầu từ máy khách và
     phản hồi các yêu cầu đó

"""

import socket


# phương thức get-arguments()   sử dụng để lấy các đối số từ dòng lệnh
# lấy đối số host để kiểm tra dịch vụ


"""
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
"""


# phương thức hiển thị các thông tin về hệ thống: OS, hostname, ip, ..
def display_information_socket(host_name, ip_host_name, domain, ip):
    try:  # bắt ngoại lệ ,nếu có xảy ra

        # dưới đây là hiển thị thông tin  quả phương thức print() tích hợp của python

        print(f"Hostname: {host_name}")  # hiển thị tên máy chủ
        print(f"IP address host name: {ip_host_name}")  # hiển thị ip máy chủ
        print(f"Domain: {domain}")  # hiển thị tên miền
        print(f"IP address {domain} : {ip}")  # hiển thị địa chỉ ip của tên miêền

        # getfqdn() trong Python dùng để lấy tên đầy đủ của máy tính hiện tại
        # nếu đối số truyền vào  là tên miền : sẽ trả về tên đầy đủ của máy chủ được liên kết với
        # địa chỉ IP đó
        print(f'Fully Qualified Domain Name of the host : {socket.getfqdn(domain)}')

        """
        getaddrinfo()  thực hiện phân giải tên miền thành địa chỉ IP
        giúp truy cập các tài nguyên trên internet.
        tham số nhận vào lần lượt là  : + host: Tên miền hoặc địa chỉ IP của máy chủ cần kết nối.
                                         + port: Cổng mà chương trình muốn kết nối đến.
                                         + family: Loại địa chỉ (IPv4 hoặc IPv6) mà chương trình muốn
                                          sử dụng để kết nối.
                                         + type : kiểu kết nối (TCP hay UDP)
                                         + proto: Giao thức mạng mà chương trình muốn sử dụng (thường là 0,
                                         + tức là tự động chọn giao thức phù hợp).

        Hàm này trả về một danh sách các bộ (tuple) gồm các thông tin về địa chỉ IP, cổng và
        các thông tin khác cần thiết để thiết lập kết nối tới máy chủ
        """
        print(f'Get addrinfo : {socket.getaddrinfo(domain, None, 0, socket.SOCK_STREAM)}')

        # gethostbyaddr() sử dụng địa chỉ IP như đối số và trả về thông tin về máy chủ
        # có địa chỉ IP đó
        # thông tin trả về là một tuple gồm tên máy chủ chính, các tên địa chỉ khác
        # và danh sách các địa chỉ IP của máy chủ
        print(f'Reverse lookup: {socket.gethostbyaddr(ip)[0]}')

        # getservbyname() sử dụng để tìm kiếm thông tin về một dịch vụ trên một máy tính
        # nhận vào hai tham số, là tên dịch vụ cần tìm và tên giao thức được sử dụng
        # (thường là 'tcp' hoặc 'udp')
        # trả về là một tuple chứa các thông tin về dịch vụ đó như tên dịch vụ, số hiệu cổng,
        # tên giao thức, ...
        print(f'Service name for TCP protocol: {socket.getservbyname("http", "tcp")}')

        # getprotobyname() trả về số hiệu giao thức (protocol number) tương ứng
        # với tên giao thức được chỉ định.
        # sử dụng khi cần truyền thông tin về giao thức từ ứng dụng đến hệ thống hoặc ngược lại.
        print("Protocol number for TCP: " + str(socket.getprotobyname("tcp")))


    except socket.error as error:  # văng ra ngoại lệ của socket
        print(f'Error: {error}')  # thông báo ngoại lệ
        pass  # pass(bỏ qua)


if __name__ == '__main__':
    host_name = socket.gethostname()  # lấy tên máy chủ
    ip_host_name = socket.gethostbyname(host_name)  # lấy địa chỉ ip máy chủ
    domain = input('Enter domain : ')
    url = 'www.' + domain  # host,lấy đối số từ phương thức get_arguments()

    ip = socket.gethostbyname(url)  # truy vấn địa chỉ IP của tên miền

    # lời gọi phương thức display_information_socket()
    display_information_socket(host_name, ip_host_name, url, ip)
