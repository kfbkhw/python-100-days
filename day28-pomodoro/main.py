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
    global reps, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    progress_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # for test
    # work_sec = 5
    # short_break_sec = 2
    # long_break_sec = 4

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(second):
    display_min = math.trunc(second/60)
    display_sec = second % 60
    canvas.itemconfig(timer_text, text=f"{display_min:02d}:{display_sec:02d}")
    if second > 0:
        global timer
        timer = window.after(1000, count_down, second-1)
    elif second == 0:
        if reps % 2 == 0:
            check_mark = "✔"*int(reps/2)
            progress_label.config(text=check_mark)
        if reps % 8 == 0:
            title_label.config(text="Timer", fg=GREEN)
        else:
            window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.config(padx=20, pady=10)
title_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

progress_label = Label(text="", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
progress_label.config(padx=20, pady=10)
progress_label.grid(column=2, row=4)

window.mainloop()
