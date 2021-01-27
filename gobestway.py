# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import requests
from lxml import etree
import json
import random
import string

proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}

count = 1

while True:
    print("Count: %s" % count)

    # register #
    url = 'http://find.gobestway.org/auth/register'
    em = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    email = em + '@gmail.com'
    print('Email: %s' % email)
    data = {
        'email': email,
        'name': 'nmsl',
        'passwd': 'sbsbsbsb123',
        'repasswd': 'sbsbsbsb123',
        'wechat': email,
        'imtype': '2',
        'code': '',
    }
    res = requests.post(url, data, proxies=proxies)
    print(json.loads(res.text)['msg'])

    # login #
    url = 'http://find.gobestway.org/auth/login'
    data = {
        'email': email,
        'passwd': 'sbsbsbsb123',
        'code': '',
    }
    res = requests.post(url, data)
    # print(json.loads(res.text))
    cookies = res.cookies

    # check-in #
    # url = 'http://find.gobestway.org/user/checkin'
    # res = requests.post(url, {}, proxies=proxies, cookies=cookies)
    # print(json.loads(res.text)['msg'])

    # get links #
    url = 'http://find.gobestway.org/user'
    res = requests.get(url, proxies=proxies, cookies=cookies)
    html = etree.HTML(res.text)
    link = html.xpath('//button/@data-clipboard-text')
    # print(link[1])

    # output #
    with open('wangyiyun.txt', 'a+', encoding='utf-8')as f:
        f.write(link[1])

    # 计数哒 #
    count += 1
