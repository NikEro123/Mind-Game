from tkinter import Tk, Button, Label, Frame, Canvas, Toplevel
import random


red_nums = []
blue_nums = []
lives = 4

colors = ["red", "cyan"]

c1 = random.choice(colors)
c2 = random.choice(colors)
c3 = random.choice(colors)
c4 = random.choice(colors)



def start_game():
    start_frame.pack_forget()
    lives_label.pack(side="top", anchor="e", padx=10)
    table_frame.pack(side="top")
    button_frame.pack(side="top")

def click(button):
    color = button.cget("fg")
    num = button.cget("text")
    
    if color == "red":
        red_nums.append(num)
        draw(table1, red_nums, "red")
    else:
        blue_nums.append(num)
        draw(table2, blue_nums, "blue")

    button.pack_forget()

    if len(red_nums) + len(blue_nums) == 4:
        check_win()

def check_win():
    global lives
    red_ok = all(int(red_nums[i]) > int(red_nums[i+1]) for i in range(len(red_nums)-1))
    blue_ok = all(int(blue_nums[i]) < int(blue_nums[i+1]) for i in range(len(blue_nums)-1))

    if red_ok and blue_ok:
        show_result("You win!")
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")

        if lives == 0:
            show_result("You lost!")
        else:
            show_result("Try again!", restart_after=True)

def draw(canvas, stack, text_color):
    canvas.delete("all")
    for i, num in enumerate(stack):
        offset = i * 10
        x1 = 10 + offset
        y1 = 10 + offset
        x2 = 120 + offset
        y2 = 150 + offset
        canvas.create_rectangle(x1,y1,x2,y2, fill="black")
        canvas.create_text((x1+x2)//2, 
                           (y1+y2)//2, 
                           text=str(num), 
                           font=("Arial",18,"bold"), 
                           fill=text_color)

def restart():
    red_nums.clear()
    blue_nums.clear()

    new_nums = random.sample(range(1, 51), 4)

    button1.config(text=str(new_nums[0]), fg=c1)
    button2.config(text=str(new_nums[1]), fg=c2)
    button3.config(text=str(new_nums[2]), fg=c3)
    button4.config(text=str(new_nums[3]), fg=c4)

    button1.pack(side="left", padx=5, pady=5)
    button2.pack(side="left", padx=5, pady=5)
    button3.pack(side="left", padx=5, pady=5)
    button4.pack(side="left", padx=5, pady=5)

    table1.delete("all")
    table2.delete("all")

result_label = None
again_btn = None
leave_btn = None

def play_again():
    global lives, result_label, again_btn, leave_btn
    lives = 4
    lives_label.config(text=f"Lives: {lives}")
    result_label.destroy()
    again_btn.destroy()
    leave_btn.destroy()
    table_frame.pack(side="top")
    button_frame.pack(side="top")
    restart()


def show_result(message, restart_after=False):
    global result_label, again_btn, leave_btn
    table_frame.pack_forget()
    button_frame.pack_forget()

    result_label = Label(window, 
                         text=message, 
                         font=("Arial", 14), 
                         bg="black", fg="cyan")
    
    result_label.config(width=20, height=5)
    result_label.pack(expand=True)


    if restart_after:
        window.after(2000, lambda: [result_label.destroy(), table_frame.pack(side="top"), restart()])
        window.after(2000, lambda: [button_frame.pack(side="top"), restart()])
    else:
        again_btn = Button(window, 
                           text="Again", 
                           command=play_again, 
                           width=5, height=2)
        again_btn.config(bg="gray", 
                         fg="cyan", 
                         activebackground="gray", 
                         activeforeground="cyan")
                         
        leave_btn = Button(window, 
                           text="Leave", 
                           command=window.destroy, 
                           width=5, height=2)
        
        leave_btn.config(bg="gray", fg="cyan", 
                         activebackground="gray", 
                         activeforeground="cyan")
        again_btn.pack(side="top", pady=5)
        leave_btn.pack(side="top", pady=5)


window = Tk()
window.title("Mind")
window.config(bg="cyan")
window.geometry("500x400")

start_frame = Frame(window, bg="cyan")
start_frame.pack(expand=True)

title_label = Label(start_frame, text="The Mind", font=("Arial", 24, "bold"), bg="black", fg="cyan")
title_label.config(width=20, height=5)
title_label.pack(pady=40)

start_button = Button(start_frame, 
                      text="Play", 
                      font=("Arial", 14), 
                      command=start_game, 
                      bg="gray", fg="cyan", 
                      activebackground="gray", 
                      activeforeground="cyan", 
                      width=10, height=2)
start_button.pack()

lives_label = Label(window, 
                    text=f"Lives: {lives}", 
                    font=("Arial", 14), 
                    bg="black", fg="cyan")



table_frame = Frame(window, bg="cyan")


table1 = Canvas(table_frame, bg="red", width=190, height=190)
table1.pack(side="left")

table2 = Canvas(table_frame, bg="blue", width=190, height=190)
table2.pack(side="right")

button_frame = Frame(window, bg="cyan")

nums = random.sample(range(1, 51), 4)


button1 = Button(button_frame,
                 command=lambda: click(button1), 
                 text=str(nums[0]), 
                 width=13, height=12)

button1.config(bg="black",
               fg=c1, 
               activebackground="black", 
               activeforeground=c1)
button1.pack(side="left", padx=5, pady=5)

button2 = Button(button_frame, 
                 command=lambda: click(button2), 
                 text=str(nums[1]), 
                 width=13, height=12)

button2.config(bg="black",
               fg=c2, 
               activebackground="black", 
               activeforeground=c2)

button2.pack(side="left", padx=5, pady=5)

button3 = Button(button_frame, 
                 command=lambda: click(button3), 
                 text=str(nums[2]), 
                 width=13, height=12)
button3.config(bg="black",
               fg=c3, 
               activebackground="black", 
               activeforeground=c3)
button3.pack(side="left", padx=5, pady=5)

button4 = Button(button_frame,
                 command=lambda: click(button4), 
                 text=str(nums[3]), 
                 width=13, height=12)

button4.config(bg="black",fg=c4, 
               activebackground="black", 
               activeforeground=c4)

button4.pack(side="left", padx=5, pady=5)


window.mainloop()


def create_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

