from tkinter import *

count = 0


def click():
    global count
    count = count + 1
    count_label.config(text=count)


window = Tk()

button = Button(window, text='click me!')
button.config(command=click, font=('Ink Free', 50, 'bold'), bg="orange", fg="black")
button.config(activebackground='#FF0000', activeforeground='#FFA500')
image = PhotoImage(file='logo.png')
button.config(image=image, compound='top', state=ACTIVE)
count_label = Label(window, text=count, font=('Monospace', 50, 'bold'))
count_label.config(bg='white')
count_label.pack()
button.pack()

window.mainloop()
