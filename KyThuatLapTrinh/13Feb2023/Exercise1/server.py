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


# phương thức handle_client() dùng để xử lý với một client cụ thể
# tham số nhận vào client_connection là một đối tượng socket đại diện cho kết nối giữa máy chủ và client,
# tham số lient_address là một bộ địa chỉ IP và cổng của client
def handle_client(client_connection, client_address):
    try:  # bắt ngoại lệ ,nếu xảy ra

        while True:  # lặp vô hạn để xử lý hết dữ liệu bên client
            data = client_connection.recv(1024)  # nhận dữ liệu bên client ,
            # kích thước tối đa là 1024 byte
            if data:
                # check data bên client có nhu cầu đóng hay không
                if data.decode() in ['quit', 'exit']:  # nếu có
                    # hiển thị thông báo máy client nào đóng
                    print(f'Client disconnected: {client_address}')
                    client_connection.close()  # đóng
                    break  # kết thúc
                else:
                    # nếu không server sẽ gửi lại thông báo cho client
                    # để xác nhận việc nhận được dữ liệu từ client thông qua sendall()
                    print(f'Data from client {client_address}: {data.decode()}')
                    print("=============")
                    client_connection.sendall(f'Server received message from client '
                                              f'{client_address}'.encode())
            else:
                print(f'Client disconnected: {client_address}')
                client_connection.close()
                break
    except BrokenPipeError:  # xảy ra ngoại lệ BrokenPipeError thì pass(bỏ qua)
        pass


def start_server():
    threads = []  # khai báo 1 list ,lưu các luồng
    # Tạo socket của client  ,client_socket
    # - Tham số đầu tiên nhận vào là kiểu địa chỉ IP ,cụ thể đây là IPV4
    # - Tham số thứ hai nhận vào cho biết loại socket  là TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # tao dia chi
    localhost = input('Enter localhost : ')
    port = int(input('Enter port : '))
    server_address = (localhost, port)
    server_socket.bind(server_address)  # xay dung may chu server

    # Chạy server
    server_socket.listen(10)  # lang nghe ket noi toi da 10 client
    print(f'Server is running on {server_address}')  # thông báo ra màn hình

    try:  # bắt ngoại lệ ,nếu xảy ra
        while True:  # ở đây là dùng lặp vô hạn ,cho server luôn luôn mở ,xử lý nhiều client cùng luc
            # chap nhan ket noi client thông qua accpet()
            # giá trị nhận được là :
            # tham số nhận vào client_connection là một đối tượng socket đại diện cho kết nối giữa máy chủ và client,
            # tham số lient_address là một bộ địa chỉ IP và cổng của client
            client_connection, client_address = server_socket.accept()

            print(f'Client connected : {client_address}')  # thông báo máy nào kết nối

            """
            tạo một thread để thực thi hàm handle_server để xử lý dữ liệu nhận được từ server
            - target là một đối tượng gọi lại (callable) mà đối tượng Thread này sẽ thực hiện
                khi bắt đầu chạy ,cụ thể đối tượng đây là "handle_client"
            - args là một bộ sưu tập các tham số vị trí mà callable sẽ được gọi với.
                Đây là một tuple trống mặc định ,cụ thể nhận vào 1 tuple đơn chứa 2 tham số là 
                client_connection, client_address
            """
            t = threading.Thread(target=handle_client,
                                 args=(client_connection, client_address))
            threads.append(t)  # thêm vào list threads
            t.start()  # bắt đầu thực thi Thread mới tương ứng


    except KeyboardInterrupt:  # xảy ra ngoại lệ KeyboardInterrupt ,ví dụ người dùng bấm ctrl+c
        server_socket.close()  # đoóng kết nối
        print('Hmm .... Closed server !')  # thông báo
    """"
     Duyệt hết luồng trong list threads
     đóng tất cả các luồng
     đảm bảo khi chương trình kết thúc ,không còn luồng nào hoạt động ngầm hay là treo ...
     """
    for t in threads:
        t.join()


if __name__ == '__main__':
    start_server()  # gọi hàm  start_server()
