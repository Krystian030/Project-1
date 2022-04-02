from tkinter import *
from Grid import Grid

root = Tk()
root.title("Path")
root.geometry("800x600")

b = Grid(root, 800, 600)
b.displayGrid()

root.mainloop()