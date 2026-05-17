from tkinter import *
import random

window = Tk()

window.title("HangMan Game")
window.geometry("1000x600")

icon = PhotoImage(file='photo/OIP.png')
window.iconphoto(True, icon)
window.config(bg="#2C2C2C")

imghow=PhotoImage(file='photo/htp.png')
imghow = imghow.subsample(2, 2)
img_label3 = Label(window, image=imghow, bg='#2C2C2C')
img_label3.place(relx=0.5, rely=0.49, anchor="center")

window.mainloop() 