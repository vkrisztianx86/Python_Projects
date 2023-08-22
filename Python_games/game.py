import time
import turtle

# WINDOW
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor('brown')
window.title('PONG')
window.tracer(0)

# Left hand side bat
left_bat = turtle.Turtle()
left_bat.speed(0)
left_bat.shape('square')
left_bat.shapesize(stretch_wid=5, stretch_len=1)
left_bat.color('white')
left_bat.penup()
left_bat.goto(-350, 0)

# Right hand side bat
right_bat = turtle.Turtle()
right_bat.speed(0)
right_bat.shape('square')
right_bat.shapesize(stretch_wid=5, stretch_len=1)
right_bat.color('white')
right_bat.penup()
right_bat.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.changesX = 1
ball.changesY = 0

def left_bat_up():
    y = left_bat.ycor()
    y += 30
    left_bat.sety(y)

def left_bat_down():
    y = left_bat.ycor()
    y -= 30
    left_bat.sety(y)

def right_bat_up():
    y = right_bat.ycor()
    y += 30
    right_bat.sety(y)

def right_bat_down():
    y = right_bat.ycor()
    y -= 30
    right_bat.sety(y)

window.onkey(left_bat_up, 'w')
window.onkey(left_bat_down, 's')

window.onkey(right_bat_up, 'o')
window.onkey(right_bat_down, 'k')

window.listen()

while True:
    #screen refresh
    window.update()
    ball.setx(ball.xcor() + ball.changesX)
    ball.sety(ball.ycor() + ball.changesY)

    #bounce from top
    if ball.ycor() > 288:
        ball.sety(288)
        ball.changesY *= -1

    #bounce from bottom
    if ball.ycor() < -288:
        ball.sety(-288)
        ball.changesY *= -1











# manoturtle = turtle.Turtle()
#
# manoturtle.speed(1)
# manoturtle.shape('square')
# manoturtle.color('green')
# manoturtle.shapesize(stretch_wid=5, stretch_len=1)
# manoturtle.penup()
#
# manoturtle.forward(100)
# manoturtle.right(90)
# manoturtle.forward(100)
# manoturtle.right(90)
# manoturtle.forward(100)
# manoturtle.right(90)
# manoturtle.forward(100)
# manoturtle.right(90)
