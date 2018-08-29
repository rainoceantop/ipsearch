import json
import requests
import os
import time

workpath = os.getcwd() + '/ipsearch/'

ip_info_container = dict()


def tryAgain(ip, ip_info_container):
    print('获取ip{}信息失败，正在尝试重新获取...'.format(ip), flush=True)
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0"
    }
    try:
        # 尝试获取，如果时间超过0.5秒，返回True重新获取
        ipinfo = requests.get(url, headers=headers, timeout=1)
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
    return False


def getIpInfo(ip, ip_info_container):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0"
    }
    try:
        ipinfo = requests.get(url, headers=headers, timeout=1)
    except requests.exceptions.ConnectTimeout:
        return True
    except requests.exceptions.Timeout:
        return True

    if not ipinfo:
        # 如果无返回数据，重新请求
        while tryAgain(ip, ip_info_container):
            time.sleep(0.8)

    else:
        ipinfo = ipinfo.json()
        print('{}的信息为{}'.format(ip, ipinfo), flush=True)
        if ipinfo['code'] == 1:
            # 如果返回数据 code = 1,重新请求
            while tryAgain(ip, ip_info_container):
                time.sleep(0.8)
        ip_info_container[ip] = ipinfo


def main():
    with open(workpath + 'china_ip.json') as c:
        ips = json.loads(c.read())

    ipkeys = ips.keys()
    count = len(ipkeys)
    rest_time = 0
    for index, ip in enumerate(ipkeys):
        time.sleep(0.8)
        print('({}/{})正在获取ip为{}的信息...'.format(index+1, count, ip), flush=True)
        getIpInfo(ip, ip_info_container)
        # 每获取250个ip的信息，休息60秒，防止夭折
        rest_time += 1
        if rest_time == 250:
            time.sleep(60)
            rest_time = 0

    with open(workpath + 'ip_info.json', 'w+') as i:
        i.write(json.dumps(ip_info_container))


if __name__ == '__main__':
    main()
