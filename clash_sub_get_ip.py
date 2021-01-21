# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import yaml
import requests
import socket

clash_sub_link = ''
proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}


def get_ip(domain):
    addr = socket.getaddrinfo(domain, 'http')
    print(addr[0][4][0])


y = yaml.load((requests.get(clash_sub_link, proxies=proxies)).text, Loader=yaml.FullLoader)
for num in y['Proxy']:
    get_ip(num['server'])
