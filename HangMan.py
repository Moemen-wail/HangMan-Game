import random 

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
    "chocolate", "fried chicken", "fries","apple pie",
    "meat loaf", "chicken wings", "hotdog","salmon",
    "fish and chips"
]
instruments_word_list = [
    "electric guitar", "organ", "harmonica", "guitar",
    "piano", "violin", "drums", "flute",
    "trumpet", "saxophone", "cello", "harp",
    "clarinet","recorderguitar"
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


category= input("choose the number of the category you want to play"+
"\n1. IT\n2. Animals\n3. Countries\n4. Food\n5. Instruments"+
"\n6. Superheroes\n7. Makeup\n8. Space\n9. Underwater World"+
"\n10. Musicians\n11. Colors\n12. How to Play\n\nEnter your choice: ")


lives = 6
hint = 1

if category == "1":
    chosen_word = random.choice(IT_word_list)
elif category == "2":
    chosen_word = random.choice(Animals_word_list)
elif category == "3":
    chosen_word = random.choice(countries_word_list)
elif category == "4":
    chosen_word = random.choice(food_word_list)
elif category == "5":
    chosen_word = random.choice(instruments_word_list)
elif category == "6":
    chosen_word = random.choice(superheroes_word_list)
elif category == "7":
    chosen_word = random.choice(makeup_word_list)
elif category == "8":
    chosen_word = random.choice(space_word_list)
elif category == "9":
    chosen_word = random.choice(underwater_world_list)
elif category == "10":
    chosen_word = random.choice(musicians_word_list)
elif category == "11":
    chosen_word = random.choice(colors_word_list)    
elif category == "12":
    chosen_word = random.choice(how_to_play_list)



placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []
if (" ") in chosen_word:
    correct_letters.append(" ")

while not game_over:
    while True:
        guess = input("guess a letter: ").lower()

        if guess == "?":
            if hint == 1:
                hidden_letters = [letter for letter in chosen_word if letter not in correct_letters]
                hint_letter = random.choice(hidden_letters)
                correct_letters.append(hint_letter)   
                hint = 0
                break
            else:
                print("No hints left.")
                continue
        elif len(guess) == 1 and guess.isalpha():
            break
        else:
            print("BRO enter ONE letter only 😑")

    display = ""

    if guess not in correct_letters:
        correct_letters.append(guess)

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    

        

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")

    if "_" not in display:
        game_over = True
        print("you win <3")

    print(stages[lives])