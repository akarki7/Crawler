# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
    This class is used to store the data that has been scraped/crawled from the given websites.
"""
class Packages(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field() -> dictionary key=name value=value

    package_url=scrapy.Field()
    package_description=scrapy.Field()
    package_name=scrapy.Field()