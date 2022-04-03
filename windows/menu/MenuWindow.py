from tkinter import *
import os
from pathVisualisation.Grid import Grid


class MenuWindow:

    def __init__(self, root):
        self.root = root
        self.bg = PhotoImage(file="resources/background.png")
        self.banner = PhotoImage(file="resources/banner.png")
        self.createBackground()
        self.createBanner()
        self.createBtnGrid()

    # set background
    def createBackground(self):
        bgLabel = Label(self.root, image=self.bg)
        bgLabel.place(x=-5, y=0)

    # set banner
    def createBanner(self):
        bannerLabel = Label(self.root, image=self.banner)
        bannerLabel.grid(row=1,column=1)

    # grid
    def createBtnGrid(self):
        g = Grid(self.root, 800, 600)
        B = Button(self.root, text='Path sss', width=20, height=5, background="black", fg="white", command=g.displayGrid)
        B.grid(row=2, column=1)
        B2 = Button(self.root, text='Path simulation', width=20, height=5, background="black", fg="white",
                   command=g.displayGrid)
        B2.grid(row=2,column=3)
