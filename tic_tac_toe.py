from turtle import *
import tkinter as tk

turn = 1
tie_count = -1
hideturtle()
Screen().bgcolor("black")
speed(0)
used = []
winner = False
win_check = [
             [], [], [],
             [], [], [],
             [], [], []
             ]


def popupmsg(one_or_two):
    global winner
    Screen().bye()
    if one_or_two == 3:
        popup = tk.Tk()
        popup.wm_title("DRAW!")
        label = tk.Label(popup, text=f"Neither players won!")
        label.pack(side="top", fill="x", pady=20, padx=80)
        B1 = tk.Button(popup, text="Better luck next time!", command = popup.destroy)
        B1.pack()
        popup.mainloop()
    else:
        popup = tk.Tk()
        popup.wm_title("WINNER!")
        label = tk.Label(popup, text=f"Player {one_or_two} wins!!!")
        label.pack(side="top", fill="x", pady=20, padx=80)
        B1 = tk.Button(popup, text="Woohoo!", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        winner = True


def drawboard():
    color("white")
    penup()
    goto(60, -180)
    pendown()
    goto(60, 180)

    penup()
    goto(180, 60)
    pendown()
    goto(-180, 60)

    penup()
    goto(-180, -60)
    pendown()
    goto(180, -60)

    penup()
    goto(-60, 180)
    pendown()
    goto(-60, -180)
    penup()


def circles(p2_position):
    color("blue")
    pensize(2)
    if p2_position == 1:
        penup()  # 1
        goto(-120, 60)
        pendown()
        circle(60)
        penup()

    elif p2_position == 2:
        penup()  # 2
        goto(0, 60)
        pendown()
        circle(60)
        penup()

    elif p2_position == 3:
        penup()  # 3
        goto(120, 60)
        pendown()
        circle(60)
        penup()

    elif p2_position == 4:
        penup()  # 4
        goto(-120, -60)
        pendown()
        circle(60)
        penup()

    elif p2_position == 5:
        penup()  # 5
        goto(0, -60)
        pendown()
        circle(60)
        penup()

    elif p2_position == 6:
        penup()  # 6
        goto(120, -60)
        pendown()
        circle(60)
        penup()

    elif p2_position == 7:
        penup()  # 7
        goto(-120, -180)
        pendown()
        circle(60)
        penup()

    elif p2_position == 8:
        penup()  # 8
        goto(0, -180)
        pendown()
        circle(60)
        penup()

    elif p2_position == 9:
        penup()  # 9
        goto(120, -180)
        pendown()
        circle(60)
        penup()


def naughts(p1_position):
    color("red")
    pensize(2)
    if p1_position == 1:
        penup()  # 1
        goto(-180, 180)
        pendown()
        goto(-60, 60)
        penup()
        goto(-180, 60)
        pendown()
        goto(-60, 180)
        penup()

    elif p1_position == 2:
        penup()  # 2
        goto(-60, 180)
        pendown()
        goto(60, 60)
        penup()
        goto(-60, 60)
        pendown()
        goto(60, 180)
        penup()

    elif p1_position == 3:
        penup()  # 3
        goto(60, 60)
        pendown()
        goto(180, 180)
        penup()
        goto(60, 180)
        pendown()
        goto(180, 60)
        penup()

    elif p1_position == 4:
        penup()  # 4
        goto(-180, 60)
        pendown()
        goto(-60, -60)
        penup()
        goto(-180, -60)
        pendown()
        goto(-60, 60)
        penup()

    elif p1_position == 5:
        penup()  # 5
        goto(-60, -60)
        pendown()
        goto(60, 60)
        penup()
        goto(-60, 60)
        pendown()
        goto(60, -60)
        penup()

    elif p1_position == 6:
        penup()  # 6
        goto(60, 60)
        pendown()
        goto(180, -60)
        penup()
        goto(60, -60)
        pendown()
        goto(180, 60)
        penup()

    elif p1_position == 7:
        penup()  # 7
        goto(-180, -60)
        pendown()
        goto(-60, -180)
        penup()
        goto(-60, -60)
        pendown()
        goto(-180, -180)
        penup()

    elif p1_position == 8:
        penup()  # 8
        goto(-60, -60)
        pendown()
        goto(60, -180)
        penup()
        goto(60, -60)
        pendown()
        goto(-60, -180)
        penup()

    elif p1_position == 9:
        penup()  # 9
        goto(60, -60)
        pendown()
        goto(180, -180)
        penup()
        goto(60, -180)
        pendown()
        goto(180, -60)
        penup()


def center():
    global turn, win_check
    if "center" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=5)
            win_check[4] = 1
            won()
            turn = 2
        else:
            circles(p2_position=5)
            win_check[4] = 0
            won()
            turn = 1
        used.append("center")


def center_right():
    global turn, win_check
    if "center_right" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=6)
            win_check[5] = 1
            won()
            turn = 2
        else:
            circles(p2_position=6)
            win_check[5] = 0
            won()
            turn = 1
        used.append("center_right")


