from tkinter import *

list = [[0,0,0,0], [0, 0, 0, 0], [0, 0, 0, 0]]
a = len(list)     
length = 300//a 
ws = Tk()
ws.geometry("500x500")


canvas = Canvas(ws, width=500, height=500, bg="#7698A6")
canvas.pack(side=RIGHT)

for i in range(a):
    y = i * length
    for j in range(a):
        x = j * length
        canvas.create_rectangle(x, y, x+length, y+length, fill="#D97E4A")

f = Frame(ws, width=200, height=500, bg="#F23E2E")
f.pack(side=RIGHT)

ws.mainloop()