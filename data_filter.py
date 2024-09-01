from datetime import datetime

def filter_recent_data(soup):
    results = []
    current_year = str(datetime.now().year)
    for link in soup.find_all('a', href=True):
        if current_year in link.text:
            results.append(link['href'])
    return results
