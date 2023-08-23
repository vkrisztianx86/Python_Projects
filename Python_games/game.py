import time
import turtle

# WINDOW
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor('grey')
window.title('PONG')
window.tracer(2)

# LEFT HAND SIDE BAT
left_bat = turtle.Turtle()
left_bat.speed(0)
left_bat.shape('square')
left_bat.shapesize(stretch_wid=5, stretch_len=1)
left_bat.color('black')
left_bat.penup()
left_bat.goto(-350, 0)

# RIGHT HAND SIDE BAT
right_bat = turtle.Turtle()
right_bat.speed(0)
right_bat.shape('square')
right_bat.shapesize(stretch_wid=5, stretch_len=1)
right_bat.color('brown')
right_bat.penup()
right_bat.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(0, 0)
ball.changesX = 1.5
ball.changesY = -1.5

# SCORES
right_score = 0
left_score = 0

score = turtle.Turtle()
score.speed(0)
score.color('blue')
score.penup()
score.hideturtle()
score.goto(0, 260)

score.write(f'Left-side player: {left_score} Right-side player: {right_score} ',
            align='center', font=('Curier', 24, 'normal'))

def left_bat_up():
    y = left_bat.ycor()
    y += 40
    left_bat.sety(y)
    if y > 280:
        left_bat.sety(280)

def left_bat_down():
    y = left_bat.ycor()
    y -= 40
    left_bat.sety(y)
    if y < -280:
        left_bat.sety(-280)

def right_bat_up():
    y = right_bat.ycor()
    y += 40
    right_bat.sety(y)
    if y > 280:
        right_bat.sety(280)

def right_bat_down():
    y = right_bat.ycor()
    y -= 40
    right_bat.sety(y)
    if y < -280:
        right_bat.sety(-280)

window.onkey(left_bat_up, 'w')
window.onkey(left_bat_down, 's')

window.onkey(right_bat_up, 'o')
window.onkey(right_bat_down, 'k')

window.listen()

while True:
    # screen refresh
    time.sleep(1 / 240)
    window.update()
    ball.setx(ball.xcor() + ball.changesX)
    ball.sety(ball.ycor() + ball.changesY)

    # bounce from top
    if ball.ycor() > 288:
        ball.sety(288)
        ball.changesY *= -1

    # bounce from bottom
    if ball.ycor() < -288:
        ball.sety(-288)
        ball.changesY *= -1

    # touch right side
    if ball.xcor() > 388:
        ball.goto(0,0)
        ball.changesX *= -1
        left_score += 1
        score.clear()
        score.write(f'Left-side player: {left_score} Right-side player: {right_score} ',
                    align='center', font=('Curier', 24, 'normal'))

    # touch left side
    if ball.xcor() < -388:
        ball.goto(0,0)
        ball.changesX *= -1
        right_score += 1
        score.clear()
        score.write(f'Left-side player: {left_score} Right-side player: {right_score}',
                    align='center', font=('Curier', 24, 'normal'))

    # bouncing from right bat
    if right_bat.xcor() -20 < ball.xcor() < right_bat.xcor() and right_bat.ycor() - 55 < ball.ycor() < right_bat.ycor() + 50:
        ball.setx(right_bat.xcor() - 20)
        ball.changesX *= -1

    # bouncing from left bat
    if left_bat.xcor() + 20 > ball.xcor() > left_bat.xcor() and left_bat.ycor() - 55 < ball.ycor() < left_bat.ycor() + 50:
        ball.setx(left_bat.xcor() + 20)
        ball.changesX *= -1











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
