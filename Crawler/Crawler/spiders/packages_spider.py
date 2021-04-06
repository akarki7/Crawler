import scrapy
from Crawler.Crawler.items import Packages
# from Crawler.items import Packages
import itertools


class Packages_Crawler(scrapy.Spider):
    name = "Packages"  # identifies the spider; must be unique within a project

    total_pages = 0

    items = []

    def __init__(self,start_urls="",package_names="",package_versions="",package_urls="",package_descriptions="",url_initial="",next_page_url="",next_index="",next_page_url_text="",next_button="", **kwargs):
        self.start_urls = start_urls
        self.package_name_url=package_names
        self.package_versions_url=package_versions
        self.package_urls_url=package_urls
        self.package_descriptions_url=package_descriptions
        self.url_initials=url_initial
        self.next_page_url_url=next_page_url
        self.next_index=next_index
        self.next_page_url_text=next_page_url_text
        self.next_button=next_button
        super().__init__(**kwargs)  # python3

    def parse(self, response):
        package_names = response.xpath(self.package_name_url).extract()
        if self.package_versions_url!="":
            package_versions = response.xpath(self.package_versions_url).extract()
        else:
            package_versions=""

        package_urls = response.xpath(self.package_urls_url).extract()
        package_descriptions = response.xpath(self.package_descriptions_url).extract()

        total_now = len(package_urls)

        if total_now+Packages_Crawler.total_pages > 100:
            i = 0
            while Packages_Crawler.total_pages+i != 100:
                item = Packages()
                url = self.url_initials + package_urls[i]
                if package_versions!="":
                    item['package_name'] = package_names[i] + package_versions[i]
                else:
                    item['package_name'] = package_names[i]
                item['package_url'] = url
                item['package_description'] = package_descriptions[i]
                Packages_Crawler.items.append(item)
                yield item
                i += 1
            Packages_Crawler.total_pages += i
        else:
            Packages_Crawler.total_pages += total_now
            if package_versions !="":
                for package_name, package_version, href, package_description in zip(package_names, package_versions, package_urls, package_descriptions):
                    item = Packages()
                    url = self.url_initials + href
                    item['package_name'] = package_name + package_version
                    item['package_url'] = url
                    item['package_description'] = package_description
                    Packages_Crawler.items.append(item)
                    yield item
            else:
                for package_name, href, package_description in zip(package_names, package_urls, package_descriptions):
                    item = Packages()
                    url = self.url_initials + href
                    item['package_name'] = package_name
                    item['package_url'] = url
                    item['package_description'] = package_description
                    Packages_Crawler.items.append(item)
                    yield item


        if Packages_Crawler.total_pages < 100:
            next_page_url_text = response.xpath(self.next_page_url_text).extract()[self.next_index]

            if next_page_url_text == self.next_button:
                next_page_url = response.xpath(self.next_page_url_url).extract()[self.next_index]
            else:
                next_page_url = None

            if next_page_url:
                next_page_url = self.url_initials + next_page_url
                yield scrapy.Request(next_page_url, callback=self.parse)