# By LovelyHaochi
# Github: https://github.com/LovelyHaochi/

import requests
import socket
import uuid
import time

# Config here
inviteCode = "wOSV"
address = "0x8a7164A74D7df96b727841013Cb128A13a678F13"

# Clash Proxies
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}


def fakeLogin():
    time.sleep(0.25)
    print("--------------------------------------------------")
    time.sleep(0.5)
    fakeAddress = '0x' + uuid.uuid4().hex
    print("fakeAddress: {}".format(fakeAddress))

    url = 'https://1incha.net/index.php?m=Home&c=User&a=do_login'
    data = {
        "address": fakeAddress,
        "dre": inviteCode,
    }
    print("callBack: ", end="")
    res = requests.post(url, data, proxies=proxies).json()
    print("{}".format(res['msg']), flush=True)


def extract(address):
    time.sleep(0.25)
    print("--------------------------------------------------")
    time.sleep(0.5)
    print("extracting...")
    print("address: {}".format(address))

    url = 'https://1incha.net/home/Index/extract.html'
    data = {
        "address": address,
        "value": 300,
        "user": address,
    }
    print("callBack: ", end="")
    res = requests.post(url, data, proxies=proxies).json()
    print("{}".format(res['msg']), flush=True)


def getValue(address):
    url = 'https://1incha.net/index.php?m=Home&c=User&a=do_login'
    data = {
        "address": address,
        "dre": "",
    }
    res = requests.post(url, data, proxies=proxies).json()
    return res['data']['yfiii']


while True:
    fakeLogin()
    if getValue(address) == "300":
        extract(address)
