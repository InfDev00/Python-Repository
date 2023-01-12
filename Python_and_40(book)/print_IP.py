import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.kr", 443))
print("in_IP", in_addr.getsockname()[0])

#www.google.kr에 접속하고 접속 정보를 바탕으로 IP 구하기

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' , req.text)[1]
print("out_IP: ", out_addr)

#http://ipconfig.kr을 통해서 IP 주소 가져오기