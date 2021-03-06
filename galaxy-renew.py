# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import requests
import time

username = 'lovelyhaochi@gmail.com'
passwd = '123456aa'
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}
useProxy = True
proxies = proxies if useProxy else {}

if __name__ == '__main__':
    print("--- 开始登录 ---")
    url = 'https://galaxy-cloud.link/api/v1/passport/auth/login'
    data = {
        "email": username,
        "password": passwd
    }
    res = requests.post(url, data, proxies=proxies)
    cookies = res.cookies

    print("--- 开始提交save ---")
    url = 'https://galaxy-cloud.link/api/v1/user/order/save'
    data = {
        "cycle": "onetime_price",
        "plan_id": "1"
    }
    res = requests.post(url, data, proxies=proxies, cookies=cookies).json()
    print(res)
    id = res['data']

    print("--- 开始Checkout ---")
    print("订单号: {}".format(id))
    url = 'https://galaxy-cloud.link/api/v1/user/order/checkout'
    data = {
        "trade_no": id,
        "method": "4"
    }
    res = requests.post(url, data, proxies=proxies, cookies=cookies).json()
    # print(res['data'])

    print("--- 开始更新消息 ---")
    url = 'https://api.telegram.org/bot1487564471:AAFE2wVRqwVCn7OhoCrmtMZv_PNmct9oMkc/editMessageText'
    data = {
        "chat_id": "@sharecentre",
        "message_id": "2232",
        "text": 'https://subscribe.galaxy-cloud.link/api/v1/client/subscribe?token=6c23b99c9e9b3ff3af24c5d21e63b665\n\n'
                'galaxy\n'
                '节点不多 每20分钟脚本自动重置流量\n' 
                '在账号不封&免费套餐不下架的情况下\n'
                '理论无限流量\n\n'
                '最后一次更新时间: ' + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + '\n'
                '状态: ' + ("✅ 正常" if res['data'] else "❎ 失败")
    }
    res = requests.post(url, data, proxies=proxies)
    print(res)

