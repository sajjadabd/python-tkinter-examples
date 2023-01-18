# Import the required libraries in tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from ttkthemes import ThemedStyle

#pip install ttkthemes

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of tkinter window
win.geometry("700x350")
win.title("Changing Themes")
# Create an instance of ttk Style
#style = ttk.Style()

style = ThemedStyle(win)


# Configure the theme with style
#style.theme_use('clam')
#style.theme_use('alt')
#style.theme_use('classic')
#style.theme_use('vista')
#style.theme_use('xpnative')
#style.theme_use('winnative')


#Aquativo
#Arc
#Clearlooks
#Equilux
#Keramic
#Plastik
#Radiance
#Scid themes
#Smog

#style.theme_use('Aquativo')
#style.set_theme("scidgrey")
style.set_theme("scidgrey")


# Define a function to show the message
def display_msg():
   messagebox.showinfo("Message", "You are learning Python Tkinter!")

# Add a Customized Label widget
label = Label(win, text="Hey Folks, I have a Message for You!", font=('Aerial 16'))
label.pack(pady=5)

# Add a Button widget
ttk.Button(win, text="Exit Program", command=quit).place(x=285, y=98)

win.mainloop()