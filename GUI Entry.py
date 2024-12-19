from tkinter import *

def submit():
    username = entry.get()
    print("Hello" + " " + username)

def delete():
    entry.delete(0, END)

def backspace():
   entry.delete(len(entry.get()) - 1, END)


window = Tk()

submit = Button(window, text = 'Submit', command =submit)
submit.pack(side = RIGHT)

delete = Button(window, text = 'Delete', command = delete)
delete.pack(side = RIGHT)

backspace = Button(window, text = 'Backspace', command = backspace)
backspace.pack(side = RIGHT)



entry = Entry()
entry.config(font = ('Ink Free', 50), bg = '#000000', fg = '#00FF00')
#entry.insert(10, "Hey!")
#entry.config(state = DISABLED)
entry.config(width = 30)
#entry.config(show = '.')
entry.pack()
window.mainloop()