import json
import requests
import os
import time
import random
from multiprocessing import Pool, Manager


def tryAgain(ip, ip_info_container, proxies):
    print('获取ip{}信息失败，正在尝试重新获取...'.format(ip), flush=True)
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    proxy = random.choice(proxies)
    print('尝试用代理{}获取数据'.format(proxy))
    # headers = {
    #     'user-agent': random.choice(useragents)
    # }
    try:
        # 尝试获取，如果时间超过0.5秒，返回True重新获取
        ipinfo = requests.get(url, proxies=proxy,  timeout=0.4)
    except requests.exceptions.ConnectTimeout:
        return True
    except requests.exceptions.Timeout:
        return True

    # 如果获取的信息为None，则返回True重新获取
    if not ipinfo:
        return True
    # 如果获取的code=1,返回True重新获取
    ipinfo = ipinfo.json()
    if ipinfo['code'] == 1:
        return True
    else:
        # 一切OK，返回False退出循环
        print('{}的信息为{}'.format(ip, ipinfo), flush=True)
        ip_info_container[ip] = ipinfo
        print('目前容器的长度是：({}/8233)'.format(len(ip_info_container)), flush=True)
        return False


def getIpInfo(ip, ip_info_container, proxies):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    proxy = random.choice(proxies)
    print('尝试用代理{}获取数据'.format(proxy))
    # headers = {
    #     'user-agent': random.choice(useragents)
    # }
    print('尝试用代理{}获取数据'.format(proxy), flush=True)
    try:
        ipinfo = requests.get(url, proxies=proxy, timeout=0.8)
    except requests.exceptions.ConnectTimeout:
        return True
    except requests.exceptions.Timeout:
        return True

    if not ipinfo:
        # 如果无返回数据，重新请求
        while tryAgain(ip, ip_info_container, proxies):
            time.sleep(0.8)
            print('再来一次...', flush=True)

    else:
        ipinfo = ipinfo.json()
        print('{}的信息为{}'.format(ip, ipinfo), flush=True)
        if ipinfo['code'] == 1:
            # 如果返回数据 code = 1,重新请求
            while tryAgain(ip, ip_info_container, proxies):
                time.sleep(0.8)
                print('再来一次', flush=True)
        ip_info_container[ip] = ipinfo
        print('目前容器的长度是：({}/8233)'.format(len(ip_info_container)), flush=True)


def main():
    # 设置代理
    proxies = Manager().dict()
    proxies = [
        {'https': '101.132.122.230:3128'},
        {'https': '114.215.95.188:3128'},
        {'https': '117.85.84.103:53128'},
        {'https': '119.251.244.131:8080'},
        {'https': '123.245.56.5: 8118'},
        {'https': '106.56.102.95:8070'},
        {'https': '119.188.94.145:80'},
        {'https': '223.93.172.248:3128'},
        {'https': '114.215.95.188:3128'},
        {'https': '101.37.79.125:3128'},
        {'https': '183.62.196.10:3128'},
        {'https': '101.37.79.125:3128'},
        {'https': '218.60.8.98:3129'},
        {'https': '114.215.95.188:3128'},
        {'https': '218.60.8.99:3129'},
        {'https': '118.31.223.194:3128'},
        {'https': '218.60.8.83:3129'},
        {'https': '203.130.46.108:9090'},
        {'https': '119.251.244.131:8080'},
        {'https': '101.132.122.230:3128'},
        {'https': '223.93.172.248:3128'},
        {'https': '60.182.239.234:33216'},
        {'https': '202.107.195.217:80'},
        {'https': '222.85.39.112:808'},
        {'https': '115.221.126.100:32713'},
        {'https': '125.88.172.57:80'},
        {'https': '114.113.126.83:80'},
        {'https': '106.42.20.143:31440'},
        {'https': '106.56.102.95:8070'},
        {'https': '106.56.102.249:8070'},
        {'https': '180.122.149.142:26928'},
    ]

    # 设置headers
    # useragents = Manager().list()
    # useragents = [
    #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    #     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    #     "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    #     "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    #     "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    #     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    #     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER"
    # ]
    workpath = os.getcwd() + '/ipsearch/'
    with open(workpath + 'china_ip.json') as c:
        ips = json.loads(c.read())

    ip_info_container = Manager().dict()
    p = Pool(4)

    ipkeys = list(ips.keys())
    count = len(ipkeys)
    rest = 0
    for index, ip in enumerate(ipkeys):
        print('({}/{})正在获取ip为{}的信息...'.format(index, count, ip), flush=True)
        p.apply_async(getIpInfo, args=(ip, ip_info_container, proxies,))
        time.sleep(0.8)
        rest += 1
        if rest == 100:
            time.sleep(5)
            rest = 0
    p.close()
    p.join()

    with open(workpath + 'ip_info.json', 'w+') as i:
        i.write(json.dumps(ip_info_container))


if __name__ == '__main__':
    main()
