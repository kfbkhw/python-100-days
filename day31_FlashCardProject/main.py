from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
lang_type_fr = "French"
lang_type_eng = "English"
french_word = ""
english_word = ""
turning = ""
words_set = {}

# -------------------- Save Progress -------------------- #


def update_words():
    words_list.remove(words_set)

    with open("./data/words_to_learn.csv", 'w') as file:
        new_df = pandas.DataFrame(words_list)
        file.write(pandas.DataFrame.to_csv(new_df, index=False))

    new_card()


# --------------------- Import Words -------------------- #

try:
    words_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_df = pandas.read_csv("./data/french_words.csv")
words_list = words_df.to_dict(orient="records")


def new_card():
    global french_word, english_word, turning, words_set
    words_set = words_list[random.randint(0, len(words_list)-1)]
    french_word = words_set['French']
    english_word = words_set['English']
    card.itemconfig(card_img, image=card_front_img)
    card.itemconfig(type_text, text=lang_type_fr, fill="black")
    card.itemconfig(word_text, text=french_word, fill="black")
    turning = window.after(3000, turn_card)


# --------------------- Card Turning -------------------- #


def turn_card():
    global turning
    card.itemconfig(card_img, image=card_back_img)
    card.itemconfig(type_text, text=lang_type_eng, fill="white")
    card.itemconfig(word_text, text=english_word, fill="white")
    window.after_cancel(turning)


# --------------------- UI Settings --------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = card.create_image(400, 263, image=card_front_img)
type_text = card.create_text(400, 150, text=lang_type_fr, font=LANG_FONT, fill="black")
word_text = card.create_text(400, 263, text=french_word, font=WORD_FONT, fill="black")
card.grid(column=1, row=1, columnspan=2)

new_card()

# Button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(command=update_words, image=right_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=2, row=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(command=new_card, image=wrong_image, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=2)

window.mainloop()
