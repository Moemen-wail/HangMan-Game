from tkinter import *
import random

window = Tk()

window.title("HangMan Game")
window.geometry("1000x600")

icon = PhotoImage(file='photo/OIP.png')
window.iconphoto(True, icon)
window.config(bg="#2C2C2C")

stages = [
    r"""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    r"""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

IT_word_list = [
    "python", "keyboard", "laptop", "internet",
    "program", "developer", "operating system", "application",
    "protocol", "computer", "software", "hardware",
    "internet", "network", "database", "server",
    "coding", "algorithm", "cybersecurity"
]

Animals_word_list = [
    "leopard", "cheetah", "hyena", "wolf",
    "fox", "zebra", "rhinoceros", "lion",
    "tiger", "elephant", "giraffe", "dog",
    "cat", "horse", "bear", "beaver",
    "lizard"
]

countries_word_list = [
    "united states", "spain", "portugal", "netherlands",
    "sweden", "norway", "switzerland", "poland",
    "ukraine", "china", "south korea", "thailand",
    "france", "japan", "brazil", "canada",
    "egypt", "germany", "italy", "mexico",
    "australia", "turkey", "palestine"
]

food_word_list = [
    "sushi", "tacos", "lasagna", "steak",
    "grilled chicken", "ramen", "kebab", "falafel",
    "shawarma", "pizza", "burger", "pasta",
    "rice", "chicken", "salad", "bread",
    "chocolate", "fried chicken", "fries", "apple pie",
    "meat loaf", "chicken wings", "hotdog", "salmon",
    "fish and chips"
]

instruments_word_list = [
    "electric guitar", "organ", "harmonica", "guitar",
    "piano", "violin", "drums", "flute",
    "trumpet", "saxophone", "cello", "harp",
    "clarinet", "recorderguitar"
]

superheroes_word_list = [
    "superman", "spiderman", "batman", "ironman",
    "wonder woman", "hulk", "captain america", "antman",
    "daredevil", "thor", "doctor strange", "black widow",
    "loki", "captain marvel", "deadpool", "scarlet witch",
    "hawkeye", "flash", "aquaman"
]

makeup_word_list = [
    "foundation", "concealer", "powder", "blush",
    "bronzer", "highlighter", "mascara", "eyeliner",
    "lipstick", "lip gloss", "eye makeup", "eyeshadow",
    "eyebrow pencil", "brow gel", "eyelash curler", "false lashes",
    "glitter", "lip liner", "corrector", "contour"
]

space_word_list = [
    "planet", "galaxy", "asteroid", "comet",
    "satellite", "spaceship", "astronaut",
    "black hole", "supernova", "orbit", "meteor",
    "rocket", "moon", "star"
]

underwater_world_list = [
    "shark", "whale", "octopus", "jellyfish",
    "seahorse", "crab", "lobster", "dolphin",
    "seal", "atlantis", "starfish", "coral",
    "squid", "sea turtle"
]

musicians_word_list = [
    "britney spears", "christina aguilera", "avril lavigne", "kelly clarkson",
    "jennifer lopez", "lady gaga", "dua lipa", "lana del rey",
    "dominic fike", "chris grey", "eminem", "taylor swift",
    "drake", "beyonce", "ed sheeran", "adele",
    "the weeknd", "billie eilish", "bruno mars", "rihanna",
    "justin bieber", "michael jackson", "radiohead"
]

colors_word_list = [
    "crimson", "amber", "sapphire", "emerald",
    "charcoal", "mustard", "olive", "peach",
    "mint", "lilac", "turquoise", "burgundy",
    "lavender", "magenta", "teal", "coral",
    "indigo", "beige", "ivory", "maroon"
]


def start_game():

    button.destroy()
    img_label.destroy()

    frame = Frame(
        window,
        bg="#450011",
        padx=10,
        pady=15
    )

    frame.place(relx=0.5, rely=0.57, anchor="center")

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
        ("How to Play", "photo/hp.png")
    ]

    images = []

    row = 0
    col = 0

    for category_name, image_file in categories:

        img = PhotoImage(file=image_file)
        img = img.subsample(2, 2)

        images.append(img)

        button2 = Button(
            frame,
            image=img,
            bg="#450011",
            activebackground="#450011",
            bd=0,
            highlightthickness=0
        )

        button2.image = img
        button2.grid(row=row, column=col, padx=7, pady=3)

        col += 1

        if col == 4:
            col = 0
            row += 1

        img3 = PhotoImage(file='photo/cat.png')
        img3 = img3.subsample(3, 3)

        img_label3 = Label(window, image=img3, bg='#2C2C2C')
        img_label3.pack(pady=3)
    


button = Button(
    window,
    text='Start',
    font=('Consolas', 32, 'bold'),
    bg="#450011",
    fg='#8FAADC',
    activebackground="#8FAADC",
    activeforeground='#450011',
    command=start_game
)

img = PhotoImage(file='photo/Thee.png')
img = img.subsample(3, 3)

img_label = Label(window, image=img, bg='#2C2C2C')
img_label.pack(pady=30)

button.pack(side="bottom", pady=50)



window.mainloop()