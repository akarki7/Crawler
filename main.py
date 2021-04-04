import sys

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Crawler.Crawler.spiders.packages_spider import PackagesPypiSpider, PackagesPackagistSpider
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

def process_now(s,spider_cls):
    process = CrawlerProcess(s)
    process.crawl(spider_cls)
    return process

def main():
    if sys.argv[1] == '1':
        s=get_settings('output_Pypi')
        spider_cls = PackagesPypiSpider
        process=process_now(s,spider_cls)
        process.start()

    elif sys.argv[1] == '2':
        s=get_settings('output_Packagist')
        spider_cls = PackagesPackagistSpider
        process=process_now(s,spider_cls)
        process.start()
    elif sys.argv[1] == '3':
        s1=get_settings('output_Pypi')
        spider_cls1 = PackagesPypiSpider
        process1=process_now(s1,spider_cls1)

        s2=get_settings('output_Packagist')
        spider_cls2 = PackagesPackagistSpider
        process2=process_now(s2,spider_cls2)

        process1.start()
        process2.start()
    else:
        print('1st argument must be either 1, 2 or 3')
        return


if __name__ == '__main__':
    main()
