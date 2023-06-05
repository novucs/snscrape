from snscrape.modules.twitter import TwitterProfileScraper

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

if __name__ == '__main__':
    scraper = TwitterProfileScraper("jmrousseau")
    for item in scraper.get_items():
        print(item)
