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
    try:
        return (socket.getaddrinfo(domain, 'http'))[0][4][0]
    except Exception as error:
        return '{} ({})'.format(error, domain)


y = yaml.load((requests.get(clash_sub_link, proxies=proxies, headers=headers)).text, Loader=yaml.FullLoader)
print(y)

print('')

print('--- Domain list ---')
if y['proxies']:
    for num in y['proxies']:
        print(num['server'])
else:
    for num in y['Proxy']:
        print(num['server'])
print('')

print('--- IP list ---')
if y['proxies']:
    for num in y['proxies']:
        print(get_ip(num['server']))
else:
    for num in y['Proxy']:
        print(get_ip(num['server']))
