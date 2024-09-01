import logging

logging.basicConfig(filename='aidork.log', level=logging.INFO)

def log_results(links, log_file="results.log"):
    with open(log_file, 'a') as log:
        for link in links:
            log.write(f"{link}\n")
            logging.info(f"Downloaded: {link}")
