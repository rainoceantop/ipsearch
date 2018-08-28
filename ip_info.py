import json
from multiprocessing import Pool, Manager
import random
import requests


def getIpInfo(ip, info_container, proxy):
    print('aaaaaaaaaaa')
    separator_index = ip.index(':')
    ip = ip[:separator_index]
    print('使用代理{}，开始获取{}的信息'.format(proxy['http'], ip))
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    print('url' + url)
    info = requests.get(url, proxies=proxy)
    print(json.loads(info))
    info_container[ip] = info


def main():
    with open('countries_ip.json') as c:
        ips = json.loads(c.read())

    p = Pool(4)

    proxies = [
        {"http": "http://180.118.247.189:9000"},
        {"http": "http://182.87.143.81:9000"},
        {"http": "http://222.73.68.144:8090"},
        {"http": "http://112.74.108.145:80"},
        {"http": "http://223.150.38.210:9000"},
        {"http": "http://115.153.173.95:9000"},
        {"http": "http://124.42.7.103:80"}
    ]
    info_container = Manager().dict()
    ips = ips['CN']
    # ip_count = len(ips)
    proxy = random.choice(proxies)
    p.apply_async(getIpInfo, args=(ips[0], info_container, proxy))

    p.close()
    p.join()

    info_container = dict(info_container)
    with open('ip_info.json', 'w+') as ip_info:
        ip_info.write(json.dumps(info_container))


if __name__ == '__main__':
    main()
