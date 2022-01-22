import turtle as t
import tkinter as tk

root = tk.Tk()
root.withdraw()
v = tk.IntVar()
x = 0
y = 0
custom = ''
toggle = 1
distance = 5
t.TurtleScreen._RUNNING = True

t.speed(0)
t.Screen().bgcolor("black")

t.color("white")
t.penup()
t.goto(-60, 0)
t.pendown()
t.goto(-60, 120)
t.goto(60, 120)
t.goto(60, 0)
t.goto(-60, 0)

t.penup()


def on_close():
    t.Screen().bye()


wn = t.Screen()
canvas = wn.getcanvas()
turtle_root = canvas.winfo_toplevel()


def popupmsg():
    global popup, v
    popup = tk.Tk()
    popup.wm_title("Controls")
    label = tk.Label(popup,
                     text=f"WASD / ARROW KEYS = Movement\n'R' = Reset Board\n'E' / SPACEBAR = Toggle Pen\n'1' - '0' = Change Movement Distance\n'C' = Change Color")
    label.pack(side="top", fill="x", pady=20, padx=80)
    B1 = tk.Button(popup, text="Start Drawing!", command=popup.destroy)
    B1.pack()


def color(v, custom):
    if custom == "":
        if v == 1:
            t.color("white")
        elif v == 2:
            t.color("blue")
        elif v == 3:
            t.color("red")
        elif v == 4:
            t.color("orange")
        elif v == 5:
            t.color("yellow")
        elif v == 6:
            t.color("pink")
    else:
        try:
            t.color(custom)
        except:
            color_select()


def color_select():
    global custom, gen, v, integer
    gen = tk.Toplevel(root)
    integer = v

    tk.Label(gen, text="Select a color:", justify=tk.LEFT, padx=5).pack()

    tk.Radiobutton(gen, text="White", padx=20, variable=v, value=1).pack(anchor=tk.W)
    tk.Radiobutton(gen, text="Blue", padx=20, variable=v, value=2).pack(anchor=tk.W)
    tk.Radiobutton(gen, text="Red", padx=20, variable=v, value=3).pack(anchor=tk.W)
    tk.Radiobutton(gen, text="Orange", padx=20, variable=v, value=4).pack(anchor=tk.W)
    tk.Radiobutton(gen, text="Yellow", padx=20, variable=v, value=5).pack(anchor=tk.W)
    tk.Radiobutton(gen, text="Pink", padx=20, variable=v, value=6).pack(anchor=tk.W)
    input_text = tk.Entry(gen)
    input_text.insert(-1, 'Ex: white')
    input_text.pack(anchor=tk.W)

    def exit_color(input_text, v):
        global custom, integer
        value = integer.get()
        color(value, custom)
        custom = input_text.get()
        if custom == 'Ex: white':
            custom = ''
        gen.destroy()
        gen.update()

    tk.Button(gen, text="Confirm", padx=15, pady=15, command=lambda: exit_color(input_text, v)).pack(anchor=tk.W)


def move_right():
    global x, y, distance
    x = int(t.pos()[0])
    y = int(t.pos()[1])
    t.goto(x + distance, y)


def move_left():
    global x, y, distance
    x = int(t.pos()[0])
    y = int(t.pos()[1])
    t.goto(x - distance, y)


def move_up():
    global x, y, distance
    x = int(t.pos()[0])
    y = int(t.pos()[1])
    t.goto(x, y + distance)


def move_down():
    global x, y, distance
    x = int(t.pos()[0])
    y = int(t.pos()[1])
    t.goto(x, y - distance)


def toggle_pen():
    global toggle
    if toggle == 0:
        t.penup()
        toggle = 1
    else:
        t.pendown()
        toggle = 0


def clear_page():
    t.clear()


def distance_ten():
    global distance
    distance = 10


def distance_nine():
    global distance
    distance = 9


def distance_eight():
    global distance
    distance = 8


def distance_seven():
    global distance
    distance = 7


def distance_six():
    global distance
    distance = 6


def distance_five():
    global distance
    distance = 5


def distance_four():
    global distance
    distance = 4


def distance_three():
    global distance
    distance = 3


def distance_two():
    global distance
    distance = 2


def distance_one():
    global distance
    distance = 1


popupmsg()
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")
t.onkey(move_right, "Right")
t.onkey(move_left, "Left")
t.onkey(move_up, "w")
t.onkey(move_down, "s")
t.onkey(move_right, "d")
t.onkey(move_left, "a")
t.onkey(toggle_pen, "space")
t.onkey(toggle_pen, "e")
t.onkey(clear_page, "r")
t.onkey(distance_ten, "0")
t.onkey(distance_nine, "9")
t.onkey(distance_eight, "8")
t.onkey(distance_seven, "7")
t.onkey(distance_six, "6")
t.onkey(distance_five, "5")
t.onkey(distance_four, "4")
t.onkey(distance_three, "3")
t.onkey(distance_two, "2")
t.onkey(distance_one, "1")
t.onkey(color_select, 'c')

t.listen()
turtle_root.protocol("WM_DELETE_WINDOW", on_close)
turtle_root.wait_window()
try:
    popup.destroy()
except:
    None
try:
    gen.destroy()
except:
    None
