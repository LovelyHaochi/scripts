# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

from gmailnator import *
import time
import re
import requests

affcode = 'Bzl3'
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}
useProxy = True

proxies = proxies if useProxy else {}

if __name__ == '__main__':
    _Gmailnator = Gmailnator()
    gmail = _Gmailnator.getEmail()
    print(gmail)

    url = 'https://freeperson.xyz/auth/send'
    data = {
        'email': gmail
    }
    res = requests.post(url, data, proxies=proxies).json()
    print(res)
    if not res['ret'] == 1:
        # continue
        exit()

    email_res = _Gmailnator.receiveInbox()
    try:
        mail_code = re.search(r"<b>(\d+)</b>", email_res).group(1)
    except BaseException:
        # continue
        exit()
    print(mail_code)

    url = 'https://freeperson.xyz/auth/register'
    data = {
        'name': '默认用户组',
        'email': gmail,
        'passwd': '123456aa',
        'repasswd': '123456aa',
        'code': affcode,
        'emailcode': mail_code
    }
    res = requests.post(url, data, proxies=proxies)
    print(res.json())

    url = 'https://freeperson.xyz/auth/login'
    data = {
        'email': gmail,
        'passwd': '123456aa',
        'code': '',
    }
    res = requests.post(url, data, proxies=proxies)
    cookies = res.cookies
    print(res.json())

    url = 'https://freeperson.xyz/user/checkin'
    res = requests.post(url, {}, proxies=proxies, cookies=cookies)
    print(res.json())

    url = 'https://freeperson.xyz/user'
    res = requests.get(url, proxies=proxies, cookies=cookies)
    link = re.search(r"oneclickImport\('clash','(.+)'\)", res.text).group(1)
    print(link)
