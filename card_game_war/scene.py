from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('700x600')
root.title('Card Game War')
root.configure(background='green')

frame = Frame(root, width=100, height= 100)
frame.grid(row=7,column=7)
root.mainloop()