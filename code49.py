from tkinter import *

wd = Tk()
wd.config(height=500, width=500)
can = Canvas(wd, bg = 'red', height=100, width=100)
can.place(relx=0.5, rely=0.5, anchor=CENTER)

label = Label(text='text' , bg='red' , fg='black' , font=('Tahoma' , 20))
label.place(relx=0.5, rely=0.5, anchor=CENTER)

label.configure(text='Hello')

mainloop()