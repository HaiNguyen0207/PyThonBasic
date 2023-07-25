#!/usr/bin/python

# Mô đun optparse : phân tích cú pháp và xử lý các đối số dòng lệnh
# xác định các tùy chọn và đối số được truyền vào chương trình từ dòng lệnh,
# giúp cho việc viết các ứng dụng dòng lệnh trở nên dễ dàng hơn
# ở đây đối số là port
import optparse
# Mô đun threading : cung cấp các đối tượng thread để quản lý các luồng
# Sử dụng 'theading' : chương trình có thể thực hiện nhiều tác vụ đồng thời,
# tăng tốc độ thực thi và cải thiện hiệu suất
# chạy đồng thời nhiều IP kiểm tra đăng nhập anonymous
import threading

# Mô đun Shodan để tìm kiếm các máy chủ FTP đăng nhập ở chế độ Anonymous.
# cung cấp các công cụ và API cho phép truy xuất thông tin của các thiết bị kết nối mạng trên toàn cầu,
# bao gồm thông tin về các port đang mở, các dịch vụ chạy trên các port này
# Sử dụng Shodan API,  tìm kiếm các thiết bị trên Internet và truy xuất thông tin về chúng
import shodan


# Phương thức get_argument(): Phương thức này sử dụng module optparse để lấy giá trị của đối số -p
# từ dòng lệnh khi chương trình được chạy.
# Nếu đối số này không được cung cấp,
# chương trình sẽ in ra một thông báo lỗi và dừng lại.
# Nếu đối số được cung cấp, phương thức sẽ trả về giá trị của đối số này.
def get_argument():
    # khởi tạo một đối tượng
    parser = optparse.OptionParser()
    # # -p hoặc --port được sử dụng để truyền cổng vào chương trình.
    parser.add_option('-p', '--port', dest='port', help='Enter address port to check !')
    options, arguments = parser.parse_args()
    if not options.port:
        parser.error('Please enter address port valid ! Example 20 ,21,80 ...')
    return options.port  # trả về địa chỉ port


# phương thức get_infor lấy thông tin về địa chỉ ip
# như tên miền,tên quốc gia,khu vực...
def get_infor(ip):
    # khi thực thi , xảy ra lỗi phát sinh
    try:
        # shodan_api.host(ip) : truy xuất thông tin về một địa chỉ IP cụ thể
        # trả về một đối tượng chứa các thông tin về địa chỉ IP đó
        host = shodan_api.host(ip)
        # in thông tin
        print(f'IP: {host["ip_str"]}, Country: {host.get("country_name", "Unknown")}, '
              f'City: {host.get("city", "Unknown")}, ISP: {host.get("isp", "Unknown")}')
    except shodan.APIError as e:  # xảy ra ngoại lệ
        print('Error:', e)  # in thông tin ngoại lệ


if __name__ == '__main__':
    # shodan api của máy em
    shodan_api_key = '7AAlIWIXUWCXsOvSTNHiTzhIdbAOF5dy'
    # khởi tạo 1 đối tượng shodan
    shodan_api = shodan.Shodan(shodan_api_key)

    port = get_argument()  # cổng lấy từ đối số ,thông qua get_argument()
    query = f'port: {port} Anonymous user logged in'  # câu lệnh truy vấn
    # sử dụng câu lệnh truy vấn trong hàm search()
    # tìm kiếm thông qua search()
    # trả về 1 đối tượng JSON()
    results = shodan_api.search(query)
    # in số lượng đã tìm được
    print(f'hosts number: {str(len(results["matches"]))}')
    # tạo 1 list chứa các tiến trình
    threads = []
    # results là 1 kiểu dictionary
    # em xét values của 'matches'
    for result in results['matches']:  # duyệt
        ip = result['ip_str']  # lấy địa chỉ ip
        if ip is not None:  # kiểm tra
            # chạy song song từng ip ,thông qua threading

            t = threading.Thread(target=get_infor, args=(ip,))
            threads.append(t)  # thêm vào list
            t.start()  # bắt đầu
    # duyệt từng cái trong list threads
    # dừng hết tiến trình
    # phòng ngừa khi chương trình kết thúc rồi mà vẫn còn tiến trình treo...
    for t in threads:
        t.join()
