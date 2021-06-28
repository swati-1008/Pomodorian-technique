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
reps = 1        # After 4 times of short break, take a long break
global_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(global_timer)
    canvas.itemconfig(timer_text, text = "00:00")       # Change the text of a canvas component
    timer.config(text = "TIMER", fg = GREEN)
    checkmark.config(text = "")
    global reps
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # count_down(5 * 60)
    global reps
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60
    work_sec = 5
    short_break_sec = 5
    long_break_sec = 5
    if reps % 2 == 1:
        print("Work Timer")
        timer.config(text = "WORK", fg = GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        print("Long Break")
        timer.config(text = "BREAK", fg = RED)
        count_down(long_break_sec)
    else:
        print("Short Break")
        timer.config(text = "BREAK", fg = PINK)
        count_down(short_break_sec)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global global_timer
        global_timer = window.after(1000, count_down, count - 1)       # 1000 is milliseconds -> 1 second
    else:
        start_timer()
        global reps
        checks = checkmark["text"]
        if reps % 8 == 1:
            checkmark.config(text = "")
        elif reps % 2 != 0:
            new_text = checks + "✔"
            checkmark.config(text = new_text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro Technique")
window.config(padx = 100, pady = 50, bg = YELLOW)

timer = Label(text = "TIMER", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 45, "bold"))
timer.grid(row = 0, column = 1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)     # If no highlightthickness, white border will come up around Canvas
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)       # 101 because at 100, the image was cut off a bit in left
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))      # fill means text's font colour
canvas.grid(row = 1, column = 1)

start = Button(text = "Start", bg = YELLOW, highlightthickness = 0, command = start_timer)
start.grid(row = 2, column = 0)

reset = Button(text = "Reset", bg = YELLOW, highlightthickness = 0, command = reset_timer)
reset.grid(row = 2, column = 2)

checkmark = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 25))
checkmark.grid(row = 3, column = 1)

window.mainloop()
