def generate_dorks(keyword):
    dorks = [
        f'inurl:"/admin" "{keyword}"',
        f'intitle:"index of" "{keyword}"',
        f'"{keyword}" ext:sql | ext:xml | ext:json',
        f'site:pastebin.com "{keyword}"',
    ]
    return dorks
