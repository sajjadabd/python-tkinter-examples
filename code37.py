import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tkinter import *

def showMessage():
    messagebox.showinfo('Message title', 'Message content')

#messagebox.askquestion('Message title','Message content')
#messagebox.askyesno('Message title','Message content')
#messagebox.askyesnocancel('Message title','Message content')
#messagebox.askokcancel('Message title','Message content')
#messagebox.askretrycancel('Message title','Message content')

def close():
    window.destroy()

window = Tk()
window.title("محموله ورودی")

frame = ttk.Frame(window, padding=20)
frame.grid()
ttk.Label(frame, text="Hello World!" , font=('Tahoma',12)).grid(column=0,row=0)
#label.pack_propagate(0)
#label.pack(fill="both", expand=1)


#ttk.Label(frame, text="Hello World!").grid(column=0, row=1)
ttk.Button(frame, text="OK", command=close).grid(column=0,row=1)


#e1 = Entry(frame).grid(row=0, column=1)
#e2 = Entry(frame).grid(row=1, column=1)



window.geometry('350x100')
window.resizable(0 , 0)
#window.maxsize(350, 100)
#window.minsize(350, 100)
#Start the event loop.
window.mainloop()