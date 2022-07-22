from tkinter import *
from math import *

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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def startTimer():
    global reps
    reps +=1
    workSec = WORK_MIN*60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countDown(longBreakSec)
        titleLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countDown(shortBreakSec)
        titleLabel.config(text="Break", fg=PINK)
    else:
        countDown(workSec)
        titleLabel.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    countMin = floor(count/60)
    countSec = count % 60
    if countSec < 10:
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        window.after(1000, countDown, count - 1)
    else:
        startTimer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Productivity Life Hack")
window.config(padx=100, pady=50, bg=YELLOW)

titleLabel = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
titleLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timerText = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

startButton = Button(text="Start", highlightthickness=0, command=startTimer)
startButton.grid(column=0, row=2)
resetButton = Button(text="Reset", highlightthickness=0)
resetButton.grid(column=2, row=2)

checkMarks = Label(text="✔", fg=GREEN, bg=YELLOW)
checkMarks.grid(column=1, row=3)

window.mainloop()
