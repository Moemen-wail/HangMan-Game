from tkinter import *
import random

window = Tk()

window.title("HangMan Game")
window.geometry("1000x600")

icon = PhotoImage(file='photo/OIP.png')
window.iconphoto(True, icon)
window.config(bg="#2C2C2C")



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
how_to_play_list = [
    "guess a letter in the word",
    "you have 6 lives",
    "each wrong guess costs a life",
    "guess the word before you run out of lives",
    "you can ask for a hint once by typing '?'"
]
#----------------- Work in progress ----------------


frame1 = Frame(window, bg="#450011", padx=10, pady=15)
frame1.place_forget()

img3 = PhotoImage(file='photo/cat.png')
img3 = img3.subsample(3, 3)
img_label3 = Label(window, image=img3, bg='#2C2C2C')
img_label3.place_forget()

#----------------- This is the code for the playing screen-----------------

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

frame2 = Frame(window)
frame2.config(bg="#450011" ,
    padx=20,
    pady=20)
frame2.place_forget()
row1 = 0
col1 = 0

keyboard_buttons = []

for letter in letters:
    
    button3 = Button( 
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

    button3.config(
        command=lambda l=letter, b=button3: letter_click(l, b)
    )

    button3.grid(row=row1, column=col1, padx=3, pady=3)

    col1 += 1

    # move to next row every 4 buttons
    if col1 == 9:
        col1 = 0
        row1 += 1

global imgh0

img4 = PhotoImage(file='photo/Thee.png')
img4 = img4.subsample(10, 10)

img_label4 = Label(window, image=img4, bg='#2C2C2C')
img_label4.place_forget()

imgh0= PhotoImage(file='photo/h0.png')
imgh0 = imgh0.subsample(2, 2)


img_label5 = Label(window, image=imgh0, bg='#2C2C2C')
img_label5.place_forget()

button4 = Button(window, text='Back to Menu',
                font=('Consolas', 12, 'bold'),
                bg="#450011", fg='#8FAADC',
                activebackground="#8FAADC", activeforeground='#450011'
                )
button4.place_forget()





def start_game():

    button.destroy()
    img_label.destroy()

    img_label3.place(relx=0.5, rely=0.1, anchor="center")
    frame1.place(relx=0.5, rely=0.57, anchor="center")



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
row = 0
col = 0
lives = 6
hint = 1
correct_letters = []
chosen_word = ""
word_label = None


# ---------------- CREATE IMAGE BUTTONS ----------------



def choose_category(category):
    frame1.place_forget()
    img_label3.place_forget()

    frame2.place(relx=0.66, rely=0.75, anchor="center")
    img_label4.place(relx=1.0, rely=0.0, x=-15, y=10, anchor="ne")
    img_label5.place(relx=0.0, rely=0.0, x=5, y=10, anchor="nw")
    button4.place(relx=1.0, rely=1.0, x=-19, y=-10, anchor="se")


    global chosen_word
    global display_word
    global word_label 
    global lives_label
    global message_label
    global hint_label
    global category_label

    if category == "IT":
        chosen_word = random.choice(IT_word_list)
    elif category == "Animals":
        chosen_word = random.choice(Animals_word_list)
    elif category == "Countries":
        chosen_word = random.choice(countries_word_list)
    elif category == "Food":
        chosen_word = random.choice(food_word_list)
    elif category == "Instruments":
        chosen_word = random.choice(instruments_word_list)
    elif category == "Superheroes":
        chosen_word = random.choice(superheroes_word_list)
    elif category == "Musicians":
        chosen_word = random.choice(musicians_word_list)
    elif category == "Makeup":
        chosen_word = random.choice(makeup_word_list)
    elif category == "Colors":
        chosen_word = random.choice(colors_word_list)
    elif category == "Space":
        chosen_word = random.choice(space_word_list)
    elif category == "Underwater":
        chosen_word = random.choice(underwater_world_list)   
    elif category == "How to Play":
        chosen_word = random.choice(how_to_play_list)

    




    if " " in chosen_word:
        correct_letters.append(" ")

    display_word = ""

    for letter in chosen_word:
        if letter == " ":
            display_word += "  "
        else:
            display_word += "_ "    

        

    # display word
    word_label = Label(window,
            text=display_word,
            font=("Consolas", 24, "bold"),
            bg="#2C2C2C",
            fg='#8FAADC')
    word_label.place( relx=0.395, rely=0.5, anchor="w")  


    lives_label = Label(window,
            text=f"Lives: {lives}",
            font=("Consolas", 20, "bold"),
            bg="#2C2C2C",
            fg='#8FAADC')
    lives_label.place( relx=0.395, rely=0.3, anchor="w")  


    hint_label = Label(window,
            text=f"Hint: {hint}",
            font=("Consolas", 20, "bold"),
            bg="#2C2C2C",
            fg='#8FAADC')
    hint_label.place( relx=0.395, rely=0.35, anchor="w")


    category_label = Label(window,
            text=f"Category: {category}",
            font=("Consolas", 20, "bold"),
            bg="#2C2C2C",
            fg='#8FAADC')
    category_label.place( relx=0.395, rely=0.25, anchor="w")

    message_label = Label(window,
            text=f"",
            font=("Consolas", 20, "bold"),
            bg="#2C2C2C",
            fg='#8FAADC')
    message_label.place( relx=0.395, rely=0.4, anchor="w")


#--------------------- This is the code for the how to play screen---------------------
    if category == "How to Play":
        frame2.place_forget()
        img_label4.place_forget()
        img_label5.place_forget()
        word_label.place_forget()
        lives_label.place_forget()
        hint_label.place_forget()
        


for category_name, image_file in categories:



    img2 = PhotoImage(file=image_file)
    img2 = img2.subsample(2, 2)

    images.append(img2)

    button1 = Button(
        frame1,
        image=img2,
        bg="#450011",
        activebackground="#450011",
        bd=0,
        highlightthickness=0,
        command=lambda c=category_name: choose_category(c)
    )

    button1.grid(row=row, column=col, padx=7, pady=3)

    col += 1

    if col == 4:
        col = 0
        row += 1
    
    

    def back_to_menu():
        global lives
        global hint
        global correct_letters

        lives = 6
        hint = 1
        correct_letters.clear()
        
        img_label5.config(image=imgh0)

        for widget in frame2.winfo_children():
            widget.config(state=NORMAL)

        frame2.place_forget()
        img_label4.place_forget()
        img_label5.place_forget()
        button4.place_forget()
        category_label.place_forget()

        word_label.place_forget()
        lives_label.place_forget()
        hint_label.place_forget()
        message_label.place_forget()

        frame1.place(relx=0.5, rely=0.57, anchor="center")
        img_label3.place(relx=0.5, rely=0.1, anchor="center")    

    button4 = Button(window, text='Back to Menu',
                font=('Consolas', 12, 'bold'),
                bg="#450011", fg='#8FAADC',
                activebackground="#8FAADC", activeforeground='#450011',
                command=back_to_menu
                )
    button4.place_forget()    

def letter_click(letter, button):

    global lives_label
    global hint_label
    global chosen_word
    global word_label
    global display_word
    global correct_letters
    global lives
    global message_label
    global hint

    button.config(state=DISABLED)

    if letter.lower() in chosen_word:

        correct_letters.append(letter.lower())

    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")


    def update_word():
        global word_label
        global chosen_word
        global correct_letters
        
        new_display = ""

        for letter in chosen_word:

            if letter in correct_letters:
                new_display += letter + " "

            elif letter == " ":
                new_display += "  "

            else:
                new_display += "_ "

        word_label.config(text=new_display)

    def disable_buttons():
        global frame2
        for widget in frame2.winfo_children():
            widget.config(state=DISABLED)

                

    

    if letter == "?":
            if hint == 1:
                hidden_letters = [letter for letter in chosen_word if letter not in correct_letters]
                hint_letter = random.choice(hidden_letters)
                if hidden_letters:
                    correct_letters.append(hint_letter)   
                hint -= 1
                hint_label.config(text=f"Hint: {hint}")
                message_label.config(text=f"Hint used!")
            else:
                message_label.config(text="No hints left")

    update_word()



    if len(letter) != 1 or not letter.isalpha() and letter != "?":
        message_label.config(text="Enter ONE letter 😑")
        return

    if letter not in correct_letters:
        correct_letters.append(letter)

    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter + " "
        else:
            display += "_ "

    word_label.config(text=display)

    if letter not in chosen_word:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")

    if "_" not in display:
        message_label.config(text="YOU WIN <3")
        disable_buttons()

    if lives == 0:
        message_label.config(text=f"YOU LOSE 💀Word was: {chosen_word}")
        disable_buttons()

    if lives == 5:
        img_label5.config(image=imgh1)
    elif lives == 4:
        img_label5.config(image=imgh2)
    elif lives == 3:
        img_label5.config(image=imgh3)
    elif lives == 2:
        img_label5.config(image=imgh4)
    elif lives == 1:
        img_label5.config(image=imgh5)
    elif lives == 0:
        img_label5.config(image=imgh6)                
        



imgh1= PhotoImage(file='photo/h1.png')
imgh1 = imgh1.subsample(2, 2)

imgh2= PhotoImage(file='photo/h2.png')
imgh2 = imgh2.subsample(2, 2)

imgh3= PhotoImage(file='photo/h3.png')
imgh3 = imgh3.subsample(2, 2)

imgh4= PhotoImage(file='photo/h4.png')
imgh4 = imgh4.subsample(2, 2)

imgh5= PhotoImage(file='photo/h5.png')
imgh5 = imgh5.subsample(2, 2)

imgh6= PhotoImage(file='photo/h6.png')
imgh6 = imgh6.subsample(2, 2)














window.mainloop()    