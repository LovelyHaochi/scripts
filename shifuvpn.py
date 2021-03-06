# By LovelyHaochi
# link: https://github.com/LovelyHaochi/

from gmailnator import Gmailnator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import requests

affcode = 'GUft'
apikey = '' # to 2captcha
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890',
}
useProxy = True

proxies = proxies if useProxy else {}

if __name__ == '__main__':
    Gmailnator = Gmailnator()
    gmail = Gmailnator.getEmail()
    print(gmail)

    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://shifuvpn.com/auth/register?code={}'.format(affcode))
    # time.sleep(5)
    browser.find_element_by_id("name").send_keys("默认用户组")
    time.sleep(1)
    browser.find_element_by_id("email").send_keys(gmail)
    browser.find_element_by_id("passwd").send_keys("123456aa")
    browser.find_element_by_id("repasswd").send_keys("123456aa")
    time.sleep(1)
    browser.find_element_by_id("email_verify").click()

    email_res = Gmailnator.receiveInbox()
    mail_code = re.search(r"\">(\d+)</span>", email_res).group(1)
    browser.find_element_by_id("email_code").send_keys(mail_code)

    sitekey = browser.find_element_by_class_name("g-recaptcha").get_attribute("data-sitekey")
    print(sitekey)
    res = requests.post("https://2captcha.com/in.php", {
        "key": apikey,
        "method": "userrecaptcha",
        "googlekey": sitekey,
        "pageurl": "https://shifuvpn.com/auth/register",
        "json": 1,
    }, proxies=proxies)
    rid = res.json()["request"]

    while True:
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]').click()
        except BaseException:
            time.sleep(1)
        break

    time.sleep(5)

    while True:
        res = requests.post("https://2captcha.com/res.php", {
            "key": apikey,
            "action": "get",
            "id": int(rid),
            "json": 1,
        })
        print(res.json())
        if res.json()["status"] == 1:
            token = res.json()["request"]
            break
        time.sleep(5)

    browser.execute_script('document.getElementById("g-recaptcha-response").innerHTML="{}";'.format(token))
    time.sleep(1)
    browser.find_element_by_id("register-confirm").click()

    time.sleep(3)
    browser.close()

    url = 'https://shifuvpn.com/auth/login'
    data = {
        'email': gmail,
        'passwd': '123456aa',
        'code': '',
    }
    res = requests.post(url, data, proxies=proxies)
    cookies = res.cookies

    url = 'https://shifuvpn.com/user/buy'
    data = {
        'coupon': '',
        'shop': 13,
        'autorenew': 0,
        'disableothers': 1,
    }
    res = requests.post(url, data, proxies=proxies, cookies=cookies)
    print(res.json())

    url = 'https://shifuvpn.com/user/checkin'
    res = requests.post(url, {}, proxies=proxies, cookies=cookies)
    print(res.json())

    url = 'https://shifuvpn.com/user'
    res = requests.get(url, proxies=proxies, cookies=cookies)
    link = re.search(r"oneclickImport\('clash','(.+)'\)", res.text).group(1)
    print(link)
