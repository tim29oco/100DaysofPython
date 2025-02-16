from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# --- CSV Data --- #
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/DONT_DELETE_spanish_words.csv')
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


# --- Window Creation ---#
window = Tk()
window.title("Flashy (@_@)")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_face, image=card_front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill='black')
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill='black')
    flip_timer = window.after(1500, func=flip_card)

def flip_card():
    canvas.itemconfig(card_face, image=card_back_img)
    canvas.itemconfig(card_title, text= "English", fill='white')
    canvas.itemconfig(card_word, text= current_card["English"], fill='white')

flip_timer = window.after(1500, func=flip_card)

# --- Picture Creation --- #
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
card_face = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

language_font = ("Arial", 40, "italic")
select_word_font = ("Arial", 60, "bold")

card_title = canvas.create_text(400, 150, font=language_font)
card_word = canvas.create_text(400, 263, font=select_word_font)
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
