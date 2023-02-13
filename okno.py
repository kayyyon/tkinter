from tkinter import *


def clicked():
    lbl.configure(text=":)", bg = "pink")


window = Tk()
window.title("это window - окно :)")
window.geometry('400x400')
window.configure(bg='pink')
lbl = Label(window, text="Привет",bg = "pink", font=("TkSmallCaptionFont", 30))
lbl.grid(column=0, row=0)
btn = Button(window, text="нажми", command=clicked, bg = "white")
btn.grid(column=1, row=0)
window.mainloop()