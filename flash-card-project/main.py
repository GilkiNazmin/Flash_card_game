from tkinter import *
import pandas as pd
import random

try:
    french_english_words = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_english_words = pd.read_csv("data/french_words.csv")
french_english_words = french_english_words.to_dict(orient="records")
random_card = {}


def user_knows_answer():
    french_english_words.remove(random_card)
    to_learn = pd.DataFrame(french_english_words)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    generate_french_word()


def generate_french_word():
    global random_card, flip_timer
    windows.after_cancel(flip_timer)
    canvas.itemconfig(cards_front, image=card_front)
    random_card = random.choice(french_english_words)
    canvas.itemconfig(card_text, text="French")
    canvas.itemconfig(word_text, text=random_card["French"])
    flip_timer = windows.after(3000, func=translate_to_english)


def translate_to_english():
    canvas.itemconfig(cards_front, image=card_back)
    canvas.itemconfig(card_text, text="English")
    canvas.itemconfig(word_text, text=random_card["English"])


BACKGROUND_COLOR = "#B1DDC6"
windows = Tk()
windows.title("Flashy")
flip_timer = windows.after(3000, func=translate_to_english)
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="Images/card_back.png")
cards_front = canvas.create_image(400, 263, image=card_front)
card_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
cross_img = PhotoImage(file="Images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=generate_french_word)
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="Images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=user_knows_answer)
right_button.grid(row=1, column=1)
generate_french_word()
windows.mainloop()
