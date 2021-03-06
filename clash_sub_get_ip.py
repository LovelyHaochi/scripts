# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import yaml
import requests
import socket
import sys

# clash_sub_link = input("Clash Sub Link >> ")
clash_sub_link = sys.argv[1] if len(sys.argv) > 1 else input("Clash Sub Link >> ")
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}
headers = {
    'User-Agent': 'ClashforWindows/Clash-sub-get-ip'
}

def get_ip(domain):
    try:
        return '{:18} ({})'.format(socket.getaddrinfo(domain, 'http')[0][4][0], domain)
    except Exception as error:
        return '{} ({})'.format(error, domain)


def main():
    # y = yaml.load((requests.get(clash_sub_link, proxies=proxies, headers=headers)).text, Loader=yaml.FullLoader)
    y = yaml.load((requests.get(clash_sub_link, headers=headers)).text, Loader=yaml.FullLoader)
    """
    print(y)
    print('')
    """

    ip = []
    ip2 = []

    proxy_name = 'proxies'
    try:
        sb = y['proxies']
    except AttributeError as e:
        proxy_name = 'Proxy'

    # print(proxy_name)

    for num in y[proxy_name]:
        ip.append(num['server'])

    print('--- Domain list ---')
    for num in ip:
        print(num)
    print('')

    print('--- IP list ---')
    for num in ip:
        print(get_ip(num))
        ip2.append(socket.getaddrinfo(num, 'http')[0][4][0])
    print('')

    repeat = {}
    print('--- Repeat list ---')
    list = ip2
    lists = set(list)
    count = 0
    for item in lists:
        repeat[item] = list.count(item)
        count += list.count(item)
    repeat = sorted(repeat.items(), key=lambda item: item[1], reverse=True)
    for item in repeat:
        print("{:18}: {}".format(item[0], str(item[1] / count * 100)[:4] + '%'))


main()
