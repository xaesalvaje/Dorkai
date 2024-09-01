import requests
import random

def fetch_proxies_from_github():
    url = 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'
    response = requests.get(url)
    if response.status_code == 200:
        proxies = response.text.splitlines()
        return [proxy.strip() for proxy in proxies if proxy.strip()]
    else:
        raise Exception("Failed to fetch proxies from GitHub")

def rotate_proxy(proxies):
    return random.choice(proxies)
