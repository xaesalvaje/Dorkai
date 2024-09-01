from dork_generator import generate_dorks
from search_executor import execute_search
from anonymity_handler import fetch_proxies_from_github, rotate_proxy, use_tor_proxy
from file_manager import download_files, organize_files
from logger import log_results
from data_filter import filter_recent_data
import time

def main():
    # Fetch proxies from GitHub
    proxies_list = fetch_proxies_from_github()
    
    # Rotate to select one proxy
    proxies = rotate_proxy(proxies_list)
    
    # Set up Tor proxy (if needed)
    tor_proxy = use_tor_proxy()
    
    # Generate dorks
    dorks = generate_dorks("cc")
    
    for dork in dorks:
        # Execute search
        soup = execute_search(dork, proxies)
        recent_links = filter_recent_data(soup)
        
        # Download files
        download_files(recent_links)
        
        # Log results
        log_results(recent_links)
        
        # Wait to prevent rate limiting
        time.sleep(10)
    
    # Organize downloaded files
    organize_files()

if __name__ == "__main__":
    main()
