import sys

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Crawler.Crawler.spiders.packages_spider import PackagesPypiSpider
from Crawler.Crawler import items


def main():
    s = get_project_settings()
    s['FEEDS'] = {
        f'output.csv': {
            'format': 'csv',
            'overwrite': True
        }
    }
    s['FEED_EXPORT_FIELDS'] = ['package_name',
                               'package_description', 'package_url']
    process = CrawlerProcess(s)

    if sys.argv[1] == '1':
        spider_cls = PackagesPypiSpider
    elif sys.argv[1] == '2':
        spider_cls = PackagesPypiSpider
    else:
        print('1st argument must be either 1 or 2')
        return
    process.crawl(spider_cls)
    process.start()  # the script will block here until the crawling is finished


if __name__ == '__main__':
    main()
