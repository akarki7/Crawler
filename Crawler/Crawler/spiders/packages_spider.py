import scrapy
from Crawler.Crawler.items import Packages
# from Crawler.items import Packages
import itertools


#Spider to Find the top 100 trending packages from PyPi site
class PackagesPypiSpider(scrapy.Spider):
    name = "PackagesPypi"  # identifies the spider; must be unique within a project

    total_pages = 0

    items = []

    start_urls = [
        "https://pypi.org/search/?q=&o=-zscore&c=Topic+%3A%3A+Scientific%2FEngineering"]

    def parse(self, response):
        package_names = response.xpath(
            "//h3[contains(@class,'package-snippet__title')]/span[contains(@class,'package-snippet__name')]/text()").extract()
        package_versions = response.xpath(
            "//h3[contains(@class,'package-snippet__title')]/span[contains(@class,'package-snippet__version')]/text()").extract()
        package_urls = response.xpath(
            "//a[contains(@class,'package-snippet')]/@href").extract()
        package_descriptions = response.xpath(
            "//p[contains(@class,'package-snippet__description')]/text()").extract()

        total_now = len(package_urls)

        if total_now+PackagesPypiSpider.total_pages > 100:
            i = 0
            while PackagesPypiSpider.total_pages+i != 100:
                item = Packages()
                url = "https://pypi.org" + package_urls[i]
                item['package_name'] = package_names[i] + package_versions[i]
                item['package_url'] = url
                item['package_description'] = package_descriptions[i]
                PackagesPypiSpider.items.append(item)
                yield item
                i += 1
            PackagesPypiSpider.total_pages += i
        else:
            PackagesPypiSpider.total_pages += total_now
            for package_name, package_version, href, package_description in zip(package_names, package_versions, package_urls, package_descriptions):
                item = Packages()
                url = "https://pypi.org" + href
                item['package_name'] = package_name + package_version
                item['package_url'] = url
                item['package_description'] = package_description
                PackagesPypiSpider.items.append(item)
                yield item

        if PackagesPypiSpider.total_pages < 100:
            next_page_url_text = response.xpath(
                "//a[contains(@class,'button button-group__button')]/text()").extract()[-1]

            if next_page_url_text == "Next":
                next_page_url = response.xpath(
                    "//a[contains(@class,'button button-group__button')]/@href").extract()[-1]
            else:
                next_page_url = None

            if next_page_url:
                next_page_url = "https://pypi.org" + next_page_url
                yield scrapy.Request(next_page_url, callback=self.parse)

#Spider to Find the top 100 popular packages from Packagist site


class PackagesPackagistSpider(scrapy.Spider):
    name = "PackagesPackagist"  # identifies the spider; must be unique within a project

    total_pages = 0

    items = []

    start_urls = [
        "https://packagist.org/explore/popular"]

    def parse(self, response):
        package_names = response.xpath(
            "//ul[contains(@class,'packages list-unstyled')]/li//a/text()").extract()
        # package_names=[]

        # for names in package_names_helper:
        #     package_names.append(names.partition('/')[2])

        #This commented part is used to just extract the package name instead of the whole module and submodule names
        #I commented this out because I was not sure which name to extract

        package_urls = response.xpath(
            "//ul[contains(@class,'packages list-unstyled')]/li//@href").extract()
        package_descriptions = response.xpath(
            "//ul[contains(@class,'packages list-unstyled')]/li//div[contains(@class,'col-sm-9 col-lg-10')]/p[2]/text()").extract()

        total_now = len(package_urls)

        if total_now+PackagesPackagistSpider.total_pages > 100:
            i = 0
            while PackagesPackagistSpider.total_pages+i != 100:
                item = Packages()
                url = "https://packagist.org" + package_urls[i]
                item['package_name'] = package_names[i]
                item['package_url'] = url
                item['package_description'] = package_descriptions[i]
                PackagesPackagistSpider.items.append(item)
                yield item
                i += 1
            PackagesPackagistSpider.total_pages += i
        else:
            PackagesPackagistSpider.total_pages += total_now
            for package_name, href, package_description in zip(package_names, package_urls, package_descriptions):
                item = Packages()
                url = "https://packagist.org" + href
                item['package_name'] = package_name
                item['package_url'] = url
                item['package_description'] = package_description
                PackagesPackagistSpider.items.append(item)
                yield item

        if PackagesPackagistSpider.total_pages < 100:
            next_page_url_text = response.xpath(
                "//a[contains(@rel,'next')]/text()").extract()[0]

            if next_page_url_text == "Next →":
                next_page_url = response.xpath(
                    "//a[contains(@rel,'next')]/@href").extract()[0]
            else:
                next_page_url = None

            if next_page_url:
                next_page_url = "https://packagist.org" + next_page_url
                yield scrapy.Request(next_page_url, callback=self.parse)
