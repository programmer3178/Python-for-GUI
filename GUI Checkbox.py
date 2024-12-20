from tkinter import *

from PIL import Image, ImageTk


def display():
    if x.get() == 1:
        print('I like Python')
    else:
        print("I don't like Python")


window = Tk()
x = IntVar()

window.geometry('500x500')

checkbox = Checkbutton(window, text='Python',
                       variable = x,
                       onvalue = 1,
                       offvalue = 0,
                       command = display)
checkbox.config(font=('Arial', 50, 'bold'), fg = 'sky blue', bg = 'black')
checkbox.config(activeforeground ='sky blue', activebackground = 'black', relief ='raised', bd = 10)
image = Image.open('logo.png')
my_photo = image.resize((30, 30))
photo = ImageTk.PhotoImage(my_photo)

checkbox.config(image=photo)

checkbox.pack()

window.mainloop()
