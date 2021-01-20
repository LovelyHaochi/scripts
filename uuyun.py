# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import requests
from lxml import etree
import json
import random
import string
import re

proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}

count = 1

while True:
    print("Count: %s" % count)

    # register #
    url = 'https://www.uuyun.club/auth/register'
    em = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    email = em + '@gmail.com'
    # print('email:%s' % ( email))

    data = {
        'email': email,
        'name': 'nmsl',
        'passwd': 'nmsl123456a',
        'repasswd': 'nmsl123456a',
        'wechat': email,
        'imtype': '2',
        'code': '',
    }
    res = requests.post(url, data, proxies=proxies)
    print(json.loads(res.text)['msg'])

    # login #
    url = 'https://www.uuyun.club/auth/login'
    data = {
        'email': email,
        'passwd': 'nmsl123456a',
        'code': '',
    }
    res = requests.post(url, data)
    # print(json.loads(res.text))
    cookies = res.cookies

    # check-in #
    url = 'https://www.uuyun.club/user/checkin'
    res = requests.post(url, {}, proxies=proxies, cookies=cookies)
    print(json.loads(res.text)['msg'])

    # get links #
    url = 'https://www.uuyun.club/user/node'
    res = requests.get(url, proxies=proxies, cookies=cookies)
    html = etree.HTML(res.text)
    link = re.findall(r">vmess(.*?)<", res.text)
    # print(link)

    # output #
    for link2 in link:
        # print("vmess%s" % link2)
        with open('uuyun.txt', 'a+', encoding='utf-8')as f:
            f.write("vmess%s" % link2)
            f.write('\n')

    # 计数哒 #
    count += 1
