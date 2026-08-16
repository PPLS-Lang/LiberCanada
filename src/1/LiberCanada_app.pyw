import tkinter as tk
from tkinter import ttk
import os

win = tk.Tk()
win.geometry("800x500")
photo = tk.PhotoImage(file='Liber.png')
image = tk.Label(win, image=photo)
win.iconbitmap("Icon.ico")
win.title("LiberCanada")
image.pack()

def Search():
    os.startfile("C:\\Users\\saman\\Downloads\\LiberCanada\\2\\dist\\Search.exe")

Search = tk.Button(win, text="Search", command=Search)
Search.pack()

win.mainloop()
