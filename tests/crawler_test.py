import unittest
from helper import fake_response,generate_urls
import sys

sys.path.append("./..")

from Crawler.Crawler.spiders.packages_spider import PackagesPypiSpider, PackagesPackagistSpider

class CrawlerProject(unittest.TestCase):
    def setUp(self):
        self.spider = PackagesPypiSpider()
        self.spider2=PackagesPackagistSpider()

    def test_parse_Pypi(self):
        print("\n\nTesting the parser of first crawler")
        response = fake_response('test1.html')
        item = self.spider.parse(response)
        url_extracted=[]
        for x in item:
            url_extracted.append(x['package_url'])
        urls=generate_urls(1)
        with self.subTest(True):
            i=0
            self.assertEqual(len(url_extracted), len(urls))
            while i< len(url_extracted):
                self.assertEqual(url_extracted[i],urls[i])
                i+=1
    
    def test_parse_Packagist(self):
        print("\n\nTesting the parser of second crawler")
        response = fake_response('test2.html')
        item = self.spider2.parse(response)
        url_extracted=[]
        for x in item:
            url_extracted.append(x['package_url'])
        urls=generate_urls(2)
        with self.subTest(True):
            i=0
            self.assertEqual(len(url_extracted), len(urls))
            while i< len(url_extracted):
                self.assertEqual(url_extracted[i],urls[i])
                i+=1
        

if __name__ == '__main__':
    unittest.main()