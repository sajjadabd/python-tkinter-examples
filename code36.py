from tkinter import *

win= Tk()
win.geometry("700x300")

#Don't allow the screen to be resized
win.resizable(0,0)

label= Label(win, text= "Select an option", font=('Times New Roman',12))
label.pack_propagate(0)
label.pack(fill= "both",expand=1)

def quit():
   win.destroy()

#Create two buttons
b1= Button(win, text= "Continue")
b1.pack_propagate(0)
b1.pack(fill="both", expand=1)
b2= Button(win, command= quit, text= "Quit")
b2.pack_propagate(0)
b2.pack(fill="both", expand=1)

win.mainloop()