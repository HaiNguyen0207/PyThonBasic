import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin tài khoản email của bạn
email ='kythuatlaptrinhl07@gmail.com'
password = 'qaz12345@'

# Thông tin email người nhận
to_email ='kythuatlaptrinhl07@gmail.com'
subject = 'Test email'
body = 'This is a test email sent from Python.'

# Tạo đối tượng MIMEMultipart và thiết lập thông tin email
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = subject

# Thêm nội dung email
msg.attach(MIMEText(body, 'plain'))

# Khởi tạo kết nối SMTP và đăng nhập vào tài khoản email của bạn
server = smtplib.SMTP('smtp.gmail.com', 535)
server.starttls()
server.login(email, password)

# Gửi email
text = msg.as_string()
server.sendmail(email, to_email, text)

# Đóng kết nối SMTP
server.quit()