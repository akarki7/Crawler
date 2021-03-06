# Crawler

A simple python project that crawls two different websites and is capable to be extended easily to add new sites. The sites that have been crawled for now are:

- [Pypi site](https://pypi.org/search/?q=&o=-zscore&c=Topic+%3A%3A+Scientific%2FEngineering): Got the 100 top trending packages in the topic of Scientific Engineering.
- [Packagist site](https://packagist.org/explore/popular): Got the 100 top popular packages.

Architecture Notes
------------------
* The project is written in Python and uses [scrapy framework](https://docs.scrapy.org/en/latest/) for web scraping.


Steps to setup & start the project
---------------------------------------------
* Make sure you have python virtual env installed: `pip install virtualenv` 
* Create a virtual env in the root directory of the project: `virtualenv venv`
* Switch to the venv: `source venv/bin/activate`
* Install all the python requirements: `pip3 install -r requirements.txt`
* From the root directory run:
  * Crawl through the first website: `python3 main.py 1` 
  * Crawl through the second website: `python3 main.py 2`
* If you want to stop the virtual environment: `deactivate`

Steps to view the output
--------------------------
* Once the program is run you can view the results on:
  * For the data of first website: `output_Pypi.csv`
  * For the data of second website: `output_Packagist.csv`
  * Notes:Open the files in a spreadsheet (eg LibreOffice Calc on Linux) to see the datas in a proper table view

Steps to run the unittests
--------------------------
* From the tests directory run `python3 crawler_test.py`


Folder and File Descriptions: (only the important files are listed)
-------------------------------------------------------------------

    COMPREDICT
    ├── main.py (main file from where you pass the data and run the project)
    ├── docs
        ├── Documentation.pdf (contains the documentation of the project)
    ├── tests
        ├── crawler_test.py (main file to run unittests)
        ├── helper.py (helper function for unittests)
        ├── test1.html (contains html code needed for unittests)
        ├── test2.html (contains html code needed for unittests)
    ├── Crawler 
        ├── Crawler
           ├──spiders (folder which stores all the crawlers)
              ├──packages_spider.py (connects to the website and scraps data from it)
           ├──items.py (contains the Class definition which is used to store the crawled data)
  