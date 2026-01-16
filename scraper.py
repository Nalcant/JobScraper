from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

'''
this class handles all the scraping stuff, it's 
instantiated one time per search in app.py 
'''
class Scraper:
    INDEED = "https://br.indeed.com/"
    def __init__(self, urlList = list[str], min = int, max = int):
        self.urlList = urlList
        self.min = min
        self.max = max
        self.search()

    '''
    this function directs the driver to it's respected scraper function
    it's expected to be adaptable for futere job sites
    '''
    def search(self):
        print("begining search")
        driver = webdriver.Chrome()
        for jobSite in self.urlList:
            match jobSite:
                case self.INDEED:
                    self.indeedScraping(jobSite, driver)
                
    def indeedScraping(self, url, driver):
        print("going to indeed job site")
        driver.get(url)
        pass
