# Python program to create a table

from tkinter import *

backgroundColor = '#222'

class Table:
    global backgroundColor
    def __init__(self,root):
        for i in range(total_rows):
            for j in range(total_columns):
                if i%2 == 0 :
                    backgroundColor = '#111'
                else : 
                    backgroundColor = '#333'
                self.e = Label(root, width=10, bg=backgroundColor,
                fg='white',font=('Shabnam',16,'bold'),
                justify='right',pady=10, cursor='hand2')
                self.e.grid(row=i, column=j)
                self.e.config(text= lst[i][j] )
                
"""
cursors =[
        "arrow",
        "circle",
        "clock",
        "cross",
        "dotbox",
        "exchange",
        "fleur",
        "heart",
        "man",
        "mouse",
        "pirate",
        "plus",
        "shuttle",
        "sizing",
        "spider",
        "spraycan",
        "star",
        "target",
        "tcross",
        "trek"
]

"""

# take the data
lst = [(1,'آرش','تهران',19),
	(2,'کاوه','ساری',18),
	(3,'فریدون','یزد',20),
	(4,'سهراب','تبریز',21),
	(5,'زال','سنندج',21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.resizable(0 , 0)
root.mainloop()
