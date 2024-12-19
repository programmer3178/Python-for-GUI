from tkinter import *

window = Tk()
window.config(background= "#FFD700")
photo = PhotoImage(file = "logo.png")
label = Label(window,
              text="Hello World",
              font=('TimesNewRoman', 40, 'bold'),
              fg="green",
              background="black",
              relief= RAISED,
              bd= 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound= "bottom")

label.pack()

window.mainloop()
