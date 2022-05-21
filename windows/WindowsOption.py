from tkinter import *

# banner2 = PhotoImage(file="../resources/banner.png")

def clear_window(to_clean):
    for widget in to_clean.winfo_children():
        widget.destroy()


def set_background(root):
    background = PhotoImage(file='resources/background.png')
    bgLabel = Label(root, image=background)
    bgLabel.place(x=-5, y=0)
