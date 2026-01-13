import tkinter
from tkinter import Tk
from tkinter import ttk

class App:
    def __init__(self):
        #window setup
        self.root = Tk()
        self.root.geometry("500x500")
        #palavra chave do cargo desejado
        self.keywordLabel = tkinter.Label(self.root, 
                                          text="Keyword")
        self.keywordLabel.grid(row=0, column=0)
        self.keywordEntry = tkinter.Entry(self.root)
        self.keywordEntry.grid(row=1, column=0, ipadx=100,padx=10)
        self.localLabel = tkinter.Label(self.root, text="Local").grid(row=0, column=1)
        self.localEntry = tkinter.Entry(self.root).grid(row=1, column=1)
        
        #loop
        self.root.mainloop()


