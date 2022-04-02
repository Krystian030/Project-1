from tkinter import *
import os
from pathVisualisation.Grid import Grid

root = Tk()
root.geometry('1280x900+200+0')
root.title('Graph search visualisation')


# set background
bg = PhotoImage(file="..\\resources\\background.png")
bgLabel = Label(root, image=bg)
bgLabel.place(x=-5, y=0)

# set banner
banner = PhotoImage(file="..\\resources\\banner.png")
bannerLabel = Label(root,image=banner)
bannerLabel.place(x=-2,y=5)

# grid
g = Grid(root, 800, 600)

B = Button(root, text='Grid', command=g.displayGrid)
B.place(x=500, y=500)

root.mainloop()
