from tkinter import *




window = Tk()

window.title("HangMan Game")
window.geometry("1000x600")

icon = PhotoImage(file='photo/OIP.png')
window.iconphoto(True, icon)
window.config(bg="#2C2C2C")

button = Button(window, text='Start',
                font=('Consolas', 32, 'bold'),
                bg="#450011", fg='#8FAADC',
                activebackground="#8FAADC", activeforeground='#450011' )

img = PhotoImage(file='photo/Thee.png')
img = img.subsample(3, 3)

img_label = Label(window, image=img, bg='#2C2C2C')
img_label.pack(pady=30)

button.pack(side="bottom", pady=50)

window.mainloop() 

