
# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import requests
from lxml import etree
import json
import random
import string
import _thread
import time

proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}


def fuck(threadName):
    # count = 1
    print("*** %s 启动成功 ***" % threadName)
    while True:
        # print("[%s] Count: %s" % (threadName, count))

        # register #
        url = 'http://ggboom.site/auth/register'
        em = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        email = em + '@gmail.com'
        # print('[%s] email:%s' % (threadName, email))

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
        msg = json.loads(res.text)['msg']
        print("[%s] %s" % (threadName, msg))

        # login #
        url = 'http://ggboom.site/auth/login'
        data = {
            'email': email,
            'passwd': 'nmsl123456a',
            'code': '',
        }
        res = requests.post(url, data)
        # print(json.loads(res.text))
        cookies = res.cookies

        # check-in #
        url = 'http://ggboom.site/user/checkin'
        res = requests.post(url, {}, proxies=proxies, cookies=cookies)
        msg = json.loads(res.text)['msg']
        # print("[%s] %s" % (threadName, msg))

        # get links #
        url = 'http://ggboom.site/user'
        res = requests.get(url, proxies=proxies, cookies=cookies)
        html = etree.HTML(res.text)
        ssr = html.xpath('//button/@data-clipboard-text')
        # print(ssr[1])

        # output #
        with open('ggboom.txt', 'a+', encoding='utf-8')as f:
            f.write(ssr[1])
            # f.write('\n')

        # 计数哒 #
        # count += 1


# 创建线程
try:
    for num in range(1, 257):
        _thread.start_new_thread(fuck, ("Thread-%s" % num,))
        time.sleep(0.01)
except:
    print("Error: 无法启动线程")

while 1:
    pass
