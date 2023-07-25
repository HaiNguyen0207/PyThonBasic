import requests
from bs4 import BeautifulSoup


def collect_information(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    # Lấy thông tin về phiên bản
    version = soup.find("meta", attrs={"name": "version"})
    if version:
        version = version.get("content")

    # Lấy thông tin về giấy phép
    license = soup.find("meta", attrs={"name": "license"})
    if license:
        license = license.get("content")

    # Lấy thông tin về bản quyền
    copyright = soup.find("meta", attrs={"name": "copyright"})
    if copyright:
        copyright = copyright.get("content")

    # Lấy thông tin về tác giả và email
    author = soup.find("meta", attrs={"name": "author"})
    author_email = soup.find("meta", attrs={"name": "email"})
    if author:
        author = author.get("content")
    if author_email:
        author_email = author_email.get("content")

    # Lấy thông tin về URL tài liệu
    url = soup.find("link", rel="canonical")
    if url:
        url = url.get("href")

    # Lấy thông tin về tiêu đề và mô tả
    title = soup.find("title")
    description = soup.find("meta", attrs={"name": "description"})
    if title:
        title = title.text.strip()
    if description:
        description = description.get("content")

    # In kết quả
    print("Version:", version)
    print("License:", license)
    print("Copyright:", copyright)
    print("Author:", author)
    print("Author email:", author_email)
    print("URL:", url)
    print("Title:", title)
    print("Description:", description)


if __name__ == '__main__':
    domain = input("Enter domain :")
    url = 'https://' + domain
    collect_information(url)
