import json
from multiprocessing import Pool
import requests
import re
import json
import time
import sys
import signal
import os
import random
# proxies = [
#     {'https': '101.132.122.230:3128'},
#     {'https': '114.215.95.188:3128'},
#     {'https': '117.85.84.103:53128'},
#     {'https': '119.251.244.131:8080'},
#     {'https': '123.245.56.5: 8118'},
#     {'https': '106.56.102.95:8070'},
#     {'https': '119.188.94.145:80'},
#     {'https': '223.93.172.248:3128'},
#     {'https': '114.215.95.188:3128'},
#     {'https': '101.37.79.125:3128'},
#     {'https': '183.62.196.10:3128'},
#     {'https': '101.37.79.125:3128'},
#     {'https': '218.60.8.98:3129'},
#     {'https': '114.215.95.188:3128'},
#     {'https': '218.60.8.99:3129'},
#     {'https': '118.31.223.194:3128'},
#     {'https': '218.60.8.83:3129'},
#     {'https': '203.130.46.108:9090'},
#     {'https': '119.251.244.131:8080'},
#     {'https': '101.132.122.230:3128'},
#     {'https': '223.93.172.248:3128'},
#     {'https': '60.182.239.234:33216'},
#     {'https': '202.107.195.217:80'},
#     {'https': '222.85.39.112:808'},
#     {'https': '115.221.126.100:32713'},
#     {'https': '125.88.172.57:80'},
#     {'https': '114.113.126.83:80'},
#     {'https': '106.42.20.143:31440'},
#     {'https': '106.56.102.95:8070'},
#     {'https': '106.56.102.249:8070'},
#     {'https': '180.122.149.142:26928'},
# ]
ip_info_container = dict()
proxy = {'https': '101.37.79.125:3128'}
with open('/home/austin/projects/ipsearch/countries_ip.json') as c:
    cips = list(json.loads(c.read())['CN'])
for i in cips[:10]:
    time.sleep(1)
    info = requests.get(
        'http://ip.taobao.com/service/getIpInfo.php?ip={}'.format(i)).json()
    ip_info_container[i] = info

with open('ip_info.json', 'w+') as i:
    i.write(json.dumps(ip_info_container))
# print(os.getcwd())
# with open('/home/austin/projects/ipsearch/china_ip.json') as c:
#     info = json.loads(c.read())

# for index, ip in enumerate(info):
#     print('{}:{}'.format(index, ip))
#     if index > 3950:
#         break

# try:
#     print('hello world')
#     print(sys.exit)
#     print('啊啊啊啊啊啊')
# except SystemExit:
#     print('程序退出')

# def test():
#     print('aaaaaaa', flush=True)
#     time.sleep(1)


# # ip_container = dict()
# p = Pool(4)

# for i in range(10):
#     p.apply_async(test)
# p.close()
# p.join()


# info = requests.get(
#     'http://ip.taobao.com/service/getIpInfo.php?ip=1.4.4.0', proxies=proxies, timeout=1).json()
# print(info)

# for i in range(100):
#     print(i, flush=True)
#     time.sleep(0.1)

# with open('countries_ip.json') as countries_ip:
#     ips = json.loads(countries_ip.read())
# # def a(b, c):
# #     b.append(c)

# print(ips['CN'])


# def main():
#     b = multiprocessing.Manager().list([1, 2, 3])
#     p = multiprocessing.Pool(4)
#     for i in range(4):
#         p.apply_async(a, args=(b, i))
#     p.close()
#     p.join()

#     print(b)


# if __name__ == '__main__':
#     main()


# data = requests.get(
#     'http://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest')
# pattern = re.compile(
#     r'\w+\|(\w{2})\|ipv4\|(\d+\.\d+\.\d+\.\d+)\|\d+\|\d+\|[\w, -, \|]+', re.M | re.S)

# data = pattern.findall(data.text)
# print(data)
