from tkinter import *
from GridBoard import GridBoard

root = Tk()
root.title("Path")
root.geometry("1200x600")

b = GridBoard(root, 800, 600)
b.displayGridBoard()

root.mainloop()