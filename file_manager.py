import os
import requests

def download_files(links, download_dir="downloads"):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    for link in links:
        response = requests.get(link)
        file_name = link.split('/')[-1]
        with open(f"{download_dir}/{file_name}", 'wb') as file:
            file.write(response.content)

def organize_files(download_dir="downloads"):
    categories = ['cc', 'cvv', 'login_credentials']
    for category in categories:
        category_dir = os.path.join(download_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
        # Add logic here to move files based on type
