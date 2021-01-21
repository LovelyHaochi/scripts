# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import yaml
import requests
import socket

clash_sub_link = input("Clash Sub Link >> ")
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}
headers = {
    'User-Agent': 'ClashforWindows/Clash-sub-get-ip'
}


def get_ip(domain):
    addr = socket.getaddrinfo(domain, 'http')
    return addr[0][4][0]


y = yaml.load((requests.get(clash_sub_link, proxies=proxies, headers=headers)).text, Loader=yaml.FullLoader)
print(y)
if y['proxies']:
    for num in y['proxies']:
        print(get_ip(num['server']))
else:
    for num in y['Proxy']:
        print(get_ip(num['server']))
