from tkinter import * #Import all the Classes
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
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
 
def start_timer():
    global reps
    reps += 1
    work_sec = SHORT_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec) 
        title_label.config(text="Break", fg= RED)
    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg= PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg= GREEN)   

    # count_down(1 * 60) # multiply by 60 to turn into minute

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60) # ex: 4.8 by floor is 4
    count_sec = count % 60 # ex: 100 % 60 = 40
    if count_sec < 10: # Dynamic typing changing the variable to different datatype.
        count_sec = f"0{count_sec}"

    # to change the text on the canvas we use the itemconfig method.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # Saving in variable to use in after_cancel method
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark= ""
        work_session = math.floor(reps/2)
        for _ in range(len(work_session)):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)

""" Using Canvas method to setting up the images and text """
canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness= 0) # The height of the image file.
tomato_img = PhotoImage(file= "./pomodoro-start/tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35))
canvas.grid(column= 1, row= 1)

# Label
title_label = Label(text="Timer", fg= GREEN, bg= YELLOW, font=(FONT_NAME, 50))
title_label.grid(column= 1, row= 0)

check_marks = Label(fg= GREEN, bg=YELLOW)
check_marks.grid(column=1, row= 3)

# Buttons
start_button = Button(text= "Start", command= start_timer)
start_button.grid(column= 0, row= 2)

reset_button = Button(text= "Reset", command= reset_timer)
reset_button.grid(column= 2, row= 2)

window.mainloop()