import requests
from bs4 import BeautifulSoup

def execute_search(dork, proxies):
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://www.google.com/search?q={dork}"
    response = requests.get(search_url, headers=headers, proxies={'http': proxies, 'https': proxies})
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
