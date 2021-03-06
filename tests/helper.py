import os
from scrapy.http import Request, TextResponse

"""
    This function creates a Scrapy fake HTTP response from a given local html file and returns it
"""


def fake_response(file_name=None, url=None):
    if not url:  # not None -> True
        url = 'http://www.example.com'

    request = Request(url=url)
    if file_name:
        if not file_name[0] == '/':
            responses_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(responses_dir, file_name)
        else:
            file_path = file_name

        with open(file_path, 'r') as f:
            file_content = f.read()
    else:
        file_content = ''

    response = TextResponse(url=url, request=request, body=file_content,
                            encoding='utf-8')
    return response


"""
    This function takes an argument according to which it returns a list of URLS that have been extracted
    from the local html files. 
"""


def generate_urls(value):
    if value == 1:
        urls = ["https://pypi.org/project/nnabla/",
                "https://pypi.org/project/reacnetgenerator/",
                "https://pypi.org/project/landlab/",
                "https://pypi.org/project/large-image-tasks/",
                "https://pypi.org/project/moderngl/",
                "https://pypi.org/project/ocrmypdf/",
                "https://pypi.org/project/obspy/",
                "https://pypi.org/project/ontobio/",
                "https://pypi.org/project/geocoder/",
                "https://pypi.org/project/klio/",
                "https://pypi.org/project/klio-core/",
                "https://pypi.org/project/onnxruntime/",
                "https://pypi.org/project/jiminy-py/",
                "https://pypi.org/project/klio-exec/",
                "https://pypi.org/project/pymannkendall/",
                "https://pypi.org/project/jina/",
                "https://pypi.org/project/python-opensesame/",
                "https://pypi.org/project/bohrium-api/",
                "https://pypi.org/project/pytrip98/",
                "https://pypi.org/project/pytorch-transformers-pvt-nightly/"]
    else:
        urls = ["https://packagist.org/packages/symfony/polyfill-mbstring",
                "https://packagist.org/packages/symfony/polyfill-ctype",
                "https://packagist.org/packages/psr/log",
                "https://packagist.org/packages/psr/container",
                "https://packagist.org/packages/symfony/console",
                "https://packagist.org/packages/guzzlehttp/psr7",
                "https://packagist.org/packages/webmozart/assert",
                "https://packagist.org/packages/guzzlehttp/promises",
                "https://packagist.org/packages/symfony/polyfill-intl-normalizer",
                "https://packagist.org/packages/psr/http-message",
                "https://packagist.org/packages/symfony/finder",
                "https://packagist.org/packages/symfony/polyfill-php80",
                "https://packagist.org/packages/guzzlehttp/guzzle",
                "https://packagist.org/packages/doctrine/instantiator",
                "https://packagist.org/packages/symfony/polyfill-php72"]

    return urls


"""
    This function returns the required data for the pypi site
"""
def generate_pypi():

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

    return start_urls, package_names, package_versions, package_urls,package_descriptions, url_initial, next_page_url, next_index, next_page_url_text, next_button

"""
    This function returns the required data for the packagist site
"""

def generate_packagist():
    start_urls = ["https://packagist.org/explore/popular"]
    package_names = "//ul[contains(@class,'packages list-unstyled')]/li//a/text()"
    package_versions = ""
    package_urls = "//ul[contains(@class,'packages list-unstyled')]/li//@href"
    package_descriptions = "//ul[contains(@class,'packages list-unstyled')]/li//div[contains(@class,'col-sm-9 col-lg-10')]/p[2]/text()"
    url_initial = "https://packagist.org"
    next_page_url = "//a[contains(@rel,'next')]/@href"
    next_index = 0
    next_page_url_text = "//a[contains(@rel,'next')]/text()"
    next_button = "Next ???"

    return start_urls, package_names, package_versions, package_urls,package_descriptions, url_initial, next_page_url, next_index, next_page_url_text, next_button
