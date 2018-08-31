import json
import os

workpath = os.getcwd() + '/ipsearch/'

with open(workpath + 'countries_ip.json') as c:
    countries_ip = json.loads(c.read())

china_ip = countries_ip['CN']

ipphase = dict()
ipall = list()  # 记录根据长度转换的所有所有ip地址
ipfield = list()  # 记录ip域地址

for ip_item in china_ip:
    separator_index = ip_item.index(':')
    ip = ip_item[:separator_index]
    ip_part_one, ip_part_two, ip_part_three, ip_part_four = ip.split('.')
    ip_part_one, ip_part_two, ip_part_three, ip_part_four = int(
        ip_part_one), int(ip_part_two), int(ip_part_three), int(ip_part_four)

    ipall.append(ip)

    num = int(ip_item[separator_index+1:])

    for _ in range(int(num/256) - 1):
        if(ip_part_three < 255):
            ip_part_three += 1
        else:
            if(ip_part_two < 255):
                ip_part_two += 1
                ip_part_three = 0
            else:
                ip_part_one += 1
                ip_part_two = 0
                ip_part_three = 0
        new_ip = '{}.{}.{}.{}'.format(str(ip_part_one), str(
            ip_part_two), str(ip_part_three), str(ip_part_four))
        ipall.append(new_ip)

    ipphase[ip] = ipall
    ipall = list()
    ipfield.append(ip)

# 将中国所有ip地址写进文件
with open(workpath + 'china_ip.json', 'w+') as c:
    c.write(json.dumps(ipphase))

# 将中国ip域地址写进文件
with open(workpath + 'china_ip_field', 'w+') as c:
    c.write(json.dumps(ipfield))
