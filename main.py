import socket
import requests
import re

# 내 IP
# in_addr = socket.gethostbyname(socket.gethostname())
#
# print(in_addr)

# 특정사이트에 접속한 IP
# in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# in_addr.connect(("www.google.co.kr", 443))
# print(in_addr.getsockname()[0])

# 외부 IP 확인(특정사이트와 연결된 나의 IP)
# req = requests.get("http://ipconfig.kr")
# out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
# print(out_addr)

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP : ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: " , out_addr)