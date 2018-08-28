import requests
import re
import json
from multiprocessing import Pool
from multiprocessing import Manager

# 获取ipx信息


def getIpAddress(pattern, url, data):
    content = requests.get(url)
    data += pattern.findall(content.text)


def main():
    # 正则表达式搜索国家以及ip地址
    pattern = re.compile(
        r'\w+\|(\w{2})\|ipv4\|(\d+\.\d+\.\d+\.\d+)\|(\d+)\|\d+\|[\w, -, |]+', re.M | re.S)
    # 创建进程池
    p = Pool(4)
    # url列表
    urls = list()
    # 创建共享列表
    data = Manager().list()
    ip_container = list()
    with open('ip.conf') as a:
        for line in a.readlines():
            # 去除文件中的换行符
            urls.append(line.strip('\n'))
    for url in urls:
        # 进程分配任务
        p.apply_async(getIpAddress, args=(pattern, url, data))
    p.close()
    p.join()
    # 将进程共享列表转换成python列表
    data = list(data)

    ip_container = json.dumps(data)

    with open('ip_address.json', 'w+') as ip_address:
        ip_address.write(ip_container)


if __name__ == '__main__':
    main()
