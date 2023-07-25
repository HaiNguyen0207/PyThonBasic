#!/usr/bin/python
# Mô đun optparse : phân tích cú pháp và xử lý các đối số dòng lệnh
# xác định các tùy chọn và đối số được truyền vào chương trình từ dòng lệnh,
# giúp cho việc viết các ứng dụng dòng lệnh trở nên dễ dàng hơn
# ở đây đối số là domain
import optparse

# Thư viện dns.resolver là một phần của gói dnspython,
# một gói phổ biến cho phép thực hiện các hoạt động liên quan đến DNS trên Python.
# dns.resolver một thư viện Python cho phép thực hiện truy vấn DNS (Domain Name System)
# cung cấp các hàm để giải quyết các tên miền, truy vấn các bản ghi DNS và trả về thông tin DNS
import dns.resolver


# phương thức get-arguments()   sử dụng để lấy các đối số từ dòng lệnh
# lấy đối số host để kiểm tra dịch vụ
def get_arguments():
    # -d hoặc --domain được sử dụng để truyền cổng vào chương trình.
    # Nếu địa chỉ host không được cung cấp, hàm sẽ in ra thông báo lỗi tương ứng
    parser = optparse.OptionParser()  # khởi tạo 1 đối tượng
    parser.add_option('-d', '--domain', dest='domain',
                      help='Enter domain address to check ')

    options, arguments = parser.parse_args()

    if not options.domain:  # lỗi
        parser.error('[-] Please enter a valid domain address! Example: actvn.edu.vn ')  # thông báo lỗi
    return options.domain  # trả về domain


# query_dns() nhận vào hai đối số là domain (tên miền cần truy vấn)
# rrtype (loại thông tin cần truy vấn: ví dụ "A" cho IPv4 hoặc "AAAA" cho IPv6).
def query_dns(domain, rrtype):
    try:  # bắt ngoại lệ

        # thực hiện truy vấn DNS cho domain với loại thông tin được chỉ định trong rrtype[1]
        answers = dns.resolver.resolve(domain, rrtype[1])

        # duyệt qua tất cả các bản ghi DNS trả về bởi truy vấn
        for rdata in answers:
            print(f'{rrtype[0]} : {rdata}')  # in ra thông tin
    except dns.resolver.NXDOMAIN:  # ngoại lệ không tìm thấy miền truy vấn
        print("No such domain exists")
    except dns.resolver.NoAnswer:  # ngoại lệ không có bản ghi nào
        print("No {} record found for {}".format(rrtype, domain))


if __name__ == '__main__':
    # Bản ghi mail servers: response_MX
    # Bản ghi name servers: response_NS
    # Bản ghi địa chỉ IPV4: response_ipv4
    # Bản ghi địa chỉ IPV6: response_ipv6

    # list chứa cc rrtypes
    rrtypes = [['Response_IPV4 ', 'A'], ['Response_IPV6', 'AAAA'],
               ['Response_MX', 'MX'], ['Response_ND', 'NS']]
    domain = get_arguments()  # đối số domain lấy từ get_argument()
    for rrtype in rrtypes:  # duyệt
        query_dns(domain, rrtype)
