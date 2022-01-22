from turtle import *

hideturtle()
Screen().bgcolor("black")
speed(0)

penup()
for x in range(-500, 500, 30):
    goto(x, -7)
    dot(4, "white")

for x in range(0, 200, 15):
    penup()
    color("white")

    goto(x,0)
    pendown()
    goto(x-100, 0)
    goto(x-100,20)
    goto(x-80,20)
    goto(x-60,35)
    goto(x-40,35)
    goto(x-20,20)
    goto(x,20)
    goto(x,0)

    penup()
    goto(x-80,-5)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    penup()
    goto(x-20,-5)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    penup()
    goto(x,10)
    color("yellow")
    pendown()
    begin_fill()
    goto(x+80,40)
    goto(x+80,0)
    goto(x,10)
    penup()
    end_fill()



    penup()
    color("black")
    begin_fill()
    goto(x+84,-6)
    goto(x+84,44)
    goto(x-104,44)
    goto(x-104,-6)
    goto(x+84,-6)
    end_fill()

done()