import scrapy
from Crawler.items import Packages

#Spider to Find the top 100 trending packages from PyPi site
class PackagesPypiSpider(scrapy.Spider):
    name="PackagesPypi" #identifies the spider; must be unique within a project

    total_pages=0

    start_urls=["https://pypi.org/search/?q=&o=-zscore&c=Topic+%3A%3A+Scientific%2FEngineering"]

    #this function basically parses all the URLS of the packages (from the main page) in a single page and then calls the parser_helper function as callback function to extract data from the individual page 
    def parse(self,response):
        urls=response.xpath("//a[contains(@class,'package-snippet')]/@href")
        total_now=len(urls)

        if total_now+PackagesPypiSpider.total_pages >100:
            i=0
            while PackagesPypiSpider.total_pages+i!=100:
                url="https://pypi.org" + urls[i].extract()
                yield scrapy.Request(url,callback=self.parse_helper)
                i+=1
            PackagesPypiSpider.total_pages+=i
        else:
            PackagesPypiSpider.total_pages+=total_now        
            for href in urls:
                url="https://pypi.org" + href.extract()
                yield scrapy.Request(url,callback=self.parse_helper)

        if PackagesPypiSpider.total_pages <100:
            next_page_url=response.xpath("//a[contains(@class,'button button-group__button')]/@href").extract()[-1]
            next_page_url="https://pypi.org" + next_page_url
            if next_page_url:
                yield scrapy.Request(next_page_url,callback=self.parse)
        


    def parse_helper(self,response):
        item= Packages()

        package_name= response.xpath("//h1[contains(@class,'package-header__name')]/text()").extract()[0].strip()
        package_url=response.xpath("//meta[@property='og:url']/@content").extract()
        package_description= response.xpath("//p[contains(@class,'package-description__summary')]/text()").extract()

        item['package_name']=package_name
        item['package_url']=package_url
        item['package_description']=package_description

        yield item 

        #response.xpath("//h3[contains(@class,'package-snippet__title')]/span[contains(@class,'package-snippet__name')]/text()").extract()
        #response.xpath("//a[contains(@class,'package-snippet')]/@href").extract()

        #response.xpath("//h1[contains(@class,'package-header__name')]/text()").extract()[0].strip()
        #response.xpath("//meta[@property='og:url']/@content").extract()
        #response.xpath("//p[contains(@class,'package-description__summary')]/text()").extract()
        

        #response.xpath("//a[contains(@class,'button button-group__button')]/@href").extract()[-1]