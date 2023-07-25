import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mess = input('Nhập dữ liệu : ')
s.sendto(mess.encode(), ('127.0.0.1', 12000))

modifileMess, severAddress = s.recvfrom(2048)
print(modifileMess.decode())
s.close()

host = '127.0.0.1'
port = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))

print('Tin bên gửi: ')
while 1:
    mess, clientAddress = s.recvfrom(2048)
    print(mess)
    modifileMess = mess.upper()
    s.sendto(modifileMess, clientAddress)
