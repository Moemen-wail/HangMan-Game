from tkinter import *

window = Tk()
window.title("HangMan")
window.geometry("1000x600")
window.config(bg="#2C2C2C")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

frame2 = Frame(window)
frame2.config(bg="#450011" ,
    padx=20,
    pady=20)
frame2.place(relx=0.66, rely=0.75, anchor="center")
row = 0
col = 0

for letter in letters:
    
    button = Button(
        frame2,
        text=letter,
        width=3,
        height=1,
        font=("Ink Free", 16, "bold"),  # Set the font to "Ink Free", size 14, and bold//Chiller//Curlz MT
        fg="black",
        bg="#8FAADC",
        activebackground="#012850",
        activeforeground="black"
    )

    

    button.grid(row=row, column=col, padx=3, pady=3)

    col += 1

    # move to next row every 4 buttons
    if col == 9:
        col = 0
        row += 1



img4 = PhotoImage(file='photo/Thee.png')
img4 = img4.subsample(10, 10)

img_label = Label(window, image=img4, bg='#2C2C2C')
img_label.place(relx=1.0, rely=0.0, x=-15, y=10, anchor="ne")

img5= PhotoImage(file='photo/ss.png')
img5 = img5.subsample(2, 2)

img_label2 = Label(window, image=img5, bg='#2C2C2C')
img_label2.place(relx=0.0, rely=0.0, x=5, y=10, anchor="nw")

button3 = Button(window, text='Exit',
                font=('Consolas', 12, 'bold'),
                bg="#450011", fg='#8FAADC',
                activebackground="#8FAADC", activeforeground='#450011' )
button3.place(relx=1.0, rely=1.0, x=-19, y=-10, anchor="se")





window.mainloop()