def center_left():
    global turn, win_check
    if "center_left" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=4)
            win_check[3] = 1
            won()
            turn = 2
        else:
            circles(p2_position=4)
            win_check[3] = 0
            won()
            turn = 1
        used.append("center_left")


def top():
    global turn, win_check
    if "top" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=2)
            win_check[1] = 1
            won()
            turn = 2
        else:
            circles(p2_position=2)
            win_check[1] = 0
            won()
            turn = 1
        used.append("top")


def top_right():
    global turn, win_check
    if "top_right" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=3)
            win_check[2] = 1
            won()
            turn = 2
        else:
            circles(p2_position=3)
            win_check[2] = 0
            won()
            turn = 1
        used.append("top_right")


def top_left():
    global turn, win_check
    if "top_left" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=1)
            win_check[0] = 1
            won()
            turn = 2
        else:
            circles(p2_position=1)
            win_check[0] = 0
            won()
            turn = 1
        used.append("top_left")


def bottom():
    global turn, win_check
    if "bottom" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=8)
            win_check[7] = 1
            won()
            turn = 2
        else:
            circles(p2_position=8)
            win_check[7] = 0
            won()
            turn = 1
        used.append("bottom")


def bottom_right():
    global turn, win_check
    if "bottom_right" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=9)
            win_check[8] = 1
            won()
            turn = 2
        else:
            circles(p2_position=9)
            win_check[8] = 0
            won()
            turn = 1
        used.append("bottom_right")


def bottom_left():
    global turn, win_check
    if "bottom_left" in used:
        None
    else:
        if turn == 1:
            naughts(p1_position=7)
            win_check[6] = 1
            won()
            turn = 2
        else:
            circles(p2_position=7)
            win_check[6] = 0
            won()
            turn = 1
        used.append("bottom_left")


def box_location(x, y):
    global area


    goto(x,y)
    if x <= -60 and x >= -180 and y >= 60 and y <= 180:
        top_left()
    elif x >= -60 and x <= 60 and y >= 60 and y <= 180:
        top()
    elif x >= 60 and x <= 180 and y >= 60 and y <= 180:
        top_right()
    elif x <= -60 and x >= -180 and y >= -60 and y <= 60:
        center_left()
    elif x >= -60 and x <= 60 and y >= -60 and y <= 60:
        center()
    elif x >= 60 and x <= 180 and y >= -60 and y <= 60:
        center_right()
    elif x <= -60 and x >= -180 and y >= -180 and y <= -60:
        bottom_left()
    elif x >= -60 and x <= 60 and y >= -180 and y <= -60:
        bottom()
    elif x >= 60 and x <= 180 and y >= -180 and y <= -60:
        bottom_right()
    else:
        None


drawboard()
onscreenclick(box_location)


def won():
    global tie_count, winner
    if win_check[0] == 1 and win_check[1] == 1 and win_check[2] == 1:
        popupmsg(one_or_two=1)
    elif win_check[0] == 0 and win_check[1] == 0 and win_check[2] == 0:
        popupmsg(one_or_two=2)
    elif win_check[3] == 1 and win_check[4] == 1 and win_check[5] == 1:
        popupmsg(one_or_two=1)
    elif win_check[3] == 0 and win_check[4] == 0 and win_check[5] == 0:
        popupmsg(one_or_two=2)
    elif win_check[6] == 1 and win_check[7] == 1 and win_check[8] == 1:
        popupmsg(one_or_two=1)
    elif win_check[6] == 0 and win_check[7] == 0 and win_check[8] == 0:
        popupmsg(one_or_two=2)

    if win_check[0] == 1 and win_check[3] == 1 and win_check[6] == 1:
        popupmsg(one_or_two=1)
    elif win_check[0] == 0 and win_check[3] == 0 and win_check[6] == 0:
        popupmsg(one_or_two=2)
    elif win_check[1] == 1 and win_check[4] == 1 and win_check[7] == 1:
        popupmsg(one_or_two=1)
    elif win_check[1] == 0 and win_check[4] == 0 and win_check[7] == 0:
        popupmsg(one_or_two=2)
    elif win_check[2] == 1 and win_check[5] == 1 and win_check[8] == 1:
        popupmsg(one_or_two=1)
    elif win_check[2] == 0 and win_check[5] == 0 and win_check[8] == 0:
        popupmsg(one_or_two=2)

    if win_check[0] == 1 and win_check[4] == 1 and win_check[8] == 1:
        popupmsg(one_or_two=1)
    elif win_check[0] == 0 and win_check[4] == 0 and win_check[8] == 0:
        popupmsg(one_or_two=2)
    elif win_check[2] == 1 and win_check[4] == 1 and win_check[6] == 1:
        popupmsg(one_or_two=1)
    elif win_check[2] == 0 and win_check[4] == 0 and win_check[6] == 0:
        popupmsg(one_or_two=2)

    tie_count = tie_count + 1
    if tie_count == 8 and winner == False:
        popupmsg(one_or_two=3)


done()
