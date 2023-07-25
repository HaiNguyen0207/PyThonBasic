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


# phương thức xử lý   liệu được gửi từ server tới client
# tham số nhận vào là đối tượng socket của client
def handle_server(client_socket):
    # bắt ngoại lệ ,nếu không xảy ra ngoại lệ thì thực hiện code trong khối try
    try:
        # lặp vô hạn ,chờ đợi và nhận hết dữ liệu bên server
        while True:
            data = client_socket.recv(1024)  # nhận dữ liệu với kích thước tối đa là 1024 byte
            if data:  # nếu chưa hết dữ liệu , in dưới dạng chuỗi unicode
                print(f'{data.decode()}')
                print("===============")  # phân tách
            else:  # Nếu không có dữ liệu được nhận,  sẽ kết thúc vòng lặp.
                break
    except OSError:  # xảy ra ngoại lệ OSError thì pass (bỏ qua)
        pass


if __name__ == '__main__':
    threads = []  # khai báo 1 list ,lưu các luồng

    # Tạo socket của client  ,client_socket
    # - Tham số đầu tiên nhận vào là kiểu địa chỉ IP ,cụ thể đây là IPV4
    # - Tham số thứ hai nhận vào cho biết loại socket  là TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tao socket

    localhost = input('Enter localhost : ')
    port = int(input('Enter port : '))
    server_address = (localhost, port)

    try:
        # kết nối đến server ,có thể văng ra ngoại lệ nếu địa chỉ không hợp lệ
        client_socket.connect(server_address)

        """
        tạo một thread để thực thi hàm handle_server để xử lý dữ liệu nhận được từ server
         - target là một đối tượng gọi lại (callable) mà đối tượng Thread này sẽ thực hiện
           khi bắt đầu chạy ,cụ thể đối tượng đây là "handle_server"
         - args là một bộ sưu tập các tham số vị trí mà callable sẽ được gọi với.
        '   Đây là một tuple trống mặc định ,cụ thể nhận vào 1 tuple đơn chứa một tham số client_socket
        """
        t = threading.Thread(target=handle_server, args=(client_socket,))

        t.start()  # bắt đầu thực thi Thread mới tương ứng
        threads.append(t)  # thêm luồng vào list threads

        # lặp vô hạn để đọc dữ liệu nhập từ bàn phím và gửi đến server thông qua socket
        while True:
            """"
            input() là 1 hàm tich hợp trong python ,dùng để nhập dữ liệu từ bàn phím ,
               ở đây là gủi qua server
               lưu vào biến msg 
               sẽ check 3 trường hợp : msg muốn đóng, msg không hợp lệ,msg hợp lệ
            """
            msg = input()

            # nếu dữ liệu từ bàn phím là quit hay exit ,thì đóng client
            if msg in ['quit', 'exit']:
                print('Client closed .... !')  # thông báo ra màn hình rằng client đóng
                client_socket.sendall(msg.encode())  # gửi yêu cầu đóng qua server
                client_socket.close()  # đóng kết nối
                break  # kết thúc
            elif msg:  # nếu không có yêu cầu đóng kết nối và hợp lệ
                # gửi dữ liệu qua server dưới dạng bytes ,thông qua hàm encode()
                client_socket.sendall(msg.encode())
            else:  # nếu dữ liệu không hợp lệ ,ví dụ như nhập dấu cách ,khoảng trắng ....
                print('Invalid message! Please try again...')  # thông báo ra màn hình ..


    except ConnectionRefusedError:  # ngoại lệ ,địa chỉ server không tồn tại
        print('Invalid server! Please try again...')  # thông báo ra màn hình
    except BrokenPipeError:  # ngoại lệ bên server ,giả dụ server đóng đột ngột
        print('Server closed the connection ..!')  # thông báo
        client_socket.close()  # đóng kết noois

    """"
    Duyệt hết luồng trong list threads
    đóng tất cả các luồng
    đảm bảo khi chương trình kết thúc ,không còn luồng nào hoạt động ngầm hay là treo ...
    """
    for t in threads:
        t.join()
