import json
import multiprocessing
import requests
import re

with open('china_ip.json') as data:
    a = json.loads(data.read())

print(len(a))
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
