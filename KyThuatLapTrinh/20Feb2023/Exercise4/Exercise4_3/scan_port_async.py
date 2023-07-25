#!/usr/bin/python3
# Mô đun nmap sử dụng để thực hiện quét mạng và kiểm tra các cổng trên
# các máy tính hoặc thiết bị khác nhau.
# Sử dụng để kiểm tra bảo mật hệ thống và phát hiện các lỗ hổng bảo mật
import nmap





# Hàm được gọi mỗi khi quá trình quét cổng trả về kết quả
def callback_result(host, scan_result):
    # In ra tên máy chủ được quét
    print(f'------------------\n{host}\n------------------')
    # Lặp qua tất cả các cổng được quét trên máy chủ
    for port in scan_result['scan'][host]['tcp']:
        # In ra trạng thái của từng cổng
        print(f"Port {port} is {scan_result['scan'][host]['tcp'][port]['state']}")

    # In một dòng trống để phân biệt giữa các kết quả quét khác nhau
    print('')


# Hàm quét cổng máy chủ bất đồng bộ
def scan_ports_async(host, ports):
    # Tạo một đối tượng quét cổng nmap
    nm = nmap.PortScannerAsync()
    # Bắt đầu quét cổng trên máy chủ được chỉ định
    # và gọi hàm callback_result() khi quá trình quét hoàn tất
    nm.scan(hosts=host, arguments=f'-p {ports}', callback=callback_result)
    # Kiểm tra xem quá trình quét cổng đã hoàn tất hay chưa
    while nm.still_scanning():
        # Nếu chưa hoàn tất, in ra thông báo "Waiting for results..."
        # và đợi cho đến khi quá trình quét cổng hoàn tất
        print("Waiting for results...")
        nm.wait(None)
        # Khi quá trình quét cổng hoàn tất, in ra thông báo "Done"
    print("Done")


if __name__ == '__main__':
    host = input('Enter domain : ')
    ports =input('Enter port :')

    scan_ports_async(host, ports)  # Gọi hàm quét cổng
