# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import yaml
import requests
import socket
import sys

# clash_sub_link = input("Clash Sub Link >> ")
clash_sub_link = sys.argv[1]
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


def main():
    y = yaml.load((requests.get(clash_sub_link, proxies=proxies, headers=headers)).text, Loader=yaml.FullLoader)
    # y = yaml.load((requests.get(clash_sub_link, headers=headers)).text, Loader=yaml.FullLoader)
    # print(y)

    ip = []

    if y['proxies']:
        for num in y['proxies']:
            ip.append(num['server'])
    else:
        for num in y['Proxy']:
            ip.append(num['server'])

    print('')

    print('--- Domain list ---')
    for num in ip:
        print(num)
    print('')

    print('--- IP list ---')
    for num in ip:
        print(get_ip(num))
    print('')

    repeat = {}
    print('--- Repeat list ---')
    list = ip
    lists = set(list)
    count = 0
    for item in lists:
        repeat[item] = list.count(item)
        count += list.count(item)
    repeat = sorted(repeat.items(), key=lambda item: item[1], reverse=True)
    for item in repeat:
        print("{}: {}".format(item[0], str(item[1] / count * 100)[:4] + '%'))


main()
