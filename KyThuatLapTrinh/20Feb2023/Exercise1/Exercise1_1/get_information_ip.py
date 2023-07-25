# Mô đun optparse : phân tích cú pháp và xử lý các đối số dòng lệnh
#   xác định các tùy chọn và đối số được truyền vào chương trình từ dòng lệnh
#   giúp cho việc viết các ứng dụng dòng lệnh trở nên dễ dàng hơn
import optparse

# Mô đun requests :được sử dụng để gửi các yêu cầu HTTP  và nhận các phản hồi HTTP từ máy chủ web.
# gửi các yêu cầu GET, POST, PUT, DELETE và các loại yêu cầu HTTP khác
# hữu ích khi muốn tương tác với các API hoặc trang web từ trong ứng dụng Python của mình
import requests


# Phương thức get_argument(): Phương thức này sử dụng module optparse để lấy giá trị của đối số --ip
# từ dòng lệnh khi chương trình được chạy.
# Nếu đối số này không được cung cấp,
# chương trình sẽ in ra một thông báo lỗi và dừng lại.
# Nếu đối số được cung cấp, phương thức sẽ trả về giá trị của đối số này.
def get_argument():
    # khởi tạo 1 đối tượng
    parser = optparse.OptionParser()
    # -h hoặc --host được sử dụng để truyền cổng vào chương trình.
    parser.add_option('-i', '--ip', dest='ip', help='Enter address ip to check ')
    options, arguments = parser.parse_args()  # khởi tạo 1 đối tượng
    # Nếu địa chỉ host không được cung cấp, hàm sẽ in ra thông báo lỗi tương ứng
    if not options.ip:
        parser.error('Please enter address ip valid ! Example 1.1.1.1')
    return options.ip  # trả về địa chỉ ip


# Phương thức shodan_information():
# Phương thức này sử dụng API của Shodan để lấy thông tin về địa chỉ IP được cung cấp.
# Đầu vào của phương thức bao gồm địa chỉ IP và API key của Shodan
def shodan_information(ip, shodan_api_key):
    # bắt ngoại lệ xảy ra ,ví dụ ip truyền vào không hợp lệ !
    try:
        # url của shodan lấy thông tin
        url = f'https://api.shodan.io/shodan/host/{ip}?key={shodan_api_key}'
        # sửa dụng thư viện request ,gửi yêu cầu GET
        # nhận lại  1 đối tượng response
        response = requests.get(url)
        # check trạng thái thành công ?
        if response.status_code == 200:
            # dùng json() chuyển đổi nội dung trả về thành  đối tượng JSON
            # ở đây chuyển đổi nội dung từ API của Shodan về Json
            # mục đích là dễ dàng xử lý các thông tin trong đối tượng JSON
            data = response.json()
            # data là 1 kiểu dictionary
            ip = data['ip_str']  # lấy ip
            country_name = data['country_name']  # lấy tên nước
            city = data.get('city', 'Unknown')
            hostnames = data['hostnames']  # lấy hostname
            domains = data['domains']  # lấy domain
            port = []  # list lưu trữ các cổng
            isp = data.get("isp", "Unknown")
            for e in data['data']:  # duyệt ,từng cổng có trong data
                port.append(e['port'])  # thông cổng vào list port[]
            # tạo 1 dictionary có tên result,chứa các thông tin trên
            result = {'IP': ip, 'Country_name': country_name, 'City': city, 'Hostnames': hostnames,
                      'Domains': domains, 'Port': port, 'ISP': isp}

            # đoạn dưới này in ra màn hình :v
            print(f'IP :{result["IP"]}')
            print(f'Country_name :{result["Country_name"]}')
            print(f'City : {result["City"]}')
            print(f'Hostnames :{result["Hostnames"]}')
            print(f'Domains :{result["Domains"]}')
            print(f'Ports :{result["Port"]}')
            print(f'Internet Server Provider :{result["ISP"]}')
        else:  # lỗi
            print('ERROR ! ')  # in ra mà hình
    except Exception as exception:  # nếu có ngoại lệ xảy ra
        print(f'ERROR : {exception}')  # in báo lỗi


if __name__ == '__main__':
    ip = get_argument()  # ip lấy từ đối số thông qua get_argument
    shodan_api_key = '7AAlIWIXUWCXsOvSTNHiTzhIdbAOF5dy'  # shodan api của nick em ạ
    shodan_information(ip, shodan_api_key)  # gọi phương thức shodan_information :v
