from stem import Signal
from stem.control import Controller
import random

def rotate_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    return random.choice(proxies).strip()

def use_tor_proxy():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    return {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }
