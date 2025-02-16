from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, title
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps, timer

    #Format 10:00 = 10 Minutes
    #Format 9:45 = 9m 45s

    minutes = math.floor(count / 60)
    seconds = str(round(count % 60, 2)).zfill(2)
    canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        checkmark.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# --- Canvas Creation --- #
canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',
                   font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

# --- Timer --- #
timer_label = Label(text='Timer', fg = GREEN, bg = YELLOW,
                    font=(FONT_NAME, 48, "bold"))
timer_label.grid(column=1, row = 0)

# --- Reset --- #
reset_button = Button(text="Reset", bg = RED, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# --- Start --- #
start_button = Button(text="Start", bg = GREEN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# --- Checkmark --- #

checkmark = Label(fg = GREEN, bg = YELLOW,
                    font=(FONT_NAME, 24, "bold"))
checkmark.grid(column=1, row = 3)

# ----- Last Line of Code ----- #
window.mainloop()
