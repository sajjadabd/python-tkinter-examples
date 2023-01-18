# Python program to create a table

from tkinter import *


class Table:
	
	def __init__(self,root):
		
		# code for creating table
		for i in range(total_rows):
			for j in range(total_columns):
				
				self.e = Entry(
                root,
                width=10,
                bg='#333',
                fg='white',
                font=('Shabnam',16,'bold'),
                justify='right'
                )
				
				self.e.grid(row=i, column=j)
				self.e.insert(END ,  lst[i][j])

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
root.resizable(0, 0)

root.mainloop()
