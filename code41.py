import tkinter as tkinter
window = tkinter.Tk()

for x in range(2):
    window.columnconfigure(x, weight=2, minsize=25)
    window.rowconfigure(x, weight=1, minsize=45)
    for y in range(3):
        frameGrid = tkinter.Frame(
            master=window,
            #relief=tkinter.FLAT,
            #relief=tkinter.RAISED,
            #relief=tkinter.SUNKEN,
            relief=tkinter.RIDGE,
            borderwidth=2
        )
        frameGrid.grid(row=x, column=y, padx=7, pady=3)
        labelGrid = tkinter.Label(master=frameGrid, text=f"{x}{y}")
        labelGrid.pack()
        

window.mainloop()