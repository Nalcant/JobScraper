import tkinter
from tkinter import Tk
from tkinter import ttk
from typing import List
from scraper import Scraper

'''
this class handles user interface
'''
class App:
    selectedURLs = [""]
    
    def __init__(self):
        #window setup
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("JobScraper")
        #job keyword
        self.keywordLabel = tkinter.Label(self.root, 
                                          text="Keyword")
        self.keywordLabel.grid(row=0, column=0)
        self.keywordEntry = tkinter.Entry(self.root)
        self.keywordEntry.grid(row=1, column=0, ipadx=80,padx=10)
        #job location
        self.localLabel = tkinter.Label(self.root, text="Local")
        self.localLabel.grid(row=0, column=1)
        self.localEntry = tkinter.Entry(self.root)
        self.localEntry.grid(row=1, column=1, ipadx=20, padx= 10)
        #exlusion keywords 
        self.exclusionLabel = tkinter.Label(self.root, text="Exclusion Keywords") 
        self.exclusionLabel.grid(row=2, column=0, ipadx= 20, padx=10)
        self.localEntry = tkinter.Entry(self.root)
        self.localEntry.grid(row=3, column=0, ipadx=80, padx= 10)
        #start button
        self.searchButtom = tkinter.Button(self.root, text = "Search", 
                                           command=self.callSearch(self.selectedURLs,
                                                                  1,2))
        self.searchButtom.grid(row=3, column=1, ipadx=20, padx= 10  )
        """  
        #minimal results
        self.minLabel = tkinter.Label(self.root, text="Min. results: ")
        self.minLabel.grid(row=4, column=0, padx=10) 
       
        #max results
        #loop 
        """
        self.root.mainloop()
    
    def callSearch(self, srcURLs = list[str], min = int, max = int) -> str: 
        if len(srcURLs) == 0:
            raise ValueError("srcURLs argument cannot be empty")
        else:
            self.scraperObj = Scraper(self.selectedURLs, min, max)
        pass


