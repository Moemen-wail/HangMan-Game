from tkinter import *

window = Tk()
window.title("HangMan Categories")
window.geometry("1000x600")
window.config(bg="#2C2C2C")


# ---------------- FUNCTION ----------------
def choose_category(category):
    print("Chosen category:", category)


# ---------------- MAIN FRAME ----------------
frame = Frame(
    window,
    bg="#450011",
    padx=10,
    pady=15
)

frame.place(relx=0.5, rely=0.57, anchor="center")


# ---------------- CATEGORY DATA ----------------
categories = [
    ("IT", "photo/IT.png"),
    ("Animals", "photo/animals.png"),
    ("Countries", "photo/count.png"),
    ("Food", "photo/food.png"),
    ("Instruments", "photo/instr.png"),
    ("Superheroes", "photo/sh.png"),
    ("Musicians", "photo/Mus.png"),
    ("Makeup", "photo/makeup.png"),
    ("Colors", "photo/colors.png"),
    ("Space", "photo/sapce.png"),
    ("Underwater", "photo/uw.png"),
    ("How to Play","photo/hp.png")
]


# ---------------- KEEP IMAGES ----------------
images = []


# ---------------- CREATE IMAGE BUTTONS ----------------
row = 0
col = 0

for category_name, image_file in categories:

    img = PhotoImage(file=image_file)
    img = img.subsample(2, 2)

    images.append(img)

    button = Button(
        frame,
        image=img,
        bg="#450011",
        activebackground="#450011",
        bd=0,
        highlightthickness=0,
        command=lambda c=category_name: choose_category(c)
    )

    button.grid(row=row, column=col, padx=7, pady=3)

    col += 1

    if col == 4:
        col = 0
        row += 1





img2 = PhotoImage(file='photo/cat.png')
img2 = img2.subsample(3, 3)

img_label2 = Label(window, image=img2, bg='#2C2C2C')
img_label2.pack(pady=3)


window.mainloop()