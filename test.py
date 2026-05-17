from tkinter import *
from tkinter import messagebox
import random

window = Tk()

window.title("HangMan Game")
window.geometry("1000x600")

icon = PhotoImage(file='photo/OIP.png')
window.iconphoto(True, icon)
window.config(bg="#2C2C2C")


# ---------------- WORD LIST ----------------
IT_word_list = [
    "python", "keyboard", "laptop", "internet",
    "program", "developer", "computer", "software",
    "hardware", "network", "database", "server",
    "coding", "algorithm", "cybersecurity"
]


# ---------------- START FUNCTION ----------------
def start_game():

    # remove start screen
    button.destroy()
    img_label.destroy()

    # title
    title = Label(window,
                  text="HangMan Started!",
                  font=('Consolas', 28, 'bold'),
                  bg="#2C2C2C",
                  fg="#8FAADC")
    title.pack(pady=20)

    # choose random word
    chosen_word = random.choice(IT_word_list)

    # game variables
    lives = 6
    correct_letters = []

    if " " in chosen_word:
        correct_letters.append(" ")

    # display word
    word_label = Label(window,
                       text="_ " * len(chosen_word),
                       font=("Consolas", 32, "bold"),
                       bg="#2C2C2C",
                       fg="white")
    word_label.pack(pady=40)

    # input box
    guess_entry = Entry(window,
                        font=("Consolas", 24),
                        justify="center",
                        width=5)
    guess_entry.pack()

    # result text
    result_label = Label(window,
                         text="",
                         font=("Consolas", 20),
                         bg="#2C2C2C",
                         fg="#8FAADC")
    result_label.pack(pady=20)

    # lives label
    lives_label = Label(window,
                        text=f"Lives: {lives}",
                        font=("Consolas", 20, "bold"),
                        bg="#2C2C2C",
                        fg="red")
    lives_label.pack()

    # ---------------- GUESS FUNCTION ----------------
    def check_guess():

        nonlocal lives

        guess = guess_entry.get().lower()
        guess_entry.delete(0, END)

        if len(guess) != 1 or not guess.isalpha():
            result_label.config(text="Enter ONE letter 😑")
            return

        if guess not in correct_letters:
            correct_letters.append(guess)

        display = ""

        for letter in chosen_word:
            if letter in correct_letters:
                display += letter + " "
            else:
                display += "_ "

        word_label.config(text=display)

        if guess not in chosen_word:
            lives -= 1
            lives_label.config(text=f"Lives: {lives}")

        if "_" not in display:
         result_label.config(text="YOU WIN <3")

        if lives == 0:
         result_label.config(text=f"YOU LOSE 💀\nWord was: {chosen_word}")

    # guess button
    guess_button = Button(window,
                          text="Guess",
                          font=("Consolas", 20, "bold"),
                          bg="#450011",
                          fg="#8FAADC",
                          command=check_guess)

    guess_button.pack(pady=20)


# ---------------- START BUTTON ----------------
button = Button(window,
                text='Start',
                font=('Consolas', 32, 'bold'),
                bg="#450011",
                fg='#8FAADC',
                activebackground="#8FAADC",
                activeforeground='#450011',
                command=start_game)

img = PhotoImage(file='photo/Thee.png')
img = img.subsample(3, 3)

img_label = Label(window, image=img, bg='#2C2C2C')
img_label.pack(pady=30)

button.pack(side="bottom", pady=50)

window.mainloop()