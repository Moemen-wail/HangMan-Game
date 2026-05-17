from tkinter import *
import random

window = Tk()

window.title("HangMan Game")
window.geometry("1000x600")

icon = PhotoImage(file='photo/OIP.png')
window.iconphoto(True, icon)
window.config(bg="#2C2C2C")

imgw= PhotoImage(file='photo/w.png')
imgw = imgw.subsample(2, 2)
img_label3 = Label(window, image=imgw, bg='#2C2C2C')
img_label3.place(relx=0.5, rely=0.32, anchor="center")

button = Button(
    window,
    text='Play again',
    font=('French Script MT', 32, 'bold'),
    bg="#450011",
    fg='#8FAADC',
    activebackground="#8FAADC",
    activeforeground='#450011'
)  
button.place(relx=0.59,rely=0.85,anchor="center")


button = Button(
    window,
    text='Exit',
    font=('Consolas', 32, 'bold'),
    bg="#450011",
    fg='#8FAADC',
    activebackground="#8FAADC",
    activeforeground='#450011'
)  
button.place( relx=0.35,rely=0.85,anchor="center")










window.mainloop() 