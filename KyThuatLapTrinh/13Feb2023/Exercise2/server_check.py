#!/usr/bin/python

"""
+ Mô đun socket : tạo thành cơ sở của tất cả các mạng giao tiếp trong python
    cho phép các ứng dụng tạo các đối tượng socket, kết nối và giao tiếp với các thiết bị mạng khác,
    đọc và ghi dữ liệu trên mạng, lắng nghe các yêu cầu từ máy khách và phản hồi các yêu cầu đó
+ Mô đun threading : cung cấp các đối tượng thread để quản lý các luồng
    Sử dụng 'theading' : chương trình có thể thực hiện nhiều tác vụ đồng thời,
    tăng tốc độ thực thi và cải thiện hiệu suất
"""
import socket
import threading

"""
 ví dụ kiểm tra các dịch vụ mở trên máy chủ có địa chỉ IP là 192.168.0.1 
và các cổng như 21 (FTP),22 (SSH), 23 (Telnet), 80 (HTTP), 443 (HTTPS)
"""


# phương thức kiêểm tra dịch vụ ip
# tham số nhận vào : ip - port -name
# thông báo dịch vụ có hoạt động hay không
def check_service(ip, port, name):
    try:  # bắt ngoại lệ ..

        # Tạo socket của client  ,client_socket
        # - Tham số đầu tiên nhận vào là kiểu địa chỉ IP ,cụ thể đây là IPV4
        # - Tham số thứ hai nhận vào cho biết loại socket  là TCP
        service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        service_socket.settimeout(5)  # đặt thời gian chờ đợi dịch vụ là 5s

        result = service_socket.connect_ex((ip, port))
        if result == 0:  # = 0 là có chạy
            print(f'{name} service is runing on {ip} :{port} ')
        else:  # ngược lại
            print(f'{name} service is not runing on {ip} :{port} ')
    except socket.error:  # xảy ra ngoại lệ thì thông báo
        print(f'An error occurred while connecting to {name} on {ip}:{port}')
    finally:  # không là đóng 
        service_socket.close()


if __name__ == '__main__':
    threads = []  # tạo các list chứa các luồng
    services = [('FTP', 21), ('SSH', 22), ('SMTP', 25), ('HTTP', 80),
                ('POP3', 110), ('IMAP', 143), ('HTTPS', 443), ('MySQL', 3306)]  # danh sach cach dich vu

    ip = input('Enter IP : ')
    port = int(input('Enter Port : '))

    boolean = False  # biến này kiểm tra xem port có trong services trên k

    for service in services:  # duyệt từng dịch vụ để kiểm tra
        if service[1] == port:
            boolean = True  # nếu có thì boolean là true

            """
                   tạo một thread để thực thi hàm handle_server để xử lý dữ liệu nhận được từ server
                   - target là một đối tượng gọi lại (callable) mà đối tượng Thread này sẽ thực hiện
                    khi bắt đầu chạy ,cụ thể đối tượng đây là "check_service"
                   - args là một bộ sưu tập các tham số vị trí mà callable sẽ được gọi với.
                   '   Đây là một tuple trống mặc định ,cụ thể nhận vào 1 tuple  
                   chứa một tham số ip, port, name
            """
            t = threading.Thread(target=check_service, args=(ip, service[1], services[0]))
            threads.append(t)  # thêm vào list thread
            t.start()  # # bắt đầu thực thi Thread mới tương ứng

    if boolean == False:  # nếu không có thi thông bao
        print('Port invalid ! Invalid port! Please enter port :'
              ' 21,22,25,80,110,143,443,3306 to check ')

    """"
        Duyệt hết luồng trong list threads
        đóng tất cả các luồng
        đảm bảo khi chương trình kết thúc ,không còn luồng nào hoạt động ngầm hay là treo ...
    """
    for t in threads:
        t.join()  # ket thuc thread
