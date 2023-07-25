import socket

host = '127.0.0.1'
port = 12000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))

print('Tin bên gửi: ')
while 1:
    mess, clientAddress = s.recvfrom(2048)
    print(mess)
    modifileMess = mess.upper()
    s.sendto(modifileMess, clientAddress)
