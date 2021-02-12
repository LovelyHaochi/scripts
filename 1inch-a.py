# By LovelyHaochi
# Github: https://github.com/LovelyHaochi/

import requests
import socket
import uuid
import time

proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}  # Clash Proxies
inviteCode = 'YourInviteCode'

count = 1
while True:
    time.sleep(0.25)
    print("--------------------------------------------------")
    time.sleep(0.5)
    fakeAddress = '0x' + uuid.uuid4().hex
    print("count: {}".format(count))
    print("fakeAddress: {}".format(fakeAddress))

    url = 'https://1incha.net/index.php?m=Home&c=User&a=do_login'
    data = {
        "address": fakeAddress,
        "dre": inviteCode,
    }
    print("callBack: ", end="")
    res = requests.post(url, data, proxies=proxies).json()
    print("{}".format(res['msg']), flush=True)
    count += 1
