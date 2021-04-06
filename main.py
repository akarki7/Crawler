import sys

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Crawler.Crawler.spiders.packages_spider import Packages_Crawler
from Crawler.Crawler import items


def get_settings(file_name):
    s = get_project_settings()
    s['FEEDS'] = {
        f'{file_name}.csv': {
            'format': 'csv',
            'overwrite': True
        }
    }
    s['FEED_EXPORT_FIELDS'] = ['package_name',
                               'package_description', 'package_url']
    return s


def process_pypi(s):

    start_urls = [
        "https://pypi.org/search/?q=&o=-zscore&c=Topic+%3A%3A+Scientific%2FEngineering"]

    package_names = "//h3[contains(@class,'package-snippet__title')]/span[contains(@class,'package-snippet__name')]/text()"
    package_versions = "//h3[contains(@class,'package-snippet__title')]/span[contains(@class,'package-snippet__version')]/text()"
    package_urls = "//a[contains(@class,'package-snippet')]/@href"
    package_descriptions = "//p[contains(@class,'package-snippet__description')]/text()"
    url_initial = "https://pypi.org"
    next_page_url = "//a[contains(@class,'button button-group__button')]/@href"
    next_index = -1
    next_page_url_text = "//a[contains(@class,'button button-group__button')]/text()"
    next_button = "Next"

    process = CrawlerProcess(s)
    process.crawl(Packages_Crawler, start_urls, package_names, package_versions, package_urls,
                  package_descriptions, url_initial, next_page_url, next_index, next_page_url_text, next_button)
    return process


def process_packagist(s):
    start_urls = ["https://packagist.org/explore/popular"]
    package_names = "//ul[contains(@class,'packages list-unstyled')]/li//a/text()"
    package_versions = ""
    package_urls = "//ul[contains(@class,'packages list-unstyled')]/li//@href"
    package_descriptions = "//ul[contains(@class,'packages list-unstyled')]/li//div[contains(@class,'col-sm-9 col-lg-10')]/p[2]/text()"
    url_initial = "https://packagist.org"
    next_page_url = "//a[contains(@rel,'next')]/@href"
    next_index = 0
    next_page_url_text = "//a[contains(@rel,'next')]/text()"
    next_button = "Next →"

    process = CrawlerProcess(s)
    process.crawl(Packages_Crawler, start_urls, package_names, package_versions, package_urls,
                  package_descriptions, url_initial, next_page_url, next_index, next_page_url_text, next_button)
    return process


def main():
    if sys.argv[1] == '1':
        s = get_settings('output_Pypi')
        process = process_pypi(s)
        process.start()
    elif sys.argv[1] == '2':
        s=get_settings('output_Packagist')
        process=process_packagist(s)
        process.start()
    else:
        print('1st argument must be either 1 or 2')
        return


if __name__ == '__main__':
    main()
