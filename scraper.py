from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

'''
this class handles all the scraping stuff, it's 
instantiated one time per search in app.py 
'''
class Scraper:
    def __init__(self, urlList = list[str], min = int, max = int):
        self.urlList = urlList
        self.min = min
        self.max = max
