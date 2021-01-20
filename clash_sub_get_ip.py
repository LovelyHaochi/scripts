# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

import yaml
import requests

sub_link = ''
proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}

y = yaml.load((requests.get(sub_link, proxies=proxies)).text, Loader=yaml.FullLoader)
for num in y['Proxy']:
    print(num['server'])