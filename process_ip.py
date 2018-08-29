import json
import os

workpath = os.getcwd() + '/ipsearch/'
# 存放国家代码
countries_code = set()
# 存放国家ip
countries_ip = dict()

with open(workpath + 'ip_address.json') as ip_address:
    data = json.loads(ip_address.read())
    before_len = len(countries_code)
    for i in data:
        countries_code.add(i[0])
        after_len = len(countries_code)
        if(after_len > before_len):
            countries_ip[i[0]] = [i[1] + ':' + i[2]]
        else:
            countries_ip[i[0]] += [i[1] + ':' + i[2]]
        before_len = after_len

with open(workpath + 'countries_ip.json', 'w+') as c:
    c.write(json.dumps(countries_ip))

print(countries_ip)
