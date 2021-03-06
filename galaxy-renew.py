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
